text = "454639"
# Q1 - Count odd and even number in text
# count_old = 0
# count_even = 0
# for i in range(len(text)):
#     if int(text[i]) % 2 != 0:
#         count_old += 1
#     elif int(text[i]) % 2 == 0:
#         count_even += 1
# print("even number: ", count_even, "old number: ", count_old)

# Q2 - Sum all number
# total = 0
# for i in range(len(text)):
#     total += int(text[i])
# print("Sum of all number: ", total)

# Q3 - Sum only even number
# sum_even_number = 0
# for i in range(len(text)):
#     if int(text[i]) % 2 == 0:
#         sum_even_number += int(text[i])
# print("Sum only even number: ", sum_even_number)
        
# Q4 - Reverse
reverse = ''
for i in range(len(text), 0, -1):
    reverse = text[i-1]
    print(reverse)
                 