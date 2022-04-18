@_default:
    just --list

@build:
    python -m build

@check:
    twine check dist/*

lint:
    black .
    blacken-docs ./README.md

@test:
    pytest

@upload:
    twine upload dist/*
