# PathFinder

PathFinder is a generic class that shows all the possible paths from a source to its destination.

To use it, its necessary to feed all the existent connections between the tables as a dictionary of sets.

For the Postgres database, there is a query in this repo, retrieved from *https://dataedo.com/kb/query/postgresql/list-of-foreign-keys-with-columns* that list all relations between tables.

Example:

```python
import pandas as pd


df = pd.read_csv('data.csv') 
relations = defaultdict(set)

for index in df.index:
  relations[df.iloc[index, 2]].add(df.iloc[index, 0])
  relations[df.iloc[index, 0]].add(df.iloc[index, 2])

teste = PathFinder(relations)
teste.print_all_paths('table1', 'table2')
```

