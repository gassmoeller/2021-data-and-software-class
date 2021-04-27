import sys, os
import numpy as np
import pandas as pd

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

import src.plotting as plotting

def test_plot():
    assert(plotting.plot() == None)

def test_process_data():
    input_data = np.array([[-3,1.0288],[1,1.0288]])
    function_output = plotting.process_data(input_data)
    expected_output = np.array([[-3,1.0288,-1.7],[1,1.0288,2.3]])
    
    assert(np.all(function_output == expected_output))

def test_read_data():
    input_file = "stable_isotope_data_assignment2.csv"
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    input_filename = os.path.join(data_directory,input_file)
    isotope_data = plotting.read_data(input_filename, starting_row=3)

    assert(isotope_data.shape == (57,2))
    assert(isotope_data[0,1] == -1.8)

def test_plot_data():
    plot_file = "test_plot_data.pdf"
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))
    plot_filename = os.path.join(results_directory,plot_file)

    input_data = np.array([[-3,1.0288,1.5],[1,1.0288,1.5]])

    if os.path.exists(plot_filename):
        os.remove(plot_filename)

    plotting.plot_data(input_data, plot_filename)

    assert (os.path.exists(plot_filename))

def test_convert_data():
    input_file = "stable_isotope_data_assignment2.csv"
    json_output_file = "data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    input_filename = os.path.join(data_directory,input_file)
    json_filename = os.path.join(results_directory,json_output_file)

    plotting.convert_data(input_filename, json_filename)

    input_data = pd.read_csv(input_filename, header=2)
    output_data = pd.read_json(json_filename)

    assert (True)