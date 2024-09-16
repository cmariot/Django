# Fixtures

## Dump database in a fixture file:
``` bash
python3 manage.py dumpdata --indent 4 > fixtures/data.json
```

## Load the fixture file in the database
``` bash
 python3 manage.py loaddata ./fixtures/data.json
 ```
