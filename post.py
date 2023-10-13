#!/usr/bin/env python

# import the packages

import numpy as np
import os
import re
import subprocess
import math

# define the species to refer source directories

species="CO2_Ar"

# define the pressure and temperature range

pressure = np.arange(35, 125, 10)
Temperature = 253

# additional sorting and add values out of range to the array
#pressure = np.array([65])
#pressure = np.append(pressure, additional_pressure)
#pressure =sorted(pressure)

# define the statistics parameter

block=5
sim=2

# Create the direcotries to store the thermophysical properties if already exist remove and create a new one 

bash_code = f'''
if [ -d "VLE_{species}" ]; then
    rm -r "VLE_{species}"
fi
mkdir "VLE_{species}"
'''

subprocess.call(bash_code, shell=True)

# Function to calculate the average of the elements in the array

def avg(array):

  sum_of_array = sum(array)
  number_of_elements = len(array)
  average = sum_of_array / number_of_elements
  return average

# Function ot calculate the variance of the elements in the array

def sd(array):
    mean = sum(array) / len(array)
    squared_mean = mean ** 2
    squared_elements = []
    for element in array:
        squared_element = element ** 2
        squared_elements.append(squared_element)
    variance = sum(squared_elements) / len(array)
    standard_deviation = math.sqrt(variance - squared_mean)
    return standard_deviation

# start the looping for the temperatures

for P in pressure:

    density_l_b = []
    density_g_b = []

    for i in range(1, block + 1):

        density_l_s = []
        density_g_s = []
        

        for j in range(1, sim + 1):

            fold_T  = f"{species}/T_{Temperature}_P_{P}/block_{i}/sim_{j}"
            
            try:
                os.chdir(fold_T)
                grep_process_C1 = subprocess.Popen(["grep", "-A", "1", "Mole fractions", "sim.log"], stdout=subprocess.PIPE)
                tail_process_C1 = subprocess.Popen(["tail", "-1"], stdin=grep_process_C1.stdout, stdout=subprocess.PIPE)
                tail_process_C1, _ = tail_process_C1.communicate()
                C1 = tail_process_C1.decode()
                C1_elements =C1.split()

                if len(C1_elements) >= 3:
                    L_C1 = float(C1.split()[1])
                    G_C1 = float(C1.split()[2])
                    print(L_C1)
                    # Append the greped values from the sim folder

                    density_l_s.append(L_C1)
                    density_g_s.append(G_C1)

                else:
                    print(f"simulation error in {fold_T}")

            except FileNotFoundError:

                print(f"sim.log not found in {fold_T}")

            finally:
                os.chdir("../../../..")

        # perform avarage of the set array

        avgs_density_l = avg(density_l_s)
        avgs_density_g = avg(density_g_s)  

        # Append the block averaged from the block folder

        density_l_b.append(avgs_density_l)
        density_g_b.append(avgs_density_g)
    
    # perform average of the block array   

    avgb_density_l = avg(density_l_b)
    avgb_density_g = avg(density_g_b)

    # Round the averaged values

    avgb_density_l = round(avgb_density_l, 4)
    avgb_density_g = round(avgb_density_g, 4)

    # Find the standard deviation of the block array

    sd_density_l = sd(density_l_b)
    sd_density_g = sd(density_g_b)

    # Round the standard deviation values

    sd_density_l = round(sd_density_l, 6)
    sd_density_g = round(sd_density_g, 6)

    # wiritng the calclated properties value to the file in the TP directory

    file_properties = f"VLE_{species}/VLE_{species}.dat"
    file_sd         = f"VLE_{species}/SD_VLE_{species}.dat"

    if not os.path.isfile(file_properties):  # Check if the file exists
        with open(file_properties, "w") as file:  # Create new file
            file.write("Temperature density_L density_g\n")  # Write the header
            file.write(f"{P} {avgb_density_l} {avgb_density_g}\n") # Write the data
    else:
        with open(file_properties, "a") as file:  # Append to existing file
            file.write(f"{P} {avgb_density_l} {avgb_density_g}\n") # Write the data

        # wiritng the standard deviation value to the file in the TP directory
                
    if not os.path.isfile(file_sd):  # Check if the file exists
        with open(file_sd, "w") as file:  # Create new file
            file.write("Temperature SD_density_L SD_density_g\n")  # Write the header
            file.write(f"{P} {sd_density_l} {sd_density_g}\n") #append the data
    else:
        with open(file_sd, "a") as file:  # Append to existing file
            file.write(f"{P} {sd_density_l} {sd_density_g}\n") #append the data        
# end of program