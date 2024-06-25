from fractions import Fraction

def get_int_positive(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x <= 0:
                print("Please enter a positive value")
                continue       
        except ValueError:
            print("Please enter a valid integer")
            continue
        else:
            return x 


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))      
        except ValueError:
            print("Please enter a valid integer")
            continue
        else:
            return x 

def get_float_positive(prompt):
    while True:
        try:
            x_input = input(prompt)
            if '/' in x_input:
                # Convert fractional input to float
                x = float(Fraction(x_input))
            else:
                x = float(x_input)
            
            if x <= 0:
                print("Please enter a valid positive value.")
                continue
        except ValueError:
            print("Please enter a valid numeric value.")
        else:
            return x


def get_percentage(prompt="Rate  :"):
    while True:
        x = get_float_positive(prompt)
        if x > 1:
            print("Please enter a value less than or equal to 1.")
        else:
            return x