#=============================================
# Plot the NN and GAP data
#=============================================
import re
import os
import numpy as np
import matplotlib.pyplot as plt
import ase.io 

def get_max_lims(ax_list, factor=0.04):
    """
    Get the maximum lims for the graphs
    
    Where:
        ax_list: Is a list of the plot/residual axis pairs
    """
    maxs0 = []
    mins1 = []
    maxs1 = []
    for ax in ax_list:
        xlim    = ax[0].get_xlim()
        ylim    = ax[0].get_ylim()
        maxs0.append(max([xlim[1], ylim[1]]))
        
        ylim    = ax[1].get_ylim()
        mins1.append(ylim[0])
        maxs1.append(ylim[1])
        
    lim0 = [-factor, max(maxs0) + factor]
    lim1 = [min(mins1) - factor, max(maxs1) + factor]
    return lim0, lim1
#---------------------------------------------

def format_plot(ax, title, lims, fontsize=16, match_residuals=False):
    """
    Format the axes object to some specific standards.
    
    Where:
        ax:              A subplot list of matplotlib Axes
        title:           The title of the Graph
        lims:            A tuple of the maximum limits for the top/bottom graph
        fontsize:        The font size for all elements (note titles
                            are +2 larger)
        match_residuals: True makes the residual plots share a y axis
    """
    lim, residual_lim = lims
    
    #-----------------------------------------
    # Format the Graph
    #-----------------------------------------
    # Draw the lines
    ax[0].plot(lim, lim, color="k") # label="$x = y$"
    ax[1].hlines(0, lim[0], lim[1])

    # Make the top plot square
    ax[0].set_xlim(lim)
    ax[0].set_ylim(lim)

    # Display grids
    ax[0].grid()
    ax[1].grid()

    # Make sure the bottom plot uses the same limits to lign up the data points
    ax[1].set_xlim(lim)
    if match_residuals:
        ax[1].set_ylim(residual_lim)

    # Plot the legends
    ax[0].legend(loc=9, ncol=2, fontsize=fontsize-2, frameon=True, fancybox=True, shadow=True)
    ax[1].legend(loc=3,         fontsize=fontsize-2, frameon=True, fancybox=True, shadow=True)

    ax[0].set_title(title,                                      fontsize=fontsize+2)
    ax[0].set_ylabel("NN Energy [eV/atom]",                     fontsize=fontsize+2)
    ax[1].set_ylabel("NN Energy Deviation from\nDFT [eV/atom]", fontsize=fontsize)
    ax[1].set_xlabel("DFT Energy [eV/atom]",                    fontsize=fontsize)

    # Change the tick label size
    ax[0].yaxis.set_tick_params(labelsize=fontsize)
    ax[1].yaxis.set_tick_params(labelsize=fontsize)
    ax[1].xaxis.set_tick_params(labelsize=fontsize)

    llim, ulim = ax[1].get_ylim()
    ax2_height = ulim - llim

    # Draw the figure letter
    ax[0].text(lim[0] + (lim[1] - lim[0]) / 100, lim[1] - abs(lim[0] - lim[1])  / 20, "(a)", fontsize=26)
    ax[1].text(lim[0] + (lim[1] - lim[0]) / 100, ulim   - ax2_height / 11, "(b)", fontsize=26)
#---------------------------------------------

def files(regex):
    """
    Returns a list of lists containing filenames  (index 0) and it's associated epoch (index 1).
    
    Where:
        regex: Is a compiled regular expression object for locating the specific epoch(s) chosen
    """
    files_to_plot = []
    for item in sorted(os.listdir()):
        regex_match = regex.match(item)
        if regex_match:
            filename = regex_match.group(0)
            epoch    = regex_match.group(1)
            files_to_plot.append([filename, int(epoch)])
    return files_to_plot
#---------------------------------------------

def get_min_values(files_to_plot):
    """
    Get the minimum value for each epoch and return a list of them.
    
    Where:
        files_to_plot: Is the output of the files definition above
    """
    list_min_values = []
    for filename, epoch in files_to_plot:
        if epoch in best_epochs:
            data  = np.loadtxt(filename, skiprows=1)
            width = len(data[0,:])

            min_values = [None] * width
            for i in range(width):
                min_values[i] = min(data[:,i])
            list_min_values.append(min_values)
    list_min_values = np.array(list_min_values)

    min_values = []
    for i in range(width):
        min_values.append(min(list_min_values[:,i]))

    return np.array(min_values)
#---------------------------------------------

def plot_NN_performance(best_epochs, ax, min_value, _type):
    """
    Plot the neural network data.
    
    Where:
        best_epochs: Is either a number or a list of numbers corresponding to the epochs to plot
        ax:          Is a numpy aray of array of axes objects
        min_value:   A list of size data containing the miminum value of each column in data
        _type:       A string, for the legend of the plot data
    """
    # Sanitise the input of best_epochs
    if type(best_epochs) == int:
        best_epochs = [best_epochs]
    elif type(best_epochs) != list:
        raise TypeError("`best_epochs` should be an integer or a list!")
    
    for best_epoch in best_epochs:
        if int(epoch) == best_epoch:
            # data: 0 = index; 1 = DFT; 2=NN
            data      = np.loadtxt(filename, skiprows=1)

            # Shift the axis to make them easier to read
            x         = data[:,1] - min_value
            y         = data[:,2] - min_value

            # Convert from Hartree -> eV
            x         = x * ase.units.Hartree
            y         = y * ase.units.Hartree

            # Main data
            ax[0].scatter(x, y, label=_type)

            # Residuals
            residuals = y - x
            ax[1].scatter(x, residuals, marker="o", label="Residuals ({})".format(_type))
#---------------------------------------------

def plot_gap(filename, label, ax, colour):
    """
    Plot the GAP data.
    
    Where:
        filename: Is the path to the saved numpy array containing the x (col 0) and y (col 1) data.
        label:    Is the legend label string
        ax:       Is a numpy aray of array of axes objects
        colour    Is  the colour of the plot points
    """
    # GAP data array
    # 0 = gap | 1 = DFT
    data = np.loadtxt(filename, skiprows=1, delimiter=",")

    # Shift the axis to make them easier to read
    minimum = min([min(data[:,0]), min(data[:,1])])
    # Divide by the number of atoms in the system
    x         = (data[:,0] - minimum) / 216
    y         = (data[:,1] - minimum) / 216

    # Main data
    ax[0].scatter(x, y, label=label, color=colour)

    # Residuals
    residuals = y - x
    ax[1].scatter(x, residuals, marker="o", color=colour, label="Residuals ({})".format(label))
