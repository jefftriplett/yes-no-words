import nox


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"], reuse_venv=True)
def test(session):
    session.install(".")
    session.install("--requirement=requirements.txt")
    session.run("pytest")
