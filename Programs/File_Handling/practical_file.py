# #5.3
# count=int(input("Student Count: "))
# file_out = open("Marks.txt", 'w')
# for i in range(count):
#     print("Details of student", i+1)
#     rollno = input("Roll No: ")
#     name = input("Name: ")
#     mark = input("Marks: ")
#     string = ','.join((rollno, name, mark)) + '\n'
#     file_out.write(string)
# file_out.close()

#5.6
# read_file = open("file_text.txt", "r")
# text = read_file.read()
# for line in text.split('\n'):
#     print('#'.join(line.split())) 
# read_file.close()

#5.7
# read_file = open("file_text.txt", "r")
# lower_text = read_file.read().lower()
# vowels = "aeiou"
# vow_count = cons_count = 0
# for i in lower_text:
#     if i.isalpha():
#         if i in vowels:
#             vow_count+=1
#         else:
#             cons_count+=1
# print("Vowel Count:", vow_count)
# print("Consonant Count:", cons_count)
# read_file.close()

#5.8
# import pickle
# emps = [{"Rollno": 1201, "Name": "Andy", "Age": 25, "Salary": 50000},
#     {"Empno": 1211, "Name": "Amy", "Age": 23, "Salary": 47000}]
# with open("emp.dat", "wb") as emp_file:
#     for emp in emps:
#         pickle.dump(emp, emp_file)

# with open("emp.dat", "rb") as emp_file:
#     try:
#         while True:
#             print(pickle.load(emp_file))
#     except EOFError:
#         print()

# # #5.16
# import pickle
# stu={}
# found=[]
# with open('Stu.dat', 'rb') as stu_bin:
#     try:
#         while True:
#             stu=pickle.load(stu_bin)
#             if stu['Marks']>81:
#                 found.append(stu)
#     except EOFError:
#         if found:
#             print("Records with marks > 81: ", *found, sep='\n')
#         else:
#             print("No records with marks > 81 found")


# #5.18
# import pickle 
# stu={}
# with open('Stu.dat', 'rb+') as stu_bin:
#     try:
#         while True:
#             rpos = stu_bin.tell()
#             stu=pickle.load(stu_bin)
#             if stu['Rollno']==12:
#                 stu['Name'] = 'Gurnam'
#                 stu_bin.seek(rpos)
#                 pickle.dump(stu, stu_bin)
#                 break
#     except EOFError:
#         print("Record not found")


#5.19
# import csv
# write_file = open("stu.csv", "w")
# csv_writer = csv.writer(write_file)
# csv_writer.writerow(['Rollno', 'Name', 'Marks'])
# for i in range(1, 6):
#     print("Student Record", i)
#     rollno = int(input("Roll No: "))
#     name = input("Name: ")
#     marks = float(input("Marks: "))
#     stu_row = [rollno, name, marks]
#     csv_writer.writerow(stu_row)
# write_file.close()

#5.20
# import csv
# write_file = open("compresult.csv", "w")
# csv_writer = csv.writer(write_file)
# data = [['Name', 'Points', 'Rank'],
#         ['Shradha', 4500, 23],
#         ['Nishchay', 4800, 31],
#         ['Ali', 4500, 25],
#         ['Adi', 5100, 14]]
# csv_writer.writerows(data)
# write_file.close()

#5.22 
# import csv
# with open('compresult.csv', 'r', newline='\r\n') as read_file:
#     csv_reader = csv.reader(read_file)
#     for row in csv_reader:
#         print(row)

#C1
# with open('file_text.txt', 'r') as read_file:
#     text = read_file.readlines()
# new_text= ''
# for line in text:
#     new_text += " ".join(line.split())
#     new_text += "\n"
# with open('new_file_text.txt', 'w+') as write_file:
#     write_file.writelines(new_text)

#C2
# import pickle
# def athletics ():
#     athletics = []
#     with open("sports.dat", "rb") as read_file:
#         try:
#             while True:
#                 participant = pickle.load(read_file).split()
#                 if participant[0] == "Athletics":
#                     athletics.append(' '.join(participant))
#         except EOFError:
#             pass
#     with open("Athletic.dat", "wb+") as write_file:
#         for participant in athletics:
#             pickle.dump(participant, write_file)
# athletics()

#C3
# phone_num = []
# with open("phone.txt", "r") as read_file:
#     phone_num = read_file.readlines()
# for i in range(len(phone_num)):
#     string = phone_num[i]
#     string = string.split()[0:2]
#     phone_num[i] = string
# print("Name \t\t Phone")
# for num in phone_num:
#     print(num[0], "\t\t", num[1])

