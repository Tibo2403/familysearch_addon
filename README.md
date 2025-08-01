# FamilySearch Addon

This project contains experimental utilities for working with genealogical data. A small example module lives in `src/familysearch_addon` and demonstrates converting a simple JSON birth record to GEDCOM.

## Quickstart

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Run the sample conversion script:

```bash
python - <<'PY'
from familysearch_addon import birth_record_json_to_gedcom

record = {
    "name": "John Doe",
    "gender": "M",
    "birth_date": "1 JAN 1900",
    "birth_place": "Somewhere"
}
print(birth_record_json_to_gedcom(record))
PY
```

This should output a basic GEDCOM representation of the record.

