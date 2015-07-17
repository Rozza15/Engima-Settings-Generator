"""
Enigma settings generator
For Kriegsmarine M3 - UKW = B
And Kriegsmarine M3 - UKW = C
Author: Rory Buchanan
E-mail: rbuchanan.1997@gmail.com

Copyright (C) 2015  Rory Buchanan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details see <http://www.gnu.org/licenses/>.
    
"""

from random import randint
from os.path import isfile
from datetime import date, timedelta

z = date.today()
filename = 'enigma_codes_%s.txt' % z.strftime('%y-%m-%d')


def file():
    if not isfile(filename):
        with open(filename, 'a') as f:
            f.write('')

    else:
        with open(filename, 'a') as f:
            f.write('\n')


def rotor_choice():  # Determines which rotors to use
    i = randint(1, 8)
    ii = randint(1, 8)
    iii = randint(1, 8)
    rotor_number = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII"}
    let_i = randint(1, 26)
    let_ii = randint(1, 26)
    let_iii = randint(1, 26)
    rotor_letter = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I",
                    10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R",
                    19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
    i_rot = rotor_number[i]
    ii_rot = rotor_number[ii]
    iii_rot = rotor_number[iii]
    i_let = rotor_letter[let_i]
    ii_let = rotor_letter[let_ii]
    iii_let = rotor_letter[let_iii]
    print("Use Rotors:")
    print("1:", i_rot)
    print("2:", ii_rot)
    print("3:", iii_rot)
    print("The rotors should be wired to:")
    print("1:", i_let)
    print("2:", ii_let)
    print("3:", iii_let, '\n')
    with open(filename, 'a') as f:
        f.write("Use Rotors:")
        f.write('\n')
        f.write("1: ")
        f.write(i_rot)
        f.write('\n')
        f.write("2: ")
        f.write(ii_rot)
        f.write('\n')
        f.write("3: ")
        f.write(iii_rot)
        f.write('\n')
        f.write("The rotors should be wired to:")
        f.write('\n')
        f.write("1: ")
        f.write(i_let)
        f.write('\n')
        f.write("2: ")
        f.write(ii_let)
        f.write('\n')
        f.write("3: ")
        f.write(iii_let)
        f.write('\n')
        f.write('\n')


def plugboard():  # Plugboard steckering
    steck_no = randint(0, 13)
    steck_list = []
    stecks_used = []
    m = 0
    while m < steck_no:
        steck = []
        n = randint(1, 26)
        o = randint(1, 26)
        c = 0
        while n in stecks_used:
            n = randint(1, 26)
        while o in stecks_used:
            o = randint(1, 26)
        if n != o:
            while c <= 1:
                if n not in stecks_used:
                    steck.append(n)
                    stecks_used.append(n)
                if o not in stecks_used:
                    steck.append(o)
                    stecks_used.append(o)
                c += 1
            steck_list.append(steck)
        m += 1
    print("Steckers to be used:", steck_no)
    print("Stecker combinations:")
    print(steck_list, '\n')
    with open(filename, 'a') as f:
        f.write("Steckers to be used: ")
        f.write(str(steck_no))
        f.write('\n')
        f.write("Stecker combinations: ")
        f.write(str(steck_list))
        f.write('\n')
        f.write('\n')


def rotor_pos():  # Rotor position
    i = randint(1, 26)
    ii = randint(1, 26)
    iii = randint(1, 26)
    num_letter = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J",
                  11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R",
                  19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
    i_let = num_letter[i]
    ii_let = num_letter[ii]
    iii_let = num_letter[iii]
    print("Rotor Positions:")
    print("Rotor I:", i_let)
    print("Rotor II:", ii_let)
    print("Rotor III:", iii_let, '\n')
    with open(filename, 'a') as f:
        f.write("Rotor Positions:\n")
        f.write("Rotor I: ")
        f.write(str(i_let))
        f.write('\n')
        f.write("Rotor II: ")
        f.write(str(ii_let))
        f.write('\n')
        f.write("Rotor III: ")
        f.write(str(iii_let))
        f.write('\n')
        f.write('\n')


def main():
    x = int(input("How many days would you like settings for?: "))
    x_str = str(x)
    with open(filename, 'a') as f:
        f.write('Settings for: %s days' % x_str)
    d = date.today()
    for i in range(x):
        print('-----------------')
        print(d)
        with open(filename, 'a') as f:
            f.write('\n-----------------\n')
            f.write(str(d))
            f.write('\n')
        rotor_choice()
        rotor_pos()
        plugboard()
        with open(filename, 'a') as f:
            f.write('-----------------\n')
        print('-----------------')
        d += timedelta(days=1)


file()
main()
