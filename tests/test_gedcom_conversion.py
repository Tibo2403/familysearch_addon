from pathlib import Path
import sys

# Ensure the src package is on the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from familysearch_addon import birth_record_json_to_gedcom


def test_complete_record_yields_formatted_lines():
    record = {
        "name": "John Doe",
        "gender": "M",
        "birth_date": "1 JAN 1990",
        "birth_place": "Somewhere",
    }
    expected = (
        "0 @I1@ INDI\n"
        "1 NAME John Doe\n"
        "1 SEX M\n"
        "1 BIRT\n"
        "2 DATE 1 JAN 1990\n"
        "2 PLAC Somewhere"
    )
    assert birth_record_json_to_gedcom(record) == expected


def test_missing_fields_handled_gracefully():
    record = {"gender": "F"}
    expected = (
        "0 @I1@ INDI\n"
        "1 NAME Unknown\n"
        "1 SEX F\n"
        "1 BIRT\n"
        "2 DATE \n"
        "2 PLAC "
    )
    assert birth_record_json_to_gedcom(record) == expected


def test_empty_dict_returns_empty_string():
    assert birth_record_json_to_gedcom({}) == ""
