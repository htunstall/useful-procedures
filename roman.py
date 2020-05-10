"""
Created on Tue Mar  3 21:07:29 2020

@author: Harry Tunstall
"""

import re
import argparse

class Roman():
    def __init__(self):
        self.roman_re = re.compile("^(M*)(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$")
        self.r2i      = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1, "":0}
        self.ival     = [1000,  900, 500,  400, 100,   90,  50,   40,  10,    9,    5,    4,   1]
        self.rval     = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V" , "IV", "I"]
    
    def check_roman(self, value):
        """Check if a string is a roman numeral.
        
        Arguments:
            value -- the string to check
        """
        match = self.roman_re.match(value.upper())
        if match and value != "":
            return match
        else:
            return False
    
    def roman2int(self, roman):
        """Convert a roman numeral to an integer.
        
        Arguments:
            roman -- the string to convert to an integer value        
        """        
        match = self.check_roman(roman)
        if match:
            integer = 0
            for group in match.groups():
                for i, char in enumerate(group):
                    val = self.r2i[char]
                    if i > 0:
                        if pre_val < val:
                            integer += val - pre_val
                        else:
                            integer += pre_val
                    if i == len(group)-1:
                        integer += val
                    pre_val = val
        else:
            raise ValueError("The input '{}' is not a roman numeral".format(value))
        return integer
    
    def int2roman(self, integer):
        """Convert an integer to a roman numeral.
        
        Arguments:
            integer -- the integer to convert
        """
        roman = ""
        if type(integer) is int:
            index = 0
            while integer != 0:
                if integer - self.ival[index] >= 0:
                    roman += self.rval[index]
                    integer = integer - self.ival[index]
                else:
                    index += 1
        else:
            raise ValueError("The value '{}' is not an integer that can be converted to roman numerals".format(integer))
        return roman

#======================
# Parser    
#======================
parser = argparse.ArgumentParser(description="A suite to convert between roman numerals and integers")
group  = parser.add_mutually_exclusive_group()
group.add_argument("--int",   metavar="i", type=int, nargs="?", help="An interger to convert to a roman numeral")
group.add_argument("--roman", metavar="r", type=str, nargs="?", help="A roman numeral to convert to an integer")

args = parser.parse_args()
if args.int:
    roman = Roman()
    print(roman.int2roman(args.int))
elif args.roman:
    roman = Roman()
    print(roman.roman2int(args.roman))