# Old Swedish Dictionary

Old Swedish Dictionary for Python. The dictionary consists of 40 000+ Old Swedish words with Swedish translations.

Based on K.F. Söderwall's Medieval Swedish Dictionary

### Install

`pip install old-swedish-dictionary`

### Usage

The project provides a getter for the whole dataset. You can use it in your script to populate your own database or otherwise use the data.

Should you want to use the data without this Python library, you might want to check [Old Swedish Dictionary Builder](https://github.com/stscoundrel/old-swedish-dictionary-builder)

```python

from old_swedish_dictionary.dictionary import get_dictionary

# Whole dictionary of +41 000 entries
dictionary = get_dictionary()

# Dictionaries return entries that consist of headword, part of speech and definition.
print(dictionary[100].headword)           # af bränna
print(dictionary[100].part_of_speech)     # vb
print(dictionary[100].grammatical_aspect) # v.
print(dictionary[100].definitions)        # ["afbränna, genom eld förstöra. hans trähws the af brendhe  [...and more]]

```

Individual words are returned in named tuple format of:

```python
# For type hint usage
from old_swedish_dictionary.dictionary import DictionaryEntry

{
    headword: str
    part_of_speech: list[str]
    grammatical_aspect: str
    information: str
    definitions: list[str]
    alternative_forms: list[str]
}
```

### About "Dictionary of Old Swedish"

_"Ordbok Öfver svenska medeltids-språket"_ dictionary was published in late 1884—1918 by K.F. Söderwall. Additional supplement to it was published in 1953—1973.

Old Swedish developed from Old East Norse, the eastern dialect of Old Norse, at the end of the Viking Age. Early Old Swedish was spoken from about 1225 until about 1375, and Late Old Swedish was spoken from about 1375 until about 1526.

The original material is licenced under [Creative Commons International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), made available by University of Gothenburg. The source code for this library is under MIT licence.

- https://spraakbanken.gu.se/en/resources/soederwall
- https://spraakbanken.gu.se/en/resources/soederwall-supp

