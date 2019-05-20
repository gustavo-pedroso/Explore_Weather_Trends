from pathlib import Path
import os
import pandas as pd
import matplotlib.pyplot as plt

base_path = os.path.dirname(os.path.abspath(Path(__file__).parent))

with open(base_path + '/data/temperature_guarulhos.csv') as file: # open guarulhos temperature dataset
    df_city = pd.read_csv(file)

with open(base_path + '/data/temperature_world.csv') as file: # open world temperature dataset
    df_world = pd.read_csv(file)

df_city['year'] = df_city['year'].apply(lambda x: int(x)) # convert data type to int
df_world['year'] = df_world['year'].apply(lambda x: int(x)) # convert data type to int

df_city['avg_temp'] = df_city['avg_temp'].apply(lambda x: float(x)) # convert data type to float
df_world['avg_temp'] = df_world['avg_temp'].apply(lambda x: float(x)) # convert data type to float

df_city['10y_ma'] = df_city['avg_temp'].rolling(window=10, min_periods=0).mean() # use built-in rolling method to create column moving average
df_world['10y_ma'] = df_world['avg_temp'].rolling(window=10, min_periods=0).mean() # use built-in rolling method to create column moving average

start_year = max(df_world['year'].min(), df_city['year'].min()) # get start interval year
end_year = min(df_world['year'].max(), df_city['year'].max()) # get end interval year

df_city = df_city[(df_city['year'] >= start_year) & (df_city['year'] <= end_year)] # filter to get data within interval
df_world = df_world[(df_world['year'] >= start_year) & (df_world['year'] <= end_year)] # filter to get data within interval

print(df_world.corrwith(df_city, axis=0)) # print correlation between coluns on both dataframes


# create plot and display 10 year moving averages for guarulhos and world dataframes.
ax = plt.subplot()
ax.set_title('Guarulhos x World 10 year Temperature MA')
ax.set_ylabel('Temperature')
df_world[['year', '10y_ma']].plot(x='year', y='10y_ma', label='World', grid=True, ax=ax)
df_city[['year', '10y_ma']].plot(x='year', y='10y_ma', label='Guarulhos', grid=True, ax=ax)
plt.show()
