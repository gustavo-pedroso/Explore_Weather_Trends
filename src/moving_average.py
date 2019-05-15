from pathlib import Path
import os
import pandas as pd

base_path = os.path.dirname(os.path.abspath(Path(__file__).parent))

with open(base_path + '/data/moving-average-exercise.csv') as file:
    df = pd.read_csv(file)

df['Sales'] = df['Sales'].apply(lambda x: int(x.replace(',', '')))
df['7d_ma'] = df['Sales'].rolling(window=7, min_periods=0).mean()
df['14d_ma'] =df['Sales'].rolling(window=14, min_periods=0).mean()

print(int(df[df['Date'] == '1/11/2009']['7d_ma'].iloc[0]))
print(int(df[df['Date'] == '3/19/2009']['14d_ma'].iloc[0]))