#c4
# with open("Poem.txt", "r") as read_file:
#     poem = read_file.read()
# poem = poem.lower().split()
# counts = {'to': poem.count('to'), 
#           'the': poem.count('the')}
# for i in counts:
#     print(i, "count:", counts[i])

#c5
# def AMCount():
#     with open("STORY.txt", "r") as read_file:
#         story = read_file.read()
#     story = story.lower()
#     counts = {'A': story.count('a'), 
#             'M': story.count('m')}
#     for i in counts:
#         print(i, "count:", counts[i])
# AMCount()

#c9
# def KLineCount():
#     with open("MYNOTES.txt", "r") as read_file:
#         notes = read_file.readlines()
#     counts = {'K': 0}
#     for line in notes:
#         if line[0].lower() == 'k':
#             counts["K"]+=1
#     for i in counts:
#         print(i, "count:", counts[i])
# KLineCount()

#c10
# def DISPLAYWORDS():
#     small_words = []
#     with open("STORY.txt", "r") as read_file:
#         story = read_file.read()
#     for word in story.split():
#         if len(word)<4:
#             small_words.append(word)
#     small_words = ', '.join(small_words)
#     print("Words with length less than 4:", small_words)
# DISPLAYWORDS()


#c15
# import pickle 

# def pickle_member():
#     members=[]
#     count = int(input("Member count: "))
#     for i in range(count):
#         member = {}
#         print(i+1, "Member Details")
#         member["MemberNo."] = int(input("Member Number: "))
#         member["Name"] = input("Member Name: ")
#         members.append(member)
#     with open("member.dat", "wb+") as write_file:
#         for member in members:
#             pickle.dump(member, write_file)
# pickle_member()

#c16
# import pickle 

# def find_s0105():
#     found = None
#     with open("staff.dat", "rb") as staff_file:
#         try:
#             while True:
#                 staff = pickle.load(staff_file)
#                 if staff['Staffcode'] == "S0105":
#                     found = staff
#         except EOFError:
#             pass
#     if found==None:
#         print("No staff with ID S0105 found")
#     else:
#         print(found)
# find_s0105()

#c19


# import pickle

# def CreateFile():
#     count = int(input("Book Count: "))

#     for i in range(count):
#         print("Book", i+1)
#         with open("Book.dat", "ab") as book_file:
#             book_no = int(input("Book Number: "))
#             book_name = input("Name: ")
#             author = input("Author: ")
#             price = float(input("Price: "))
#             book = [book_no, book_name, author, price]
#             pickle.dump(book, book_file)

# def CountRec(Author):
#     books_written=0
#     with open("Book.dat", "rb") as book_file:
#         try:
#             while True:
#                 book = pickle.load(book_file)
#                 if book[2]==Author:
#                     books_written+=1
#         except EOFError:
#             print("Total Books written by", Author, ":", books_written)
        
# CreateFile()
# CountRec("Newton")


#c20
# def Show_words():
#     five_words = []
#     with open("NOTES.txt", 'r') as read_file:
#         text = read_file.read()
#     text=text.split('\n')
#     for line in text:
#         words = line.split()
#         if len(words)==5:
#             five_words.append(line)
#     five_words = '\n'.join(five_words)
#     print(five_words)
# Show_words()

#c23
# import csv

# def delimin_changer(delim):
#     rows = []
#     read_file = open("csv_file.csv", 'r')
#     reader = csv.reader(read_file, delimiter=",")
#     for row in reader:
#         rows.append(row)
#     read_file.close()

#     write_file = open("new_csv_file.csv", 'w+')
#     writer = csv.writer(write_file, delimiter=delim)
#     writer.writerows(rows)
#     write_file.close()

# delimin_changer('@')

#c25
import csv

def add():
    fid = int(input("ID: "))
    fname = input("Name: ")
    fprice = input("Price: ")
    record = [fid, fname, fprice]
    write_file = open("furdata.csv", 'a')
    writer = csv.writer(write_file)
    writer.writerow(record)
    write_file.close()

def search():
    costly_furniture = []
    read_file = open("furdata.csv", 'r')
    reader = csv.reader(read_file)
    for row in reader:
        if int(row[2])>10000:
            costly_furniture.append(row)
    read_file.close()
    print("Records of furniture with price more than 10,000:")
    for furniture in costly_furniture:
        print(furniture)

count = int(input("Furniture Count: "))
for i in range(count):
    print("Furniture", i+1)
    add()

search()