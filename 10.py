# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
mix = 0
min = 0
for  i in range(5):
    number = int(input('Enter a number: '))
    if mix == 0 and mix == 0:
        mix = number
        min = number
    elif number > mix:
        mix = number
    elif number < min:
        min = number
print("Min=", min)
print("Max=", mix)