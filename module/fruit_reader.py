import csv

from module.models import *


# return Fruit data from .csv file
def read_data(file_name):
    result = []
    with open(file_name) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            result.append(row)
    return result


# format data, return list of Fruit objects
def extract_data(data):
    result = []
    for item in data:
        if item[0] == "":
            break
        fruit = Fruit(item[0], item[1], Seed(item[2:5]), item[5])
        result.append(fruit)

    return result


def read_fruit_list(name):
    data_list = read_data(name)
    return extract_data(data_list)


if __name__ == '__main__':
    for i in read_fruit_list("fruit.csv"):
        print(i)
