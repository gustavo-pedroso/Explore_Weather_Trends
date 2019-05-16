from pathlib import Path
import os
import pandas as pd
import matplotlib.pyplot as plt

base_path = os.path.dirname(os.path.abspath(Path(__file__).parent))

with open(base_path + '/data/temperature_guarulhos.csv') as file:
    df_city = pd.read_csv(file)

with open(base_path + '/data/temperature_world.csv') as file:
    df_world = pd.read_csv(file)

df_city['year'] = df_city['year'].apply(lambda x: int(x))
df_world['year'] = df_world['year'].apply(lambda x: int(x))

df_city['avg_temp'] = df_city['avg_temp'].apply(lambda x: float(x))
df_world['avg_temp'] = df_world['avg_temp'].apply(lambda x: float(x))

df_city['10y_ma'] = df_city['avg_temp'].rolling(window=10, min_periods=0).mean()
df_world['10y_ma'] = df_world['avg_temp'].rolling(window=10, min_periods=0).mean()

start_year = max(df_world['year'].min(), df_city['year'].min())
end_year = min(df_world['year'].max(), df_city['year'].max())

df_city = df_city[(df_city['year'] >= start_year) & (df_city['year'] <= end_year)]
df_world = df_world[(df_world['year'] >= start_year) & (df_world['year'] <= end_year)]

print(df_world.corrwith(df_city, axis=0))



ax = plt.subplot()
ax.set_title('Guarulhos x World 10 year Temperature MA')
ax.set_ylabel('Temperature')
df_world[['year', '10y_ma']].plot(x='year', y='10y_ma', label='World', grid=True, ax=ax)
df_city[['year', '10y_ma']].plot(x='year', y='10y_ma', label='Guarulhos', grid=True, ax=ax)
plt.show()
