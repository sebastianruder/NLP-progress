import argparse
import os
import pprint
from typing import Dict, Tuple, List
import re
import sys
import json


def extract_dataset_desc_links(desc:List[str]) -> List:
    """
    Extract all the links from the description of datasets

    :param desc: Lines of the description of the dataset
    :return:
    """

    out = []
    md = "".join(desc)

    md_links = re.findall("\\[.*\\]\\(.*\\)", md)

    for md_link in md_links:
        title, link = extract_title_and_link(md_link)
        out.append({
            "title": title,
            "url": link,
        })

    return out


def sanitize_subdataset_name(name:str):
    """
    Do some sanitization on automatically extracted subdataset name

    :param name: raw subdataset name line
    :return:
    """

    name = name.replace("**", "")
    if name.endswith(":"):
        name = name[:-1]

    return name.strip()


def extract_lines_before_tables(lines:List[str]):
    """
    Extract the non-empty line before the table

    :param lines: a list of lines
    :return:
    """

    out = []

    before = None
    in_table = False
    for l in lines:
        if l.startswith("|") and not in_table:
            if before is not None:
                out.append(before)
            in_table = True
        elif in_table and not l.startswith("|"):
            in_table = False
            before = None
            if l.strip() != "":
                before = l.strip()
        elif l.strip() != "":
            before = l.strip()

    return out


def handle_multiple_sota_table_exceptions(section:List[str], sota_tables:List[List[str]]):
    """
    Manually handle the edge cases with dataset partitions

    These are not captured in a consistent format, so no unified approach is possible atm.

    :param section: The lines in this section
    :param sota_tables: The list of sota table lines
    :return:
    """

    section_full = "".join(section)
    out = []

    # Use the line before the table
    subdatasets = extract_lines_before_tables(section)
    subdatasets = [sanitize_subdataset_name(s) for s in subdatasets]

    # exceptions:
    if "hypernym discovery evaluation benchmark" in section_full:
        subdatasets = subdatasets[1:]

    if len(subdatasets) != len(sota_tables):
        print("ERROR parsing the subdataset SOTA tables", file=sys.stderr)
        print(sota_tables, file=sys.stderr)
    else:
        for i in range(len(subdatasets)):
            out.append({
                "subdataset": subdatasets[i],
                "sota": extract_sota_table(sota_tables[i])
            })

    return out


def extract_title_and_link(md_link:str) -> Tuple:
    """
    Extract the anchor text and URL from a markdown link

    :param md_link: a string of ONLY the markdown link, e.g. "[google](http://google.com)"
    :return: e.g. the tuple (google, http://google.com)
    """
    title = re.findall("^\\[(.*)\\]", md_link)[0].strip()
    link = re.findall("\\((.*)\\)$", md_link)[0].strip()

    return title, link


def extract_model_name_and_author(md_name:str) -> Tuple:
    """
    Extract the model name and author, if provided

    :param md_name: a string with the model name from the sota table
    :return: tuple (model_name, author_names)
    """

    if ' (' in md_name and ')' in md_name:
        model_name = md_name.split(' (')[0]
        model_authors = md_name.split(' (')[1].split(')')[0]
    elif '(' in md_name and ')' in md_name: # only has author name
        model_name = None
        model_authors = md_name
    else:
        model_name = md_name
        model_authors = None

    return model_name, model_authors


def extract_paper_title_and_link(paper_md:str) -> Tuple:
    """
    Extract the title and link to the paper

    :param paper_md: markdown for the paper link
    :return: tuple (paper_title, paper_link)
    """

    md_links = re.findall("\\[.*\\]\\(.*\\)", paper_md)

    if len(md_links) > 1:
        print("WARNING: Found multiple paper references: `%s`, using only the first..." % paper_md)
    if len(md_links) == 0:
        return None, None

    md_link = md_links[0]

    paper_title, paper_link = extract_title_and_link(md_link)
    return paper_title, paper_link


