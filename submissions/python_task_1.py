import pandas as pd
import numpy as np

dataset1='datasets/dataset-1.csv'
df1=pd.read_csv(dataset1)


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values,
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """

    # matrix=pd.crosstab(df['id_1'], columns = df['id_2'], values = df['car'], aggfunc = 'first').fillna(0)
    matrix=df.pivot(index = 'id_1', columns = 'id_2',values='car').fillna(0)
    return matrix

def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    values=['low','medium','high']
    conditions=[(df['car']<=15),
                (df['car']>15) & (df['car']<=25),
                (df['car']>25)]

    df['car_type']=np.select(conditions,values)

    return dict(df['car_type'].value_counts())


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    tmean=2*df['bus'].mean()
    out=df[df['bus']>tmean].index.values

    return list(sorted(out))



def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    routes=df['route'].unique()
    mask=[df[df['route']==i]['truck'].mean()>7 for i in routes]

    return list(sorted(routes[np.array(mask)]))

def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """

    out=matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    out=out.round(1)

    return out


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """

    return pd.Series()
