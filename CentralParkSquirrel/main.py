import pandas as pd
# Reading data from csv file
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


p_fur_color = data["Primary Fur Color"]
val_counts = p_fur_color.value_counts()
print(val_counts)
counts = []
for count in val_counts:
    counts.append(count)

# Creating csv file according to squirrels' fur color.
data_dict = {"Fur Color":["gray","red","black"], "Count": counts}
data = pd.DataFrame(data_dict)
data.to_csv("squirrel_count")

# grey --> 2473
# red --> 392
# black --> 103

