@_default:
    just --list

lint:
    black .
    blacken-docs ./README.md
