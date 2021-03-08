'''Convert decimal number(considering float values also) to binary/octal/hexa decimal form.
if number is negative represent represent it in 2's compliment also'''


import sys
# DECIMAL TO BINARY CONVERSION
def conversion_of_binary():
    global  binary_integer_part, binary_fractional_part, binary_total, integer_part, fractional_part

    integer_part = int(number)
    binary_integer_part = bin(integer_part)[2:]  # a[2:]
    fractional_part = number - integer_part
    binary_fractional_part = conversion_of_fraction(fractional_part, 2)
    binary_total = binary_integer_part + '.' + binary_fractional_part
    return binary_total

# CONVERSION TO FRACTION PART TO BINARY
def conversion_of_fraction(num, base):
    binary = ''
    round_of = 0
    while num != 0 and round_of < 12:    # considered upto 12 because is is multiple of both 3 & 4, so easy to covert binary to octal and hexa
        num = num *base
        binary = binary + str(int(num))
        num = num - int(num)
        round_of += 1
    return binary

# REPRESENTING NEGATIVE NUMBER IN 2'S COMPLIMENT FORM
def compliment_form(num):
    num = '0' + num  # here zero is for sign representation or extra bit  eg: -15
    num = list(num)
    first_time = 0
    i = -1
    length = -len(num)
    while i >= length:
        if first_time == 1:
            if num[i] == '1':
                num[i] = '0'
            elif num[i] == '0':
                num[i] = '1'
            elif num[i] == '.':
                num[i] =  '.'
        if num[i] == '1' and first_time == 0:
            first_time = 1
    
        i -= 1
    length = length - 1
    # print(''.join(map(str, num)), type(''.join(map(str, num))))
    return ''.join(map(str, num))


def bin_2_oct():
    octal_integer_part = oct(integer_part)
    octal_fractional_part = conversion_of_fraction(fractional_part, 8)
    return octal_integer_part +'.'+ octal_fractional_part

def bin_2_hex():
    hex_integer_part = hex(integer_part)
    hex_fractional_part = conversion_of_fraction(fractional_part, 16)
    return hex_integer_part + '.' + hex_fractional_part

while True:
    try:
        number = input("\n\nDECIMAL TO BINARY, OCTAL AND HEXA DECIMAL\n ENTER A DECIMAL NUMBER:")
        number = float(number)    # by default number is global variable(object)
        print("GIVEN NUMBER IS {0}\n".format(number))

        if number < 0:
            number = number * -1
            print("\tBINARY FORM IS \t-0b{0}".format(conversion_of_binary()))
            print("\tOCTAL  FORM IS \t-{0}".format(bin_2_oct()))
            print("\tHEXA   FORM IS \t-{0}".format(bin_2_hex()))
            print("\nSince number is -{0} (negative) , its 2's complement form is {1}".format(number,
                                                                                        compliment_form(binary_total)))

        else:
            conversion_of_binary()
            print("\tBINARY FORM IS \t0b{0}".format(conversion_of_binary()))
            print("\tOCTAL  FORM IS \t{0}".format(bin_2_oct()))
            print("\tHEXA   FORM IS \t{0}".format(bin_2_hex()))

        number = input("\n\n\nTO START PRESS ANY KEY \nTO QUIT PRESS (q)....:")
        if number == 'q' or number == 'Q':
            sys.exit()

    except ValueError as x:
        print(x)
