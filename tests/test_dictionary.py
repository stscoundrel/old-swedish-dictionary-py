from src.old_swedish_dictionary.dictionary import DictionaryEntry, get_dictionary


def test_dictionary_has_correct_length() -> None:
    result = get_dictionary()
    assert len(result) == 41744


def test_dictionary_headwords_are_not_empty() -> None:
    assert all(len(entry.headword) > 0 for entry in get_dictionary())


def test_dictionary_has_expected_content() -> None:
    result = get_dictionary()

    expected_100 = DictionaryEntry(
        headword="af bränna",
        part_of_speech="vb",
        grammatical_aspect="v.",
        definitions=[
            "afbränna, genom eld förstöra. hans trähws the af brendhe  RK 2: 2757 . ib 1511. halff stadhen är affbrändh  BSH 5: 132 (  1506) . Jfr bränna af."
        ],
        alternative_forms=[],
    )
    expected_1000 = DictionaryEntry(
        headword="annat thera",
        part_of_speech="kn",
        grammatical_aspect="konj.",
        definitions=[
            " (eg. n. af annar i förening med gen. pl. af pron. thän) antingen. annat thera . . . älla, antingen . . . eller. annat thera skal jach felle thegh dödhan eller tu mik  Di 218 .  &quot; maa han i noghraa mattho wara annath thera gwdh eller man Lg 3: 108. &quot;"
        ],
        alternative_forms=[],
    )
    expected_5000 = DictionaryEntry(
        headword="diost",
        part_of_speech="nn",
        grammatical_aspect="",
        definitions=[
            "ridderlig tvekamp till häst. vid hvilken de stridande med lansarne angrepo hvarandra. Jfr Diez, Etym. Wörterb. 1: 216; Viollet-le-Duc, Dictionnarie du nobilier francais 2: 366 f.; Schultz. Höf. Leb. 2: 107, 110 f., samt Niedner, Das deutsche Turnier s. 38 f tornäy ok dyost  Iv 1560 .  ib 1847, 1962, 4213, (Cod. B. C) 948. ij torney ij diwst äller ok ij striidh  ib 3514 .  &quot; sik manleka brukande i dyysth ällar thorney &quot; Su 176 . ther mz thenna dost for gik ok torney burdhis riddirlik  Fr 1829 .  Va 52 .  &quot; ther war dust ok behordh &quot; RK 1: 3518 . riddara oc swena the giordho ther gaman mz diost oc bobordh  Iv 46 .  &quot; mz hoff oc danz oc leek oc diost &quot; MD 190 .  &quot; viisto riddara thera leek . . . mz dust at stangana gingo sönder &quot; RK 1: 1100 .  ib 1104 .  &quot; diwst at ridha &quot; Al 454 .  Fr 1671, 1719 .  RK 2: 196 .  Lg 3: 64 . rida i döst  Di 17 . ränna diost  Al 3865 .  ib 4751 . öfde ther dyst  RK 2: 5177 .  &quot; bruka . . . dwst ällar spärbräkningh &quot; Lg 3: 66 . - envig? som androm biwdher diwsth  SGGK 106 ."
        ],
        alternative_forms=[
            "dyost Iv 1560 . ",
            "diwst ib 3514, 4213 ;  Fr 1671 ;  Al 454 . ",
            "diwsth SGGK 106 . ",
            "dyst Iv 1847, (Cod. B) 948;  RK 2: 5177 ;  Va 52 . ",
            "dyysth Su 176 . ",
            "döst Di 17 . ",
            "dösth RK 2: 196 . ",
            "dost Fr 1719, 1829 . ",
            "dust RK 1: 1100, 1103, 3518 . ",
            "dwst Lg 3: 66 . ",
            "dwsth ib 64), ",
        ],
    )
    expected_10000 = DictionaryEntry(
        headword="gangilse",
        part_of_speech="nn",
        grammatical_aspect="",
        definitions=[
            " ? Se Sdw 2: 1226. - Jfr fore-, fram-, ivir-, mote-, um-, vidher-gangilse."
        ],
        alternative_forms=[],
    )
    expected_20000 = DictionaryEntry(
        headword="löna",
        part_of_speech="vb",
        grammatical_aspect="v.",
        definitions=[
            "löna, vedergälla. &quot; med personens dat. och ack. betecknande det för hvilket lön gifves. minom och ack. betecknande det för hvilket lön gifves. minom winom lönir iak lydhno oc älskogha mz miskund &quot; MB 1: 332 . hånom hans gif löna  KS 70 (112, 77) . gudh löne henne sin stora kärlek  Lg 807 .  KL 296 . han honom thz ille lönte  RK 2: 3459 . - pass. thz kan thöm aldrigh vardha lönt  Iv 4959 . - med personens dat. och ack. betecknande det som gifves ss lön. honum löna synda giäl  Al 2329 . - med personens dat. them löne  RK 2: 3216 .  &quot; löna wäl jlum &quot; Bil 104 .  &quot; iak lönir hwariom enom äptir sinne forskullan &quot; Bir 1: 381 .  MB 2: 369 .  &quot; om honum skwlde saa wordhe lönth for hans langlige . . . trotieniste &quot; BSH 4: 220 ( 1497) . - löna, aflöna. them som ey löna sino ärfuodhis folke rättelica  MP 2: 111 .  &quot; löne . . . af thy sama sinom piltom oc tiänarom &quot; Bir 5: 115 .  ib 116 .  &quot; sinom soldenärom skulu the ey vara pliktoghe antiggia harnisk. kost äller fordenskap til land ällir watn. ey oc gull äller päninga til them at löna &quot; MB 2: 242 .  ib 243 . - betala. badh löna sik  Bo 14 . - belöna. war gudh ther badhe lönar wälgerninga ok plicta synde  Bil 458 . "
        ],
        alternative_forms=[
            "lönar Bil 458 . ",
            "lönir MB 1: 332,  Bir 1: 381 . ",
            "löne: atir löne  ib 40 ; ",
            "atirlöne ib 2: 89 . ",
            "lönther: lönth BSH 4: 220 ( 1497)),",
            "löna i gen , ",
        ],
    )
    expected_40000 = DictionaryEntry(
        headword="välrotadher",
        part_of_speech="",
        grammatical_aspect="",
        definitions=["väl rotad. välrodat trä  Bir 3: 61 ."],
        alternative_forms=["-rod- )"],
    )

    assert result[100] == expected_100
    assert result[1000] == expected_1000
    assert result[5000] == expected_5000
    assert result[10000] == expected_10000
    assert result[20000] == expected_20000
    assert result[40000] == expected_40000
