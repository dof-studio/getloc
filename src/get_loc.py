# get_loc.py
# version 0.0.1 by DOF Studio
# dev 240817

import pandas as pd
import polars as pl

def get_loc(df, index_value:any, *, column:any = None):

    '''
    Get the location of an index, for Pandas or Polars dataframes.
    Params:
        df: Pandas or Polars dataframe
        index_value: Index value to search for
        column: Column to search in (default: None, when using a Polars dataframe, specify it)
    Returns:
        Location of the index value in the dataframe (integer)
    Example:
        df = pd.DataFrame({'A': [0, 1, 2, 3, 4, 5]})
        get_loc(df, 3) # Returns 3
    '''
    
    # If index not a scalar
    try:
        if isinstance(index_value, 'str') == False:
            ivlen = len(index_value)
        else:
            ivlen = 1
    except:
        ivlen = 1
    if ivlen > 1:
        raise TypeError("Arg 'index' must be a scalar!")
    
    # Pandas
    if isinstance(df, pd.DataFrame):
        return df.index.get_loc(index_value)
    
    # Polars
    elif isinstance(df, pl.DataFrame):
        if column is None:
            raise ValueError("Arg 'column' must be specified as the column name of the index!")
        return df.with_row_index('row_number').filter(pl.col(column) == index_value).select('row_number').item()
    
    # Unsupported
    else:
        raise TypeError("Arg 'df' must be a Pandas or Polars DataFrame!")


# Example:
# Using if __name__ == "__main__"

if __name__ == "__main__":
    
    # Pandas DataFrame
    df = pd.DataFrame(
        {'A': [0, 1, 2, 3, 4, 5], 'B':['a','b','c','d','e','f']},
        index = ['adam', 'bob', 'charlie', 'david', 'edward', 'frank']
    )
    # Returns 2
    print("Pandas DataFrame: ", get_loc(df, 'charlie'))
    # Convert to Polars DataFrame
    df_pl = pl.from_pandas(df.reset_index(), include_index=True)
    # Returns 2
    print("Polars DataFrame: ", get_loc(df_pl, 'charlie', column = 'index'))