def extract_code_links(code_md:str) -> List[Dict]:
    """
    Extract the links to all code implementations

    :param code_md:
    :return:
    """

    md_links = re.findall("\\[.*\\]\\(.*\\)", code_md)

    links = []
    for md_link in md_links:
        t, l = extract_title_and_link(md_link)
        links.append({
            "title": t,
            "url": l,
        })

    return links


def extract_sota_table(table_lines:List[str]) -> Dict:
    """
    Parse a SOTA table out of lines in markdown

    :param table_lines: lines in the SOTA table
    :return:
    """

    sota = {}

    header = table_lines[0]
    header_cols = [h.strip() for h in header.split("|") if h.strip()]
    cols_sanitized = [h.lower() for h in header_cols]
    cols_sanitized = [re.sub(" +", "", h).replace("**","") for h in cols_sanitized]

    # find the model name column (usually the first one)
    if "model" in cols_sanitized:
        model_inx = cols_sanitized.index("model")
    else:
        print("ERROR: Model name not found in this SOTA table, skipping...\n", file=sys.stderr)
        print("".join(table_lines), file=sys.stderr)
        return {}

    if "paper/source" in cols_sanitized:
        paper_inx = cols_sanitized.index("paper/source")
    elif "paper" in cols_sanitized:
        paper_inx = cols_sanitized.index("paper")
    else:
        print("ERROR: Paper reference not found in this SOTA table, skipping...\n", file=sys.stderr)
        print("".join(table_lines), file=sys.stderr)
        return {}

    if "code" in cols_sanitized:
        code_inx = cols_sanitized.index("code")
    else:
        code_inx = None

    metrics_inx = set(range(len(header_cols))) - set([model_inx, paper_inx, code_inx])
    metrics_inx = sorted(list(metrics_inx))

    metrics_names = [header_cols[i] for i in metrics_inx]

    sota["metrics"] = metrics_names
    sota["rows"] = []

    min_cols = len(header_cols)

    # now parse the table rows
    rows = table_lines[2:]
    for row in rows:
        row_cols = [h.strip() for h in row.split("|")][1:]

        if len(row_cols) < min_cols:
            print("This row doesn't have enough columns, skipping: %s" % row, file=sys.stderr)
            continue

        # extract all the metrics
        metrics = {}
        for i in range(len(metrics_inx)):
            metrics[metrics_names[i]] = row_cols[metrics_inx[i]]

        # extract paper references
        paper_title, paper_link = extract_paper_title_and_link(row_cols[paper_inx])

        # extract model_name and author
        model_name, model_author = extract_model_name_and_author(row_cols[model_inx])

        sota_row = {
            "model_name": model_name,
            "metrics": metrics,
        }

        if paper_title is not None and paper_link is not None:
            sota_row["paper_title"] = paper_title
            sota_row["paper_url"] = paper_link

        # and code links if they exist
        if code_inx is not None:
            sota_row["code_links"] = extract_code_links(row_cols[code_inx])

        sota["rows"].append(sota_row)

    return sota


def get_line_no(sections:List[str], section_index:int, section_line=0) -> int:
    """
    Get the line number for a section heading

    :param sections: A list of list of sections
    :param section_index: Index of the current section
    :param section_line: Index of the line within the section
    :return:
    """
    if section_index == 0:
        return 1+section_line
    lens = [len(s) for s in sections[:section_index]]
    return sum(lens)+1+section_index


def extract_dataset_desc_and_sota_table(md_lines:List[str]) -> Tuple:
    """
    Extract the lines that are the description and lines that are the sota table(s)

    :param md_lines: a list of lines in this section
    :return:
    """

    # Main assumption is that the Sota table will minimally have a "Model" column
    desc = []
    tables = []
    t = None
    in_table = False
    for l in md_lines:
        if l.startswith("|") and "model" in l.lower() and not in_table:
            t = [l]
            in_table = True
        elif in_table and l.startswith("|"):
            t.append(l)
        elif in_table and not l.startswith("|"):
            if t is not None:
                tables.append(t)
            t = None
            desc.append(l)
            in_table = False
        else:
            desc.append(l)

    if t is not None:
        tables.append(t)

    return desc, tables


