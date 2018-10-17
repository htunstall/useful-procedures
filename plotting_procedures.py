# Procedure for drawing a well formated graph
def draw_graph(_ax, _title, _xlabel, _ylabel, _fontsize, _hline, _hline_pos, 
               _hline_color, _x, _y, _linewidth, _sci, _grid, _bold, _marker, _marker_style,
               _show_legend, _legend_label):
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

    if _show_legend:
        _ax.legend(fontsize=_fontsize)

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


# Draws the elements of one of the six subfigures contained within each page of the PDF file
def plot_subfig(_axes, _row=None, _column=None, _title="", _xlabel="", _ylabel="", _fontsize=8, _hline=False,
                _hline_pos=0, _hline_color="black", _x=None, _y=None, _linewidth=1, _sci=True, _draw=True,
                _grid=True, _bold=False, _marker=False, _marker_style="o", _show_legend=False,
                _legend_label=None, _data=""):
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
                   _show_legend, _legend_label)
    else:
        o_font = font_manager.FontProperties()
        o_font.set_family(o_font)
        o_font.set_family("monospace")
        axis[row, column].text(0,
                               1,
                               _data,
                               size=_fontsize - 2,
                               ha="left",
                               va="top",
                               fontproperties=o_font)
        axis[row, column].axis("off")
