from typing import Final, NamedTuple, Tuple

from . import reader

DICTIONARY_PATH: Final[str] = "old-swedish-dictionary.json"


class DictionaryEntry(NamedTuple):
    headword: str
    part_of_speech: list[str]
    grammatical_aspect: str
    information: str
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
            raw_entry["f"],
        )
        for raw_entry in raw_data
    )
