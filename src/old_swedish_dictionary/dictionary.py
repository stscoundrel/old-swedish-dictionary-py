from typing import NamedTuple, Tuple

from . import reader

DICTIONARY_PATH = "old-swedish-dictionary.json"


class DictionaryEntry(NamedTuple):
    headword: str
    part_of_speech: str
    grammatical_aspect: str
    definitions: list[str]
    alternative_forms: list[str]


def get_dictionary() -> Tuple[DictionaryEntry, ...]:
    raw_data = reader.read_json(DICTIONARY_PATH)

    return tuple(
        DictionaryEntry(
            raw_entry["a"],
            raw_entry["b"],
            raw_entry["c"],
            raw_entry["d"],
            raw_entry["e"],
        )
        for raw_entry in raw_data
    )
