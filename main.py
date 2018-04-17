import markdown
import pathlib
import re

def get_date(directory_path):
    """
    Returns the date in ISO format at the start of the name of a directory
    """
    date_regex = '(19|20)\d\d[- ./](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])'
    try:
        return re.search(date_regex,
                         directory_path.stem[:len('yyyy-mm-dd')]).group()
    except AttributeError:
        return None

def get_title(directory_path):
    """
    Returns the title of the directory
    """
    title = directory_path.stem[len('yyyy-mm-dd'):]
    return title.replace("-", " ")

def get_talk_file(directory_path, root="main",
                  valid=[".pdf", ".html", ".link"]):
    """
    Returns the correct file exension
    """
    for p in directory_path.glob("{}.*".format(root)):
        if p.suffix in valid:
            return p

def find_directories(root="./"):
    """
    Returns all directories in root that contain a date in the name.
    """
    path = pathlib.Path(root)
    for p in path.glob("./*"):
        date = get_date(p)
        if p.is_dir() and date is not None:
            title = get_title(p)
            talk_file = get_talk_file(p)
            yield p, date, title, talk_file

def write_directory(path, index_file="main.md",
                    head=pathlib.Path("./head.html"),
                    header=pathlib.Path("./header.html"),
                    footer=pathlib.Path("./footer.html")):
    """
    Given a directory with a single markdown file create an `index.html`
    """
    path = pathlib.Path(path) / index_file
    html = markdown.markdown(path.read_text())

    out = head.read_text()
    out += header.read_text()
    out +=  """
<body>
<div class="page-content">
<div class="wrap">
<div class="home">
"""
    out += html
    out += """
</div>
</div>
</div>
"""
    out += footer.read_text()

    pathlib.Path("./rider.html").write_text(out)


if __name__ == "__main__":
    head = pathlib.Path("./head.html")
    out = head.read_text()

    header = pathlib.Path("./header.html")
    out += header.read_text()

    out +=  """
<body>
<div class="page-content">
<div class="wrap">
<div class="home">
<ul class='posts'>"""

    directories = sorted(list(find_directories()),
                         key=lambda x: x[1], reverse=True)

    for path, date, title, talk_file in directories:
        if talk_file.suffix == ".link":
            talk_file = talk_file.read_text()
            suffix = ".link"
        else:
            suffix = talk_file.suffix

        out += """<li>
        <span class="post-date">{} [{}]</span>
        <a class="post-link" href="{}">{}</a>
        </li>
        """.format(date, suffix, talk_file, title)

    out += """
</ul>
</div>
</div>
</div>
"""
    footer = pathlib.Path("./footer.html")
    out += footer.read_text()

    out_path = pathlib.Path("./index.html")
    out_path.write_text(out)

    write_directory(pathlib.Path("./rider"))
