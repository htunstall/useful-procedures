#!/bin/python3
import sys
import math
import datetime
import argparse
import matplotlib.ticker
import numpy                 as np
import matplotlib.pyplot     as plt
from   scipy.ndimage.filters import uniform_filter1d

#==============================================================================
# Parser
#==============================================================================
parser = argparse.ArgumentParser()
parser.add_argument("filename",       type=str,                                  help="The data file")
parser.add_argument("--filter_width", type=int,            default=101,          help="The width of the filter to apply to the data")
parser.add_argument("--relative",                          action="store_false", help="Do we want the plot to start at time 0")

args = parser.parse_args()

#==============================================================================
# Read in and convert the file
#==============================================================================
if args.filename.endswith("csv"):
    data      = np.loadtxt(args.filename, delimiter=",", skiprows=1, dtype=str)
    sani_data = np.zeros((data.shape[0], 3))
    for i, (day, time, temp, humid) in enumerate(data):
        date_str = "{} {}".format(day, time)
        date     = datetime.datetime.strptime(date_str, "%m/%d/%y %H:%M")
                
        sani_data[i,0] = date.timestamp()   
        sani_data[i,1] = float(temp)
        sani_data[i,2] = float(humid)
        
elif args.filename.endswith("npy"):
    sani_data = np.read(args.filename)
    
else:
    sys.exit("We can't read that file format yet")
     
# Zero the time column if we want to
if args.relative:
    sani_data[:,0] -= sani_data[0,0]

#np.save("temp-humi-data.npy", sani_data)
    
#==============================================================================
# Plotting
#==============================================================================
title        = "Physical Quantities Trend"
fontsize     = 16
nticks       = 7

fig, ax = plt.subplots(1,1, figsize=(10,10))
ax2 = ax.twinx()

time = sani_data[:,0] / 60**2 # s -> h

temp = sani_data[:,1]
humi = sani_data[:,2]

# The filter is similar to a rolling average
lns  = ax.plot(time,  uniform_filter1d(temp, size=args.filter_width),  label="Temperature", color="r")
lns += ax2.plot(time, uniform_filter1d(humi, size=args.filter_width),  label="Humidity",    color="b")

#==============================================================================
# Formatting
#==============================================================================
ax.set_title(title, fontsize=fontsize+4)

# set format for y axis (temp) labels
ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.2f'))

# For all axes
for _ax in [ax, ax2]:
    _ax.tick_params(axis="both", labelsize=fontsize)
    ylim = _ax.get_ylim()
    ylim = (math.floor(ylim[0]), math.ceil(ylim[1]))
    _ax.set_ylim(ylim)


# Mess with the tick positions (to line up hte left and right y axis) due to the twin ax
ax.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
ax2.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))

# Make one legend for the two plots
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc="lower right", fontsize=fontsize)

ax.grid()
ax.set_xlabel("Time [h]",         fontsize=fontsize)
ax.set_ylabel("Temperature [°C]", fontsize=fontsize)
ax2.set_ylabel("Humidity [%]",    fontsize=fontsize)


fig.savefig("data.png", dpi=300, bbox_inches="tight")