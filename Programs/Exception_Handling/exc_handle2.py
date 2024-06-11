# # #1 
# while True:
#     try:
#         inp = input("Input Integer: ")
#         if not ((inp[0]=='-' and inp[1:].isdigit()) or inp.isdigit()):
#             raise ValueError
#     except:
#         if inp=="exit":
#             break
#         print("ValueError: Non-integer convertible type")
#     else:
#         integer = int(inp)
#         print("Integer:", integer)

# #2
# while True:
#     try:
#         num1 = num2 = None
#         num1 = input("Number 1: ")
#         num2 = input("Number 2: ")
#         if not (num1.isnumeric() and num2.isnumeric()):
#             raise TypeError
#     except TypeError:
#         print("TypeError: Inputted Number is not of numeric data-type")
#     else:
#         sum = float(num1) + float(num2)
#         print("Sum:", sum)
#     finally:
#         if_exit = input("Exit? ")
#         if if_exit=="yes":
#             break

#3
lst = eval(input())