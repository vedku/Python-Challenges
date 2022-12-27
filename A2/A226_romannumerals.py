def denary_to_roman(num):
    roman_numerals = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }
    roman = ""
    for value in sorted(roman_numerals.keys(), reverse=True):
        quotient, num = divmod(num, value)
        roman += roman_numerals[value] * quotient
    return roman

def roman_to_denary(roman):
    roman_numerals = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    num = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in roman_numerals:
            num += roman_numerals[roman[i:i+2]]
            i += 2
        else:
            num += roman_numerals[roman[i]]
            i += 1
    return num

choice = int(input("Would you like to convert from denary to roman[0] or roman to denary[1]:"))
if choice == 0:
    denary = int(input("Input your denary number here:"))
    result = denary_to_roman(denary)
    #trying f string so I don't need commas
    print(f"The Roman numeral equivalent of {denary} is {result}.")
elif choice == 1:
    roman = input("Input your Roman numeral here:")
    result = roman_to_denary(roman)
    print(f"The denary equivalent of {roman} is {result}.")
