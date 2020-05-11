import inspect
import re

#================================================
# Externally called procedures
#================================================
def show(p):
	"""Print a variable name and it's value.
	
	Arguments:
		p      -- the variable to print
	"""
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
		m = re.search(r'\bshow\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
		if m:
			print("{} = {}".format(m.group(1), p))

def h_line(_i=120, _symbol="-"):
	"""Draw a horizontal line.
	
	Optional Arguments:
		_i      -- length of the line
		_symbol -- the symbol to repeat _i times
	"""
    print(_symbol * _i + "\n")
