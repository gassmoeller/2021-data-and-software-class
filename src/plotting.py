#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

# Create an array (a multi-dimensional table) out of our data file, full of text
all_data = np.genfromtxt("data/110-tavg-12-12-1950-2020.csv", delimiter=',',skip_header=5)

# Select the data range we are interested in, convert it into a new array, full of numbers
temperature_data = np.array(all_data[5:,:], dtype=float)

    # Append this new column to the existing temperature_data array
    processed_temperature_data = np.append(temperature_data, temperature_kelvin,1)
    return processed_temperature_data

# Append this new column to the existing temperature_data array
processed_temperature_data = np.append(temperature_data, temperature_kelvin,1)
print (processed_temperature_data)

# Create a figure of the processed data
temperature_figure = plt.figure()
temperature_plot = plt.bar (processed_temperature_data[:,0],processed_temperature_data[:,2], width=30, color='blue')
plt.show(block=True)
temperature_figure.savefig('results/temperature-over-time.pdf')

def convert_data(filename, output_filename):
    all_data = pd.read_csv(filename, index_col='Date', header=4)
    all_data.info()
    all_data.to_json(output_filename)

print("hello world", all_data.loc['195012':'197512','Value'])

    input_filename = os.path.join(data_directory,input_file)
    plot_filename = os.path.join(results_directory,plot_file)
    json_filename = os.path.join(results_directory,json_output_file)

    temperature_data = read_data(input_filename, starting_row=5)
    processed_temperature_data = process_data(temperature_data)
    plot_data(processed_temperature_data, plot_filename)
    convert_data(input_filename, json_filename)

if __name__ == "__main__":
    print(sys.argv)
    plot()