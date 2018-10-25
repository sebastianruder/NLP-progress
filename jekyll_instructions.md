# Instructions for building the site locally

You can build the site locally using Jekyll by following the steps detailed
[here](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/#requirements):

1. Check whether you have Ruby 2.1.0 or higher installed with `ruby --version`, otherwise [install it](https://www.ruby-lang.org/en/downloads/).
On OS X for instance, this can be done with `brew install ruby`. Make sure you also have `ruby-dev` and `zlib1g-dev` installed.
1. Install Bundler `gem install bundler`. If you run into issues with installing bundler on OS X, have a look
[here](https://bundler.io/v1.16/guides/rubygems_tls_ssl_troubleshooting_guide.html) for troubleshooting tips. Also try refreshing
the terminal.
1. Clone the repo locally: `git clone https://github.com/sebastianruder/NLP-progress`
1. Navigate to the repo with `cd NLP-progress`
1. Install Jekyll: `bundle install`
1. Run the Jekyll site locally: `bundle exec jekyll serve`
1. You can now preview the local Jekyll site in your browser at `http://localhost:4000`.
