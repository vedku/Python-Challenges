thousandscolumn = []
hundrethscolumn = []
tenscolumn = []
onescolumn = []

number = input("What number do you want to convert to roman numerals?:")

for i in range(len(number)):
    if len == 1:
        onescolumn = (number[0])
    elif len ==2:
        tenscolumn = (number[0])
        onescolumn = (number[1])
    elif len ==3:
        hundrethscolumn = (number[0])
        tenscolumn = (number[1])
        onescolumn = (number[2])
    elif len==4:
        thousandscolumn = (number[0])
        hundrethscolumn = (number[1])
        tenscolumn = (number[2])
        onescolumn = (number[3])
