# vowels = 'aeiou'
# i=2

# # match i:
# #     case 0:
# #         text_file = open(r"./Programs/File_Handling/file.txt", "r")
# #         print(text_file.read())
# #     case 1:
# #         text_file = open(r"./Programs/File_Handling/file.txt", "w")
# #         print(text_file.write("NEW TEXT\n"))
# #     case 2:
# #         text_file = open(r"./Programs/File_Handling/file.txt", "a")
# #         print(text_file.write("APPENDED TEXT\n"))

# with open(r"./file.txt", "r") as file:
#     text = file.read().lower()
# match i:
#     case 0: #count vowels
#         count = sum([text.count(i) for i in vowels])
#     case 1: #count words
#         count = len(text.split(" "))
#     case 2: #count vowel words
#         count = sum([i[0] in vowels for i in text.split(" ")])
# print(count)

import pickle

file = open(r'Programs\File_Handling\apple.bat', 'rb')
print(pickle.load(file))
