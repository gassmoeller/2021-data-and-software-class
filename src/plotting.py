#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

# Create an array (a multi-dimensional table) out of our data file, full of text
all_data = np.genfromtxt("stable_isotope_data_assignment2-Sheet1.csv", delimiter=',',skip_header=3)

# Select the data range we are interested in, convert it into a new array, full of numbers
isotope_data = np.array(all_data[3:,:], dtype=float)

 # Select the data range we are interested in, convert it into a new array, full of numbers
isotope_data = np.array(all_data[3:,:], dtype=float)
print(isotope_data)

# Append this new column to the existing isotope_data array
processed_isotope_data = np.append(isotope_data, isotope_data,1)
print (processed_isotope_data)

# Create a figure of the processed data
plt.style.use('seaborn-whitegrid')
isotope_figure = plt.figure()
isotope_plot = plt.scatter (processed_isotope_data[:,0], processed_isotope_data[:,2])
plt.xlabel("Carbon")
plt.ylabel("Oxygen")
plt.title('Stable Isotope Analysis')
plt.show(block=True)
isotope_figure.savefig('results/stable-isotopes.pdf')

def convert_data(filename, output_filename):
    all_data = pd.read_csv(filename, index_col='Date', header=4)
    all_data.info()
    all_data.to_json(output_filename)

    input_filename = os.path.join(data_directory,input_file)
    plot_filename = os.path.join(results_directory,plot_file)
    json_filename = os.path.join(results_directory,json_output_file)

    isotope_data = read_data(input_filename, starting_row=3)
    processed_isotope_data = process_data(isotope_data)
    plot_data(processed_isotope_data, plot_filename)
    convert_data(input_filename, json_filename)

if __name__ == "__main__":
    print(sys.argv)[1]
    plot()