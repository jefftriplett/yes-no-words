# yes-no-words

> Get yes/no-like words.

Inspired by: https://github.com/sindresorhus/yes-no-words

## install

```shell
pip install yes-no-words
```

## usage

```python
import yes_no_words

yes_no_words.yes_random()  # "yisss"

yes_no_words.no_random()  # "absolutely not"

# test "truthy" words
yes_no_words.is_truthy("Yisss")  # True

yes_no_words.is_truthy("nope")  # False

# test "falsy" words
yes_no_words.is_falsy("certainly not")  # True
```
## api

### `.YES`

Yes like words.

### `.NO`

No like words.

### `.ALL`

Both yes and no like words.

### `.yes_random() -> str`

Random yes like words.

### `.no_random() -> str`

Random no like words.

### `.all_random() -> str`

Random yes or no like words.

### `.is_falsy(word_or_phrase: str) -> bool`

Test a word to verify if it's falsy.

### `.is_truthy(word_or_phrase: str) -> bool`

Test a word to verify if it's truthy.

## license

Apache License 2.0 :copyright: [Jeff Triplett](https://jefftriplett.com/)
