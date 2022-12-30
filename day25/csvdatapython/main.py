import csv
import pandas

# Using CSV reader
with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = [int(row[1]) for row in data if row[1] != "temp"]

# Using pandas
data_panda = pandas.read_csv("weather_data.csv")
print(data_panda["temp"])

# Data to dictionary
data_dict = data_panda.to_dict()
print(data_dict)

# Pandas to list temps in list
temp_list = data_panda["temp"].to_list()
print(temp_list)

# Work out avg temp for column of temps
avg_temp = data_panda["temp"].mean()
print(avg_temp)

# Get Max Value Temp using Pandas
max_temp = data_panda["temp"].max()
print(max_temp)

# Pandas to get columns
condition = data_panda.condition
print(condition)

# Pandas get desired row
monday = data_panda[data_panda.day == "Monday"]
print(monday)

# Row of data with the highest temp of the week
highest_temp_row = data_panda[data_panda.temp == max_temp]
print(highest_temp_row)

# Get Monday's temp in F
monday_temp_f = (9/5) * int(monday.temp) + 32
print(monday_temp_f)

# Create dataframe from scratch in Pandas
data_students = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
p_data_students = pandas.DataFrame(data_students)
print(p_data_students)
p_data_students.to_csv("student_scores.csv")
