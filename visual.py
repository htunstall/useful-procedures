import inspect, re
#================================================
# Externally called procedures
#================================================
def show(p):
  for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
    m = re.search(r'\bshow\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
    if m:
      print("{} = {}".format(m.group(1), p))

def h_line(_i=120, _symbol="-"):
    for i in range(_i): print(_symbol, end="")
    print("")
