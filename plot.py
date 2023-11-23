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
file_path_EXP = fr'experiment.dat'

SIM = np.loadtxt(file_path_SIM, skiprows=1)
SD =  np.loadtxt(file_path_SD, skiprows=1)
NIST = np.loadtxt(file_path_NIST, skiprows=9, usecols=(0, 1))

#Isothermal P, x, y data for the argon + carbon dioxide system atsix temperatures from 233.32 to 299.21 K and pressures up to 14 MPa

EXP = np.loadtxt(file_path_EXP, skiprows=1, usecols=(0,1,2))

#print(EXP[:,0])

plt.plot(1-EXP[:,1], EXP[:,0]*10,'^b', markeredgewidth=1, markerfacecolor='none', label=f'C. Coquelet a, A. Valtz a et. al, (2008)')
plt.plot(1-EXP[:,2], EXP[:,0]*10,'^r' , markeredgewidth=1, markerfacecolor='none' )
plt.plot(NIST[:269,0], NIST[:269,1], 'b-', label=f'GERG-2008')
plt.plot(NIST[270:,0], NIST[270:,1], 'r-')
plt.errorbar(SIM[:,1],SIM[:,0], xerr=SD[:,1], fmt='o',  capsize=8, markeredgewidth=1, color='black', markerfacecolor='blue')
plt.errorbar(SIM[:,2],SIM[:,0], xerr=SD[:,2], fmt='o', capsize=8,  markeredgewidth=1, color='black', markerfacecolor='red')
plt.title('CO$_2$-Ar')
plt.ylim(20, 200)
plt.xlabel(r'Mole fraction ($\mathit{x}$ or $\mathit{y}$)  - CO$_2$')
plt.ylabel(r'Preesure / [bar]')
dummy_line1, = plt.plot([], [], 'o', markeredgewidth=1, color='black', markerfacecolor='k', label= f'CFCMC-GE' )
legend = plt.legend(fontsize=8, loc='best')
for handle in legend.legendHandles:
    handle.set_color("black")
plt.savefig('CO2_Ar.png')