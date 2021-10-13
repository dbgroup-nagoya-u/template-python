# project_name

[![Python 3.9](https://github.com/dbgroup-nagoya-u/template-python/actions/workflows/push.yaml/badge.svg)](https://github.com/dbgroup-nagoya-u/template-python/actions/workflows/push.yaml)

## Usage

### Installation

```bash
pip install -e git+ssh://git@github.com/dbgroup-nagoya-u/template-python.git#egg=project_name
```

### Run Module

```bash
python -m project_name [options...] [args...]
```

### Using as a Library

Write usage of your modules...

## Development

### Prerequisites

It is assumed that [pyenv](https://github.com/pyenv/pyenv) and [pipenv](https://github.com/pypa/pipenv) are already installed.

```bash
cd <path_to_your_workspace>
git clone --recursive git@github.com:dbgroup-nagoya-u/template-python.git
cd template-python
pipenv sync -d
```
