num = 58
roman_str = [None] * 4
roman_char = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
index = 0
for i in range(4):
    print "i: " + str(i)
    print "num: " + str(num)
    roman_str[i]=''
    x = num % 10

    if x == 0 :
        num /= 10
        index += 2
        continue

    print "x: " + str(x)
    if(x >= 5) :
        if(x == 9):
            roman_str[i] =  roman_char[index] + roman_char[index+2]
        else :
            roman_str[i] += roman_char[index+1]
            for j in range(x-5):
                roman_str[i] += roman_char[index]
    else:
        if(x == 4):
            roman_str[i] += roman_char[index] + roman_char[index+1]
        else :
            for j in range(x):
                roman_str[i] += roman_char[index]
    print "yes"
    num /= 10
    index += 2

final_string=""
for i in range(3, -1, -1):
    print "roman_str : " + roman_str[i]
    final_string += roman_str[i]
print final_string
