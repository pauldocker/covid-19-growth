import pandas as pd
from operator import itemgetter
import pickle
import constants


""" Exposes df_all, a dictionary with dataframes holding all global time series data
     df_all = {
         'cases': <all global cases dataframe>,
         'deaths': <all global deaths dataframe>
     }

    Dataframe functions
    `filter(df, column, vlaue)` Generic filter
    `for_country(df, country)` Filter by country
    `for_province_state(df, province_state)` Filter by province_state
    `sum_by_date(df)` Group by date and sum case counts 
"""

renamed_columns = constants.JHU_RENAMED_COLUMNS['time_series']

def df_from_csv(file_name):
    """ Perform ETL on a Johns Hopkins COVID-19 time series file, Returning a dataframe """
    df = pd.read_csv(file_name)
    df = df.rename(columns=renamed_columns)
    date_cols = df.filter(regex=('^\d+/\d+/\d+$')).columns.array
    df = pd.melt(df, id_vars=['province_state', 'country', 'lat',
                                      'long'], value_vars=date_cols, var_name='date', value_name='cases')
    df.date = pd.to_datetime(df.date, format='%m/%d/%y')
    df['day'] = (df.date - pd.to_datetime(df.date.iloc[0])).astype('timedelta64[D]')
    df.day = df.day.apply(lambda day: int(round(day)))
    return df[['date', 'day', 'cases', 'province_state', 'country', 'lat', 'long']]

def filter(df, column, value):
    """ General purpose filter. """
    return df[df[column] == value].reset_index()

def for_country(df, country):
    """ Filter on country """
    return filter(df, 'country', country)

def for_province_state(df, province_state):
    """ Filter on province_state. us.py has its own function for this """
    return filter(df, 'province_state', province_state)

def sum_by_date(df):
    """ Return input with all rows collapsed by date and cases summed """
    return df.groupby('date').sum().reset_index()

_df_cases = df_from_csv(constants.DATA_URLS['global']['cases'])
_df_deaths = df_from_csv(constants.DATA_URLS['global']['deaths']).rename(columns={'cases': 'deaths'})

""" Dictionary containing dataframes for all global data """
df_all = {
    'cases': _df_cases,
    'deaths': _df_deaths
}

try:
    get_ipython
except:
    pickle_file = open('output/pickles/df_all.p', 'wb')
    pickle.dump(df_all, pickle_file)
    print('Updated pickle file df_all.p with global data')