def parse_markdown_file(md_file:str) -> List:
    """
    Parse a single markdown file

    :param md_file: path to the markdown file
    :return:
    """

    with open(md_file, "r") as f:
        md_lines = f.readlines()

    # Assumptions:
    # 1) H1 are tasks
    # 2) Everything until the next heading is the task description
    # 3) H2 are subtasks, H3 are datasets, H4 are subdatasets

    # Algorithm:
    # 1) Split the document by headings

    sections = []
    cur = []
    for line in md_lines:
        if line.startswith("#"):
            if cur:
                sections.append(cur)
                cur = [line]
            else:
                cur = [line]
        else:
            cur.append(line)

    if cur:
        sections.append(cur)

    # 2) Parse each heading section one-by-one
    parsed_out = []  # whole parsed output
    t = {}  # current task element being parsed
    st = None  # current subtask being parsed
    ds = None # current dataset being parsed
    for section_index in range(len(sections)):
        section = sections[section_index]
        header = section[0]

        # Task definition
        if header.startswith("#") and not header.startswith("##"):
            if "task" in t:
                parsed_out.append(t)
                t = {}
            t["task"] = header[1:].strip()
            t["description"] = "".join(section[1:]).strip()

            # reset subtasks and datasets
            st = None
            ds = None

        ## Subtask definition
        if header.startswith("##") and not header.startswith("###"):
            if "task" not in t:
                print("ERROR: Unexpected subtask without a parent task at %s:#%d" %
                      (md_file, get_line_no(sections, section_index)), file=sys.stderr)

            if "subtasks" not in t:
                t["subtasks"] = []

            # new substask
            st = {}
            t["subtasks"].append(st)

            st["task"] = header[2:].strip()
            st["description"] = "".join(section[1:]).strip()
            st["source_link"] = {
                "title": "NLP-progress",
                "url": "https://github.com/sebastianruder/NLP-progress"
            }

            # reset the last dataset
            ds = None

        ### Dataset definition
        if header.startswith("###") and not header.startswith("####") and "Table of content" not in header:
            if "task" not in t:
                print("ERROR: Unexpected dataset without a parent task at %s:#%d" %
                      (md_file, get_line_no(sections, section_index)), file=sys.stderr)

            if st is not None:
                # we are in a subtask, add everything here
                if "datasets" not in st:
                    st["datasets"] = []

                # new dataset and add
                ds = {}
                st["datasets"].append(ds)
            else:
                # we are in a task, add here
                if "datasets" not in t:
                    t["datasets"] = []

                ds = {}
                t["datasets"].append(ds)

            ds["dataset"] = header[3:].strip()
            # dataset description is everything that's not a table
            desc, tables = extract_dataset_desc_and_sota_table(section[1:])
            ds["description"] = "".join(desc).strip()

            # see if there is an arxiv link in the first paragraph of the description
            dataset_links = extract_dataset_desc_links(desc)
            if dataset_links:
                ds["dataset_links"] = dataset_links

            if tables:
                if len(tables) > 1:
                    ds["subdatasets"] = handle_multiple_sota_table_exceptions(section, tables)
                else:
                    ds["sota"] = extract_sota_table(tables[0])

    if t:
        t["source_link"] = {
            "title": "NLP-progress",
            "url": "https://github.com/sebastianruder/NLP-progress"
        }
        parsed_out.append(t)

    return parsed_out


def parse_markdown_directory(path:str):
    """
    Parse all markdown files in a directory

    :param path: Path to the directory
    :return:
    """
    all_files = os.listdir(path)
    md_files = [f for f in all_files if f.endswith(".md")]

    out = []
    for md_file in md_files:
        print("Processing `%s`..." % md_file)
        out.extend(parse_markdown_file(os.path.join(path, md_file)))

    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=str, help="Files or directories to convert")
    parser.add_argument("--output", default="structured.json", type=str, help="Output JSON file name")

    args = parser.parse_args()

    out = []
    for path in args.paths:
        if os.path.isdir(path):
            out.extend(parse_markdown_directory(path))
        else:
            out.extend(parse_markdown_file(path))

    with open(args.output, "w") as f:
        f.write(json.dumps(out, indent=2))