#!/usr/bin/env python

# import the packages
import subprocess
import math
import os
import sys
import re
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter, MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset


file_path_SIM = fr'VLE_CO2_Ar/VLE_CO2_Ar.dat'
file_path_SD  = fr'VLE_CO2_Ar/SD_VLE_CO2_Ar.dat'

SIM = np.loadtxt(file_path_SIM, skiprows=1)
SD =  np.loadtxt(file_path_SD, skiprows=1)


plt.plot(SIM[:,1],SIM[:,0],'ob', markeredgewidth=1, markerfacecolor='none')
#plt.plot(SIM[:,2],SIM[:,0],'or', markeredgewidth=1, markerfacecolor='none', label= f'Simulation, 253 K - (Dew)' )

plt.savefig('CO2_Ar.png')