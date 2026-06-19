# 1. Setting up your tools

**You'll learn:** how to get a GitHub account, git, and Python ready, and how to
get the project running on your own computer.

## 1. A GitHub account

If you don't have one, sign up at [github.com](https://github.com). Use a name
and email you're happy to have attached to public contributions.

While you're there, it's worth setting up
[SSH keys](https://docs.github.com/authentication/connecting-to-github-with-ssh)
so you don't have to type a password every time you push. (HTTPS works too if
you'd rather skip this for now.)

## 2. Install git

Download git from [git-scm.com/downloads](https://git-scm.com/downloads), then
tell it who you are:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 3. Install Python

You need **Python 3.10 or newer**. Check what you have:

```bash
python --version    # or: python3 --version
```

If it's older or missing, install from [python.org](https://www.python.org/downloads/).

## 4. Fork and clone the project

A **fork** is your own copy of the repository on GitHub. Click **Fork** at the
top-right of the [project page](https://github.com/gxogdnd/SimpleCharacterBuilder).

Then **clone** your fork to your computer (swap in your username):

```bash
git clone https://github.com/<your-username>/SimpleCharacterBuilder.git
cd SimpleCharacterBuilder
```

## 5. Set up a virtual environment

A virtual environment keeps this project's packages separate from everything
else on your machine.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## 6. Check it works

```bash
charsheet --version
pytest
```

If you see a version number and the tests pass, you're ready.

➡️ Next: [Understanding the project](02-understanding-the-project.md)
