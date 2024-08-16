text = "3 4 5 6"
total = 0
# Q1 - display number 1 by one without space
# for i in range(len(text)):
#     if text[i] != " ":
#         print(text[i])
# Q2 - Sum all number (Total: 18)
for i in range(len(text)):
    if text[i] != " ":
        total += int(text[i])
print(total)