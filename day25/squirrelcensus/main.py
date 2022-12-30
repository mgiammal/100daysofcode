import pandas

# Create CSV called squirrel count
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_color_counts = squirrel_data["Primary Fur Color"].value_counts().reset_index()
primary_color_counts.columns = ["Fur Color", "Count"]

primary_color_counts.to_csv("squirrel_count.csv")
