"""Utilities for converting genealogical data formats."""

from typing import Dict


def birth_record_json_to_gedcom(birth_record: Dict[str, str]) -> str:
    """Convert a simple JSON birth record to a GEDCOM string.

    Parameters
    ----------
    birth_record: Dict[str, str]
        Dictionary containing keys such as ``name``, ``gender``,
        ``birth_date`` and ``birth_place``.

    Returns
    -------
    str
        GEDCOM formatted representation of the record.
    """
    if not birth_record:
        return ""

    lines = [
        "0 @I1@ INDI",
        f"1 NAME {birth_record.get('name', 'Unknown')}",
        f"1 SEX {birth_record.get('gender', '')}",
        "1 BIRT",
        f"2 DATE {birth_record.get('birth_date', '')}",
        f"2 PLAC {birth_record.get('birth_place', '')}",
    ]
    return "\n".join(lines)

