import json
import matplotlib.pyplot as plt
import pandas as pd


#with open('C:\\Users\\thoga\\OneDrive\\Desktop\\VS code Workspaces\\Grade Scraper\\tutorial\\tutorial\\data.json', 'r') as file:
#        plot_data = json.load(file)


def plot_data_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract the relevant data
    average_grades = [item['average_grade'] for item in data]
    a_ranges = [float(item['a_range']) if item['a_range'] else None for item in data]
    f_ranges = [float(item['f_range']) if item['f_range'] else None for item in data]

    # Plotting the data
    plt.scatter(average_grades, a_ranges, label='A Range', marker='o', color ='green')
    plt.scatter(average_grades, f_ranges, label='F Range', marker ='o', color ='red')
    plt.xlabel('Average Grade')
    plt.ylabel('# Grades in Range')
    plt.title('Grade Ranges for Different Average Grades')
    plt.legend()
    plt.show()

plot_data_from_json('C:\\Users\\thoga\\OneDrive\\Desktop\\VS code Workspaces\\Grade Scraper\\tutorial\\tutorial\\data.json')



