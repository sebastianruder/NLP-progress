import argparse
import os
import pprint
from typing import Dict, Tuple, List
import re
import sys
import json

class Debug:
    counter = 1

def extract_title_and_link(md_link:str) -> Tuple:
    """
    Extract the anchor text and URL from a markdown link

    :param md_link: a string of ONLY the markdown link, e.g. "[google](http://google.com)"
    :return: e.g. the tuple (google, http://google.com)
    """
    title = re.findall("^\\[(.*)\\]", md_link)[0].strip()
    link = re.findall("\\((.*)\\)$", md_link)[0].strip()

    return title, link


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
    cols_sanitized = [re.sub(" +", "", h) for h in cols_sanitized]

    # find the model name column (usually the first one)
    if "model" in cols_sanitized:
        model_inx = cols_sanitized.index("model")
    else:
        print("ERROR: Model name not found in this SOTA table, skipping...\n", file=sys.stderr)
        print("".join(table_lines), file=sys.stderr)
        return {}

    if "paper/source" in cols_sanitized:
        paper_inx = cols_sanitized.index("paper/source")
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

        sota_row = {
            "model_name": row_cols[model_inx],
            "metrics": metrics,
        }

        if paper_title is not None and paper_link is not None:
            sota_row["paper_title"] = paper_title
            sota_row["paper_url"] = paper_link

        # and code links if they exist
        if code_inx is not None:
            sota_row["code_links"] = extract_code_links(row_cols[code_inx])

        sota["rows"].append(sota_row)

    #Debug.counter -= 1
    #if Debug.counter == 0:
    #    from IPython import embed; embed()

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

            # reset the last dataset
            ds = None

        ### Dataset definition
        if header.startswith("###") and not header.startswith("####"):
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
            ds["description"] = "".join([s for s in section[1:] if not s.startswith("|")]).strip()

            table_lines = [s for s in section if s.startswith("|")]
            if table_lines:
                ds["sota"] = extract_sota_table(table_lines)

    if t:
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
    parser.add_argument("languages", nargs="+", type=str)
    parser.add_argument("--output", default="export.json", type=str)

    args = parser.parse_args()

    out = []
    for language in args.languages:
        out.extend(parse_markdown_directory(language))

    with open(args.output, "w") as f:
        f.write(json.dumps(out, indent=2))