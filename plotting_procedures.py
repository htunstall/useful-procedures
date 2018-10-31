from matplotlib.font_manager import FontProperties
#================================================
# Internally called procedures
#================================================
#   Procedure for drawing a well formated graph
def draw_graph(_ax, _title, _xlabel, _ylabel, _fontsize, _hline, _hline_pos, 
               _hline_color, _x, _y, _linewidth, _sci, _grid, _bold, _marker, _marker_style,
               _show_legend, _legend_outside, _legend_label, _fancybox, _shadow, _ncol, _legend_monospace,
               _legend_fontsize):
    if _marker:
        _ax.plot(_x, _y, linewidth=_linewidth, label=_legend_label, marker=_marker_style)
    else:
        _ax.plot(_x, _y, linewidth=_linewidth, label=_legend_label)

    if _bold:
        _ax.set_title(_title, fontsize = _fontsize + 2, fontweight = "bold")
    else:
        _ax.set_title(_title, fontsize = _fontsize + 2)

    _ax.set_xlabel(_xlabel, fontsize = _fontsize)
    _ax.set_ylabel(_ylabel, fontsize = _fontsize)

    o_font = FontProperties()
    o_font.set_size(_legend_fontsize)
    if _legend_monospace:
        o_font.set_family("monospace")

    if _show_legend and _legend_outside:
        _ax.legend(fancybox=_fancybox, shadow=_shadow, ncol=_ncol, loc="upper center", bbox_to_anchor=(0.5, -0.1), prop=o_font)
    elif _show_legend:
        _ax.legend(fancybox=_fancybox, shadow=_shadow, ncol=_ncol, prop=o_font)

    if _grid:
        _ax.set_axisbelow(True)
        _ax.tick_params(axis = "both", direction = "out", labelsize = _fontsize)
        _ax.yaxis.grid(color = "lightgray", linestyle = "-", linewidth = _linewidth)
        _ax.xaxis.grid(color = "lightgray", linestyle = "-", linewidth = _linewidth)

    if _hline:
        _ax.axhline(_hline_pos, color = _hline_color, linewidth = _linewidth)

    if _sci:
        _ax.ticklabel_format(style = 'sci', axis = 'y', scilimits = (0,0), fontsize = _fontsize)
        _ax.yaxis.offsetText.set_fontsize(_fontsize)

#================================================
# Externally called Procedures
#================================================
# Draws the elements of one of the six subfigures contained within each page of the PDF file
def plot_subfig(_axes, _row=None, _column=None, _title="", _xlabel="", _ylabel="", _fontsize=8, _hline=False,
                _hline_pos=0, _hline_color="black", _x=None, _y=None, _linewidth=1, _sci=True, _draw=True,
                _grid=True, _bold=False, _marker=False, _marker_style="o", _show_legend=False, _legend_outside=False,
                _legend_label=None, _fancybox=True, _shadow=True, _ncol=1, _legend_monospace=False, _legend_fontsize=8, _data=""):
    _ax = None
    # If the row and column vars exist
    if _row != None and _column != None:
        _ax = _axes[_row, _column]
    # Else if the row var exists
    elif _row != None:
        _ax = _axes[_row]
    else:
        _ax = _axes
    if _draw:
        draw_graph(_ax, _title, _xlabel, _ylabel, _fontsize, _hline, _hline_pos,
                   _hline_color, _x, _y, _linewidth, _sci, _grid, _bold, _marker, _marker_style,
                   _show_legend, _legend_outside, _legend_label, _fancybox, _shadow, _ncol, _legend_monospace,
                   _legend_fontsize)
    else:
        o_font = FontProperties()
#        o_font.set_family(o_font)
        o_font.set_family("monospace")
        axis[row, column].text(0,
                               1,
                               _data,
                               size=_fontsize - 2,
                               ha="left",
                               va="top",
                               fontproperties=o_font)
        axis[row, column].axis("off")

# Saves a figure using some defaults
def save_fig(_fig, _filename, _path, _overwrite=False, _padding=3):
    import os.path

    # Make the figure look good
    _fig.tight_layout(pad=_padding)

    _fullpath = None
    # If there's no extenstion, then add one
    if not ".png" in _filename.lower() and not ".jpg" in _filename.lower() and not ".jpeg" in _filename.lower():
       _filename += ".png"
    # Create the fullpath
    _fullpath = os.path.join(_path, (_filename))

    if not os.path.isfile(_fullpath) or _overwrite:
        _fig.savefig(_fullpath)
    else:
        print("\nThe graph '{}' was not saved, as it already exists.\n   If you wish to save with overwrite, pass _overwrite=True into plotting_procedures.save_fig().".format(_filename))
