import pytest
import yes_no_words


def test_all():
    assert len(yes_no_words.ALL)


def test_all_random():
    word = yes_no_words.all_random()
    assert len(word)
    assert word in yes_no_words.ALL
    assert "not" in yes_no_words.ALL
    assert "yes" in yes_no_words.ALL


def test_no():
    assert len(yes_no_words.NO)
    assert "no" in yes_no_words.NO
    assert "no" not in yes_no_words.YES
    assert "false" in yes_no_words.NO


def test_no_random():
    word = yes_no_words.no_random()
    assert len(word)
    assert "not" in yes_no_words.NO
    assert "yes" not in yes_no_words.NO
    assert word in yes_no_words.NO
    assert word not in yes_no_words.YES


def test_yes():
    assert len(yes_no_words.YES)
    assert "yes" in yes_no_words.YES
    assert "yes" not in yes_no_words.NO
    assert "true" in yes_no_words.YES


def test_yes_random():
    word = yes_no_words.yes_random()
    assert len(word)
    assert "yes" in yes_no_words.YES
    assert "not" not in yes_no_words.YES
    assert word in yes_no_words.YES
    assert word not in yes_no_words.NO


@pytest.mark.parametrize("test_input", tuple(yes_no_words.NO))
def test_is_falsy(test_input):
    assert yes_no_words.is_falsy(test_input)
    assert not yes_no_words.is_truthy(test_input)


@pytest.mark.parametrize("test_input", tuple(yes_no_words.YES))
def test_is_truthy(test_input):
    assert yes_no_words.is_truthy(test_input)
    assert not yes_no_words.is_falsy(test_input)
