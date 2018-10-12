# Procedure for drawing a well formated graph
def draw_graph(_ax, _title="", _xlabel="", _ylabel="", _fontsize=8, _hline=False, _hline_pos=0,
               _hline_color="black", _draw=False, _x=None, _y=None, _linewidth=1, _sci=True,
               _grid=True, _bold=False,
               _show_legend=False, _legend_label=None):
    if _draw:
        _ax.plot(_x, _y, linewidth = _linewidth, label=_legend_label)
        
    if _bold:
        _ax.set_title(_title, fontsize = _fontsize + 2, fontweight = "bold")
    else:
        _ax.set_title(_title, fontsize = _fontsize)
    _ax.set_xlabel(_xlabel, fontsize = _fontsize)
    _ax.set_ylabel(_ylabel, fontsize = _fontsize)
    
    if _show_legend:
        _ax.legend()
        
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
def plot_subfig(x, y, title, axis, row, column, fullpath, xlabel, ylabel, fontsize=8,
                hline=False, hline_pos=0, hline_color="black", draw=True, data=""):
    if draw:
        if hline:
            draw_graph(axis[row, column], title, xlabel, ylabel, draw=True, _x=x, y=y,
                       _hline=True, _hline_pos=hline_pos, _hline_color=hline_color)
        else:
            draw_graph(axis[row, column], title, xlabel, ylabel, draw=True, _x=x, y=y)
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
