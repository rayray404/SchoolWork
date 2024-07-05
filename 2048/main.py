from random import randint as r

B = list()
for i in range(4):
    B.append([0, 0, 0, 0])

def p_b(B):
    # print(B)
    for i in B:
        print(i)

def r_a(B):
    while True:
        a,b= r(0,3), r(0,3)
        if B[a][b]==0:
            # print('b',B)
            B[a][b] = r(1,2)*2
            # print(a, b, r(1,2)*2)
            # print('f', B)
            return B

def add(l):
    l = list(l)
    if len(l) < 4:
        if l[0]==l[1]
    for i in range(len(l)):
        if l[i+1]==l[i]:
            l[i:i+1] = 2*l[i]  
    return str(l)

def move(dir, B):
    match dir:
        case 'd':
            for i in range(len(B)):
                j = str(B[i]).replace('0', '')
                j = add(j)
                j = '0'*(4-len(j)) + j
                print(j)
                B[i] = list(j)
        case 'a':
            for i in range(len(B)):
                j = str(B[i]).replace('0', '')
                j = add(j[::-1])
                j =  j + '0'*(4-len(j))
                print(j)
                B[i] = list(j)
        case 'w':
            for i in range(len(B)):
                j = str([B[k][i] for k in range(len(B))]).replace('0', '')
                j = add(j[::-1])
                j =  j + '0'*(4-len(j))
                print(j)
                for k in range(len(B)):
                    B[k][i] = j[k]
        case 's':
            for i in range(len(B)):
                j = str([B[k][i] for k in range(len(B))]).replace('0', '')
                j = add(j)
                j = '0'*(4-len(j)) + j
                print(j)
                for k in range(len(B)):
                    B[k][i] = j[k]

while True:
    p_b(B)
    B=r_a(B)
    move(input(),B)
