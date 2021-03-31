import sys, os
import numpy as np

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    "../"))

import src.plotting as plotting

def test_plot():
    assert(plotting.plot() == None)

def test_process_data():
    input_data = np.array([[0,32],[1,212]])

    function_output = plotting.process_data(input_data)
    expected_output = np.array([[0,32,273],[1,212,373]])
    
    assert(np.all(function_output == expected_output))