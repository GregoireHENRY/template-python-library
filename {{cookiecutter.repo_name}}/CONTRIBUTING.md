# Contributing to **{{cookiecutter.project_name}}**

## Practices

Some useful links:

+ [How to Contribute to an Open Source Project on GitHub](https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github)
+ [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit)
+ [Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
+ [How to Be a Good Open Source Project Owner – The Ultimate Guide](https://www.freecodecamp.org/news/ultimate-owners-guide-to-open-source/#how-to-automate-your-process)
+ [Forking Projects Guide](https://guides.github.com/activities/forking)

## Environment

Clone project, create a fork and add your fork as a new remote. Install the
dependency and packaging manager [poetry][poetry url].

Install {{cookiecutter.project_name}} depencencies:

```sh
poetry install --dev
```

Start the virtual environment:

```sh
poetry shell
```

Install [`pre-commit`][pre-commit url] to prevent commit not following guide
style.

```sh
pre-commit install
```

### Merge requests

Make a pull request with a single commit onto the (`main`) branch.

*Thank you for your time contributing!!*

[pre-commit url]: https://pre-commit.com
[poetry url]: https://python-poetry.org/docs
