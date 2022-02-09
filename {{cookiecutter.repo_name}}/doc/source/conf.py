import new

project = "{{cookiecutter.project_name}}"
copyright = "2022, Grégoire Henry"
author = "Grégoire Henry"
release = new.__version__

master_doc = "index"

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "autoapi.extension",
]

html_theme = "pydata_sphinx_theme"

templates_path = ["_templates"]
html_static_path = ["_static"]

exclude_patterns = [""]

primary_domain = "py"

autoapi_type = "python"
autoapi_dirs = ["../../{{cookiecutter.project_name}}"]
