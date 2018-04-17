import re
import pathlib

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

def get_talk_file(directory_path, root="index",
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
        out += """<li>
        <span class="post-date">{} [{}]</span>
        <a class="post-link" href="{}">{}</a>
        </li>
        """.format(date, talk_file.suffix, talk_file, title)

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
