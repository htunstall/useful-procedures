# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:07:29 2020

@author: Harry
"""

import re

class Roman():
    def __init__(self):
        self.roman_re = re.compile("^(M*)(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$")
        self.r2d      = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1, "":0}
        self.dval     = [1000,  900, 500,  400, 100,   90,  50,   40,  10,    9,    5,    4,   1]
        self.rval     = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V" , "IV", "I"]
    
    def check_roman(self, value):
        match = self.roman_re.match(value.upper())
        if match and value != "":
            return match
        else:
            return False
        
    def roman2decimal(self, roman):
        match = self.check_roman(roman)
        if match:
            decimal = 0
            for group in match.groups():
                for i, char in enumerate(group):
                    val = self.r2d[char]
                    if i > 0:
                        if pre_val < val:
                            decimal += val - pre_val
                        else:
                            decimal += pre_val
                    if i == len(group)-1:
                        decimal += val
                    pre_val = val
        else:
            raise ValueError("The input '{}' is not a roman numeral".format(value))
        return decimal
    
    def decimal2roman(self, decimal):
        roman = ""
        if type(decimal) is int:
            index = 0
            while decimal != 0:
                if decimal - self.dval[index] >= 0:
                    roman += self.rval[index]
                    decimal = decimal - self.dval[index]
                else:
                    index += 1
        else:
            raise ValueError("The value '{}' is not an integer that can be converted to roman numerals".format(decimal))
        return roman
    

# DEBUG
print("Input:")
value = input()

roman = Roman()

print(roman.roman2decimal(value))