from random import randint as r

B = [[0]*4]*4

def r_a(B):
    while True:
        a,b= r(1,4), r(1,4)
        if B[a][b]!=0:
            B[a][b] = r(1,2)*2

def add(l):
    for i in range(len(l)):
        if l[i+1]==l[i]:
            l[i:i+1] = 2*l[i]

def move(dir, B):
    match dir:
        case 'd':
            for i in range(len(B)):
                j = str(B[i]).replace('0', '')
                j = '0'*(4-len(j)) + j
                B[i] = list(j)
        case 'a':
            for i in range(len(B)):
                j = str(B[i]).replace('0', '')
                j =  j + '0'*(4-len(j))
                B[i] = list(j)
        case 'w':
            for i in range(len(B)):
                j = str([B[k][i] for k in range(len(B))]).replace('0', '')
                j =  j + '0'*(4-len(j))
                for k in range(len(B)):
                    B[k][i] = j[k]
        case 'd':
            for i in range(len(B)):
                j = str([B[k][i] for k in range(len(B))]).replace('0', '')
                j = '0'*(4-len(j)) + j
                for k in range(len(B)):
                    B[k][i] = j[k]

while True:
