import pandas
from collections import Counter

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
PriFur= data["Primary Fur Color"]
temp_list = PriFur.to_list()
black = 0
grey = 0
white = 0

counts = Counter(temp_list)

black = counts["Black"]
grey = counts["Grey"]
cin = counts["Cinnamon"]

data_dict = {
    "Primary Colour": ["Black", "Grey", "Cinnamon"],
    "scores":[
        counts.get("Black", 0),
        counts.get("Grey", 0),
        counts.get("Cinnamon", 0)]}

path = pandas.DataFrame(data_dict)
path.to_csv("New_Data.csv")










