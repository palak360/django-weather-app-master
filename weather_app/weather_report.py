import pandas as pd 

df = pd.read_csv('weather.csv')


a=df['Temperature'].max()
print("Max Temperature in tenths of a degree Celsius :", a%10)
b=df['Temperature'].min()
print("Minimum temperature in tenths of a degree Celsius: ",b%10)
c=df['precipitation'].sum()
print(c, "in tenths of a millimeter")