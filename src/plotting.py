#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

# Create a function to read the data file
def read_data(filename,delimiter=',',starting_row=0):
    """This function reads data from a specified filename. 
    The specified filename should point to a .csv file."""
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=delimiter,skip_header=5)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    temperature_data = np.array(all_data[starting_row:,:], dtype=float)
    return temperature_data

def figure_create(data,results_filename,input_filename,results_plot):
    """Processes a data file with the processed_temperature_data structure and plots the first and third columns
    and also saves the figure as pdf and the datas as a .json file"""
    temperature_figure = plt.figure()
    temperature_plot = plt.bar (data[:,0],data[:,2], width=35, color='blue')


    temperature_figure.savefig(results_plot)

    all_data = pd.read_csv(input_filename, index_col='Date', header=4)
    all_data.info()
    all_data.to_json(results_filename)
    plt.show()


    json_data = pd.read_json(results_filename)
    json_data.info()

    temperature_plot = plt.bar (all_data.loc[:,"Value"], height=all_data.loc[:,"Value"], width=30)
    plt.show()

def initialize(inputs="110-tavg-12-12-1950-2020.csv"):
    input_file = inputs
    plot_file = "temperature-over-time.pdf"
    json_output_file="data_output.json"


    data_directory=os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory=os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    input_filename= os.path.join(data_directory,input_file)
    plot_filename= os.path.join(results_directory,plot_file)
    json_filename= os.path.join(results_directory,json_output_file)

    temperature_data = read_data(input_filename, starting_row=5)

    # Compute a new column by multiplying column number 1 to Kelvin
    temperature_kelvin = (temperature_data[:,1,None] - 32) * 5/9 + 273

    # Append this new column to the existing temperature_data array
    processed_temperature_data = np.append(temperature_data, temperature_kelvin,1)

    figure_create(processed_temperature_data,json_filename,input_filename,plot_filename)


if __name__=="__main__":
    if len(sys.argv)==1:
        initialize()
    elif len(sys.argv)==2:
        initialize(inputs=sys.argv[1])
    else:
        print("too many arguments")
        




