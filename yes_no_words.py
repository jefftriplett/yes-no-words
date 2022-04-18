import random

__version__ = "2022.4.3"

NO = frozenset(
    [
        "absolutely not",
        "ahhh nah",
        "cancel",
        "certainly not",
        "decline",
        "denied",
        "deny",
        "disagreed",
        "fail",
        "false",
        "forget it",
        "impossible",
        "lolno",
        "na",
        "nada",
        "nah",
        "naw",
        "nay",
        "negative",
        "negatory",
        "nein nein nein",
        "nerp",
        "never",
        "nix",
        "no way",
        "no",
        "nope",
        "not a chance",
        "not",
        "pass",
        "reject",
        "zero",
    ]
)

YES = frozenset(
    [
        "absolutely",
        "ack",
        "acknowledged",
        "affirmative",
        "agree",
        "aight",
        "all right",
        "all righty",
        "alright",
        "aye",
        "certainly",
        "cool",
        "correct",
        "definitely",
        "exactly",
        "fine",
        "fo shizzle",
        "fo sho",
        "forizzle",
        "gladly",
        "good",
        "indeed",
        "indubitably",
        "mhm",
        "of course",
        "ok",
        "okay",
        "precisely",
        "right on",
        "right",
        "roger",
        "sure thing",
        "sure",
        "surely",
        "true dat",
        "true",
        "uh-huh",
        "very well",
        "way",
        "word",
        "ya",
        "yaaasss",
        "yah",
        "ye",
        "yea",
        "yeah",
        "yeh",
        "yep",
        "yeppers",
        "yes",
        "yessir",
        "yessum",
        "yis",
        "yiss",
        "yisss",
        "you bet",
        "yup",
        "yuppers",
        "yus",
    ]
)

ALL = YES.union(NO)


def all_random():
    return random.choice(tuple(ALL))


def no_random():
    return random.choice(tuple(NO))


def yes_random():
    return random.choice(tuple(YES))


def is_falsy(word_or_phrase: str) -> bool:
    return word_or_phrase.lower() in NO


def is_truthy(word_or_phrase: str) -> bool:
    return word_or_phrase.lower() in YES
