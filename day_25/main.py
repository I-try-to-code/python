#
# import pandas
# data= pandas.read_csv("weather-data.csv")
# print(data[data.temp == data["temp"].max()])
import pandas
data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250524.csv")
grey_ct= len(data[data["Primary Fur Color"]=="Gray"])
black_ct= len(data[data["Primary Fur Color"]=="Black"])
cinammon_ct= len(data[data["Primary Fur Color"]=="Cinnamon"])
print(grey_ct)
print(black_ct)
print(cinammon_ct)

