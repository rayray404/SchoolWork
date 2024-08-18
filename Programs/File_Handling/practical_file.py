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
