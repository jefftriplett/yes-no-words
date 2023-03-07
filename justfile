@_default:
    just --list

@fmt:
    just --fmt --unstable

@bootstrap:
    pip install --requirement=requirements.in --upgrade
    pre-commit autoupdate

@build:
    python -m build

@check:
    twine check dist/*

@lint *ARGS="--all-files":
    pre-commit run {{ ARGS }}

@nox:
    nox

@pip-compile:
    pip-compile

@test:
    pytest

@update:
    pip install -U pip pip-tools

@upload:
    twine upload dist/*
