import pandas as pd

dataset3="datasets/dataset-3.csv"
df3=pd.read_csv(dataset3)

def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # matrix=pd.crosstab(df['id_end'], columns = df['id_start'], values = df['distance'], aggfunc = 'first').fillna(0)
    # df['cum_distance']=df['distance'].cumsum()
    # print(df.head())
    # matrix=df.pivot(index = 'id_end', columns = 'id_start',values='cum_distance').fillna(0)
    # matrix=pd.crosstab(df['id_end'], columns = df['id_start'], values = df['distance'], aggfunc = 'sum').fillna(0)
    return df

def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here

    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    reference_df = df[df['id_start'] == reference_id]

    avg = reference_df['distance'].mean()

    lower,upper = 0.9 * avg, 1.1 * avg

    out = df[(df['distance'] >= lower) & (df['distance'] <= upper)]

    out = sorted(out['id_start'].unique())

    return out

def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    outdf=df.copy()
    outdf['moto']=outdf['distance']*0.8
    outdf['car']=outdf['distance']*1.2
    outdf['rv']=outdf['distance']*1.5
    outdf['bus']=outdf['distance']*2.2
    outdf['truck']=outdf['distance']*3.6
    del outdf['distance']

    return outdf
calculate_toll_rate(df3)

def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """

    return df
