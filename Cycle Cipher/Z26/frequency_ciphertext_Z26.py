import math
import pandas as pd
import numpy as np
import scipy as stats

import matplotlib.pyplot as plt
import seaborn as sns

import sys

file_path=sys.argv[1]
try:
    with open(file_path, "rb") as input_file:
        g = input_file.read()
        b = bytearray(g)
    input_file.close()

    Z=26

    #Create frequency array
    frequency=[0]*Z
    for byte in b:
        frequency[byte-65]+=1

    #Set up x axis
    x_axis_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x_axis=[i for i in x_axis_string]

    #Make the plot
    sns.barplot(x = x_axis, y=frequency)
    plt.title("The histogram of character in the input text")
    plt.show()

except FileNotFoundError:
    print("File not found")