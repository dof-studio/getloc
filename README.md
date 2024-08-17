# Repo 'getLoc'
An common API to get the location of an index, supporting Pandas or Polars dataframes.

# API
```python
def get_loc(
    df: Any,
    index_value: Any,
    *,
    column: Any = None
) -> (int | slice | np_ndarray_bool | Any)
```

# Params
df : Pandas or Polars dataframe

index_value : Index value to search for

column : Column to search in (default: None, when using a Polars dataframe, specify it)

# Returns
Location of the index value in the dataframe (integer)

# Example
```python
df = pd.DataFrame(
    {'A': [0, 1, 2, 3, 4, 5], 'B':['a','b','c','d','e','f']},
    index = ['adam', 'bob', 'charlie', 'david', 'edward', 'frank']
)
print("Pandas DataFrame: ", get_loc(df, 'charlie')) # Returns 2
df_pl = pl.from_pandas(df.reset_index(), include_index=True)
print("Polars DataFrame: ", get_loc(df_pl, 'charlie', column = 'index')) # Returns 2
```

# Author
Nathmath from DOF Studio. On Aug 17, 2024.
Nathmath is/was a Master's student of NYU MSFE program.
