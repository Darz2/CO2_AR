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
file_path_NIST = fr'CO2_Ar.txt'

SIM = np.loadtxt(file_path_SIM, skiprows=1)
SD =  np.loadtxt(file_path_SD, skiprows=1)
NIST = np.loadtxt(file_path_NIST, skiprows=10, usecols=(0, 1))
print(NIST[:269,0])
plt.plot(NIST[:269,0], NIST[:269,1], 'b-', label=f'GERG-2008 (Bubble)')
plt.plot(NIST[270:,0], NIST[270:,1], 'r-', label=f'GERG-2008 (Dew)')
plt.errorbar(SIM[:,1],SIM[:,0], xerr=SD[:,1], fmt='o',  capsize=8, markeredgewidth=1, color='black', markerfacecolor='blue', label= f'Simulation, 253 K - (Bubble)' )
plt.errorbar(SIM[:,2],SIM[:,0], xerr=SD[:,2], fmt='o', capsize=8,  markeredgewidth=1, color='black', markerfacecolor='red', label= f'Simulation, 253 K - (Dew)' )
plt.title('CO$_2$-Ar')
plt.xlabel(r'Mole fraction ($\mathit{x}$ or $\mathit{y}$)  - CO$_2$')
plt.ylabel(r'Preesure / [bar]')
plt.legend(fontsize=8, loc='best')
plt.savefig('CO2_Ar.png')