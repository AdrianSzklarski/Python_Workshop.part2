"""     Adrian SZKLARSKI, 02.2022r,
            validate-PESEL:

The program will take the PESEL number as a text string,
then check its correctness and return:


Returns:    True if the PESEL is correct,
            False, if the PESEL number is invalid.

Parameters: PESEL (str): A initiger numbers form scope 0 to 9

Error:      TypeError, NoneType' object is not iterable
"""
import sys


class Pesel:

    def __init__(self, pesel):
        self.pesel = pesel
        self.result = False
        self.table_ascii = []

    # Breakdown of PESEL into characters
    def validate_pesel(self):
        if len(self.pesel) == 11:
            string_pesel = str(self.pesel)
            table = []
            for number in string_pesel:
                if number.isdigit():
                    table.append(number)
            return table
        else:
            sys.exit("You give wrong a value, try again!")

    # Conversion using ASCII to int
    def change_to_ascii(self):
        for ascii_no in self.validate_pesel():
            self.table_ascii.append(int(chr(ord(ascii_no))))
        return self.table_ascii

    # https://pl.wikipedia.org/wiki/PESEL
    # calculation according to the formula with WIKIPEDIA
    def calculation(self):
            _WEIHGT = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            mulitab = []
            for i in range(len(self.table_ascii) - 1):
                multi = _WEIHGT[i] * self.table_ascii[i]
                mulitab.append(multi)
            sumtab = sum(mulitab[:10])
            modtab = sumtab % 10
            minustab = 10 - modtab
            if minustab == self.table_ascii[-1]:
                self.result = True
            else:
                self.result = False

    def __str__(self):
            return f'The PESEL is: {self.result}'

if __name__ == '__main__':
    myP = Pesel(input('Enter PESEL for verification: '))
    myP.change_to_ascii()
    myP.calculation()
    print(myP)
