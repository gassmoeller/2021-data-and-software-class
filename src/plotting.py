#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create a function to read the data file
def read_data(filename,delimiter=',',starting_row=0):
    """This function reads data from a specified filename. 
    The specified filename should point to a .csv file."""
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=delimiter,skip_header=5)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    temperature_data = np.array(all_data[starting_row:,:], dtype=float)
    return temperature_data

def write_data_to_json(infile,index_col,header,outfile):
    """Reads data from a .csv file 'infile' using pandas with index column 'index_col' 
    and start header 'header'. Then writes data in memory to a JSON file."""
    # Read 'infile', print DataFrame info
    all_data = pd.read_csv(infile,index_col,header=header)
    all_data.info()

    # Write to JSON format
    all_data.to_json(outfile)

temperature_data = read_data("data/110-tavg-12-12-1950-2020.csv", starting_row=5)
write_data_to_json("data/110-tavg-12-12-1950-2020.csv",'Date',4,"results/data_output.json")

# Compute a new column by multiplying column number 1 to Kelvin
temperature_kelvin = (temperature_data[:,1,None] - 32) * 5/9 + 273

# Append this new column to the existing temperature_data array
processed_temperature_data = np.append(temperature_data, temperature_kelvin,1)

# Create a figure of the processed data
temperature_figure = plt.figure()
temperature_plot = plt.bar (processed_temperature_data[:,0],processed_temperature_data[:,2], width=35, color='blue')

plt.show(block=True)
temperature_figure.savefig('results/temperature-over-time.pdf')