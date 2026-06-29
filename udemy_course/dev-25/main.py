# We can read the file and get the lines of the file as a list of strings.
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

# We can use the csv module to read the file and get the data as a list of lists.
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

print(type(data))  # Print the type of the data object, which is a DataFrame.
print(data)

print(type(data["temp"]))  # Print the type of the "temp" column, which is a Series.
print(data["temp"])

data_dict = data.to_dict()  # Convert the DataFrame to a dictionary.
print(data_dict)

data_list = data["temp"].to_list()  # Convert the "temp" column to a list.
print(data_list)

average_temp = sum(data_list) / len(
    data_list
)  # Calculate the average temperature using sum and len functions.
print(average_temp)

print(
    data["temp"].mean()
)  # Calculate the average temperature using the mean method of the Series.

print(
    data["temp"].max()
)  # Calculate the maximum temperature using the max method of the Series.

print(data.condition)  # Another way to access the "condition" column of the DataFrame.
print(
    data["condition"]
)  # Yet another way to access the "condition" column of the DataFrame.

# To get a row of data, we can use the loc method of the DataFrame. We can pass the index of the row we want to get as an argument to the loc method.
print(data[data.day == "Monday"])  # Get the row of data where the day is Monday

print(
    data[data.temp == data.temp.max()]
)  # Get the row of data where the temperature is the maximum temperature.

monday = data[data.day == "Monday"]  # Get the row of data where the day is Monday
print(monday.condition)  # Get the condition of the day where the day is Monday.

tmp = (monday.temp * 9) / 5 + 32  # Convert the temperature from Celsius to Fahrenheit.
print(tmp)  # Print the temperature in Fahrenheit.

# Create a DataFrame from scratch using a dictionary. The keys of the dictionary are the column names and the values are the data for each column.
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)  # Create a DataFrame from the dictionary.
print(data)  # Print the DataFrame.

data.to_csv("new_data.csv")  # Save the DataFrame to a CSV file.
