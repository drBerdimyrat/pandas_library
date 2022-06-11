# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# data["temp"].mean()
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# fahrenheit = (int(monday.temp) * 9/5) + 32
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

new_data = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

converted_data = pandas.DataFrame(new_data)
converted_data.to_csv("squirrels_data.csv")

