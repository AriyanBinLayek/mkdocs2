import os
import mkdocs2


def write_file(path, text):
    """
    Helper function to write 'text' to the file at 'path'.
    """
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(path, "w") as output:
        output.write(text)


def test_build(tmpdir):
    input_dir = os.path.join(tmpdir, "input")
    output_dir = os.path.join(tmpdir, "output")
    template_dir = os.path.join(tmpdir, "templates")
    index_md = os.path.join(input_dir, "index.md")
    favicon = os.path.join(input_dir, "favicon.ico")
    a_md = os.path.join(input_dir, "topics", "a.md")
    b_md = os.path.join(input_dir, "topics", "b.md")
    base_html = os.path.join(template_dir, "base.html")
    write_file(index_md, "# index\n[link to a](topics/a.md) [link to b](topics/b.md)")
    write_file(a_md, "# a\n[link to b](b.md) [link to index](../index.md)")
    write_file(b_md, "# b\n[link to a](a.md) [link to index](../index.md)")
    write_file(favicon, "xxx")
    write_file(base_html, "<html><body>{{ content }}</body></html>")

    config = {
        "site": {"url": "/"},
        "build": {
            "input_dir": input_dir,
            "output_dir": output_dir,
            "template_dir": template_dir,
        },
        "nav": {
            "Homepage": "index.md",
            "Topics": {"Topic A": "topics/a.md", "Topic B": "topics/b.md"},
        },
    }
    mkdocs2.build(config=config)
