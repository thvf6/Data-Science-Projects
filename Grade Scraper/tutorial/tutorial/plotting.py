import json
import matplotlib.pyplot as plt
import pandas as pd


def plot_data_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract Data
    average_grades = [] 
    a_ranges = []
    c_ranges = []
    f_ranges = [] 
    for item in data: 
        average_grade = item['average_grade']
        if average_grade is not None: 
            try: 
                average_grades.append(float(average_grade))
                a_ranges.append(item['a_range'])
                c_ranges.append(item['c_range'])
                f_ranges.append(item['f_range'])
            except (TypeError, ValueError):
                pass

    # Convert grade ranges to floar arrays
    a_ranges = np.array(a_ranges, dtype = float)
    c_ranges = np.array(c_ranges, dtype = float)
    f_ranges = np.array(f_ranges, dtype = float)

    # Perform linear regression 
    a_x = np.array(average_grades)
    a_y = np.array(a_ranges, dtype = float)
    a_coefficients = np.polyfit(a_x, a_y, 1)
    a_approx = np.polyval(a_coefficients, a_x)

    c_x = np.array(average_grades)
    c_y = np.array(c_ranges, dtype = float)
    c_coefficients = np.polyfit(c_x, c_y, 1)
    c_approx = np.polyval(c_coefficients, a_x)

    f_x = np.array(average_grades)
    f_y = np.array(f_ranges, dtype = float)
    f_coefficients = np.polyfit(f_x, f_y, 1)
    f_approx = np.polyval(f_coefficients, f_x)

    # Plotting the data
    title = input("Please enter the course title:") 
    plt.scatter(average_grades, a_ranges, label='A Range', marker='o', color ='green')
    plt.scatter(average_grades, c_ranges, label='C Range', marker ='o', color ='yellow')
    plt.scatter(average_grades, f_ranges, label='F Range', marker ='o', color ='red')
    plt.plot(average_grades, a_approx, color = 'green', label = 'A Range Approx.')
    plt.plot(average_grades, c_approx, color = 'yellow', label = 'C Range Approx')
    plt.plot(average_grades, f_approx, color = 'red', label ='F Range Approx.' )
    plt.xlabel('Average Grade')
    plt.ylabel('# Grades in Range')
    plt.title('Grade Distr. for' +" "+ title )
    plt.legend()
    plt.show()

plot_data_from_json('file path to data.json')



