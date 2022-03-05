def AdditionDigit(i):
    sum = 0
    while i > 0 :
        sum = sum + i%10
        i=i//10
    return sum

i = int(input("enyer the number: "))
print("addition of digit: ",AdditionDigit(i))


