#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

#Create a function to read teh data file
def read_data(filename,delimiter=',',starting_row=0):
    """This function reads data from a specified filename.
    The specified filename should point to a .csv file."""
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=',')

    # Select the data range we are interested in, convert it into a new array, full of numbers
    isotope_data = np.array(all_data[2:,:], dtype=float)
    return isotope_data

def process_data (isotope_data):
    """Given some input isotope data this function converts the first column to corrected Carbon and appends
    a new column with that data."""
    #Compute a new column from Carbon to Corrected Carbon
    isotope_carbon = isotope_data[:,0,None] + 1.3

    # Append this new column to the existing isotope_data array
    processed_isotope_data = np.append(isotope_data, isotope_carbon,1)
    return processed_isotope_data

def plot_data(processed_isotope_data, plot_isotope_figure):
    """Given some input isotope data and a file name this function
    plots the third column of the input data into a file with
    the name plot_filename."""

    # Create a figure of the processed data
    plt.style.use('seaborn-whitegrid')
    isotope_figure = plt.figure()
    isotope_plot = plt.scatter (processed_isotope_data[:,0], processed_isotope_data[:,2])
    plt.xlabel("Carbon")
    plt.ylabel("Oxygen")
    plt.title('Stable Isotope Analysis')
    plt.show(block=True)
    isotope_figure.savefig(plot_isotope_figure)

def convert_data(input_file, json_filename):
    all_data = pd.read_csv(input_file, header=4)
    all_data.info()
    all_data.to_json(json_filename) 

def plot() :    
    input_file = "stable_isotope_data_assignment2.csv"
    plot_file = 'stable-isotopes.pdf'
    json_output_file = "data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    input_file = os.path.join(data_directory,input_file)
    plot_file = os.path.join(results_directory,plot_file)
    json_filename = os.path.join(results_directory,json_output_file)

    isotope_data = read_data(input_file, starting_row=0)
    processed_temperature_data = process_data(isotope_data)
    plot_data(processed_temperature_data, plot_file)
    convert_data(input_file,json_filename)

if __name__ == "__main__":
    print(sys.argv)
    plot()