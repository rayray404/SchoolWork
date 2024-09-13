student = ["Rahul, Mehul, Manisha, Sujoy, Sonakshi, Suman",
"XII, XII, XI, XI, XII, X",
"1200, 1200, 1050, 1050, 1200, 950",
"M, M, F, M , F, F",
"2005-02-01, 2004-12-11, 2006-10-12, NULL, 2005-09-19, 2008-06-16"]
output = ""
for i in range(len(student)):
    student[i] = student[i].split(', ')
print(student)
for i in range(len(student[0])):
    output+='('
    for j in range(len(student)):
        a = student[j][i]
        if a.isdigit() or a=="NULL":
            output+=a
        else:
            output += '"'+a+'"'
        if j<len(student)-1:
            output+=", "
    if i<len(student[0])-1:
        output+="), "
    else:
        output+=")"
print(output)