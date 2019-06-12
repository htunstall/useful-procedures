# Useful colouring codes for terminal output
class colour:
   PURPLE    = "\033[95m"
   CYAN      = "\033[96m"
   DARKCYAN  = "\033[36m"
   BLUE      = "\033[94m"
   GREEN     = "\033[92m"
   YELLOW    = "\033[93m"
   RED       = "\033[91m"
   BOLD      = "\033[1m"
   UNDERLINE = "\033[4m"
   END       = "\033[0m"

# Returns true if all items in the list are identical
def compareList(_list):
    return all(i == _list[0] for i in _list)


