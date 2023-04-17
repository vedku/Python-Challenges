def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


def roman_to_int(roman):
    roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in roman:
        value = roman_val[char]
        if value > prev_value:
            if prev_value in (1, 10, 100) and value == 5 * prev_value or value == 10 * prev_value:
                total += value - 2 * prev_value
            else:
                total += value
        else:
            total += value
        prev_value = value
    return total


while True:
    choice = input("Enter '1' for Integer to Roman, '2' for Roman to Integer, 'q' to quit:")
    if choice == "1":
        number = int(input("Enter an integer between 1 and 3999:"))
        if 0 < number < 4000:
            print(f"Roman numeral: {int_to_roman(number)}")
        else:
            print("Invalid input. Please enter a number between 1 and 3999.")
    elif choice == "2":
        roman_str = input("Enter a Roman numeral: ").upper()
        print(f"Integer: {roman_to_int(roman_str)}")
    elif choice.lower() == "q":
        break
    else:
        print("Invalid choice. Please try again.")
