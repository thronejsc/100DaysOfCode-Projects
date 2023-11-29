# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# without pandas
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

# with pandas

import pandas

# table = pandas.read_csv("../weather_data.csv")
# print(table)
# print(table["temp"])

# convert data to dict
# data_dict = table.to_dict()
# print(data_dict)

# convert data to list
# data_list = table["temp"].to_list()
# print(data_list)

# ave = table["temp"].max()

# print the row with the highest temp
# print(table[table.temp == table.temp.max()])

# monday = table[table.day == "Monday"]
# print(monday.temp[1])
# fahrenheit = monday.temp[0] * 1.8 + 32
# print(fahrenheit)

# create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# create a new csv file
# data.to_csv("students.csv")


# TODO: goal to create a dataframe from squirrel data file that consists of fur color (grey, red, black) and its count
table = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231128.csv')

fur_color = table["Primary Fur Color"].to_list()

total_grey = len(table[table["Primary Fur Color"] == "Gray"])
total_red = len(table[table["Primary Fur Color"] == "Cinnamon"])
total_black = len(table[table["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [total_grey, total_red, total_black]
}

data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_count.csv")




