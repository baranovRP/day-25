import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data)
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

squirrels_color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrels_color_dict)
df.to_csv("squirrel_count.csv")

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print("Average temp =", data["temp"].mean())
# print("Max temp =", data.temp.max())
# print(data[data.day == "Monday"])
#
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # Create dataframe
# students_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# students_data = pandas.DataFrame(students_dict)
# students_data.to_csv("new_data.csv", mode="w")


# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)


# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             print(temperature)
#             temperatures.append(temperature)
