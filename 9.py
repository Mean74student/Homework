string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# number = ""
# for i in range(len(string)):
#     if string[i] != " ":
#         number += string[i]
# print(number)

# Q2 - Multiple each letter by 2 result = "6 8 10 12"
number = ""
for i in range(len(string)):
    if string[i] != " ":
        number += str(int(string[i]) * 2) + " "
print(number)
    