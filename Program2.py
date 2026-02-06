# Richard Perez

def encoding(string):
    num = 1
    letter = []

    if not string:
        return ""
    # length of the string 
    for i in range(1, len(string)):
        if string[i] == string[i-1] and string[i] != " ":
            num += 1
        else:
            if num > 1:
                # append the number
                letter.append(str(num) + string[i-1])
            else:
                letter.append(string[i-1])
            num = 1
    if num > 1:
        letter.append(str(num) + string[-1])
    else:
        letter.append(string[-1])

    return "".join(letter)
    
# our three sample imputs
print(encoding("ddd"))
print(encoding("heloooooooo there"))
print(encoding("choosemeeky and tuition-free"))