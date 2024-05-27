P9.1) Stack Implementation
def is_empty(stack):
    if stack==[]:
        return True
    else:
        return False

def push(stack, item):
    stack.append(item)
    top=len(stack)-1

def Pop(stack):
    if is_empty(stack):
        return "Underflow"
    else:
        item = stack.pop()
        if len(stack)==0:
            top=None
        else:
            top = len(stack)-1
        return item

def peek(stack):
    if is_empty(stack):
        return "Underflow"
    else:
        top = len(stack)-1
        return stack[top]

def display(stack):
    if is_empty(stack):
        print("Stack Empty")
    else:
        top = len(stack)-1
        print(stack[top],"<-top")
        for a in range(top-1, -1, -1):
            print(stack[a])

Stack = []
top=None
while True:
    print("STACK OPERATIONS", "1PUSH", "2POP", "3PEEK", "4DISPLAY", "5EXIT", sep="\n")
    inp = int(input("Choice: "))
    match inp:
        case 1:
            item = int(input("Item:"))
            push(Stack, item)
        case 2:
            item = Pop(Stack)
            if item=="Underflow":
                print("Underflow Error")
            else:
                print("Popped:", item)
        case 3:
            item = peek(Stack)
            if item=="Underflow":
                print("Underflow Error")
            else:
                print("Top:", item)
        case 4:
            display(Stack)
        case 5:
            break
    if str(inp) not in "12345":
        print("Invalid Choice")

21)
def PushS(List):
    num = int(input("Integer: "))
    List.append(num)
def PopS(List):
    if not List:
        print("Underflow")
    else:
        print("Popped:", List.pop())

no_vowel = []
vowels = "aeiou"

def PushNV(a):
    for i in range(len(a)):
        is_vowel = False
        for j in a[i]:
            if j.lower() in vowels:
                is_vowel =True
                break
            if not is_vowel:
                no_vowel.append(a[i])
                all = []
            for i in range(5):
                word = input("Word:")
                all.append(word)
            PushNV(all)
            if not len(no_vowel):
                print("Empty Stack")
            while len(no_vowel):
                print(no_vowel.pop(), end=" ")
            print()


23
def InsertQ(Names):
    naem = input("Name: ")
    Names.append(naem)

def DeleteQ(Names):
    if Names:
        print("Deleted:", Names[0])
        del Names[0]
    else:
        print("Undeflow") 

24)
def MakePush(Packages):
    package = input("Package: ")
    Packages.append(package)
def MakePop(Packages):
    if Packages==[]:
        print("Undeflwo")
    else:
        print("Popped: ", Packages.pop())


25) 

def push(stk, item):
    stk.append(item)
    
stack = []
for k,v in eval(input("Dict: ")).items():
    if v>=75:
        push(stack, k)
print(stack)


26) def PUSH(books, book):
    books.append(book)

def POP(books):
    if books:
        return books.pop()

books = []
while True:
    print("Commands:", "PUSH {BOOK_NAME, BOOK_ID}: add {BOOK_NAME, BOOK_ID} to books", "POP: remove book from books", "EXIT: exit", sep="\n")
    inp = input("Command: ")
    if inp.startswith("PUSH"):
        PUSH(books, tuple(eval(inp.partition(' ')[-1])))
    elif inp=="POP":
        POP(books)
    elif inp=="EXIT":
        break
    print(books)


27) def PUSH(memberslist, member):
    memberslist.append(member)

def POP(memberslist):
    if memberslist:
        return memberslist.pop()

memberslist = []
while True:
    print("Commands:", "PUSH {MEMBERNO, MEMBERNAME, AGE}: add {MEMBER} to memberslist", "POP: remove member from memberslist", "EXIT: exit", sep="\n")
    inp = input("Command: ")
    if inp.startswith("PUSH"):
        member_lst = inp.partition(' ')[-1].split(", ")
        member_lst[0] = int(member_lst[0])
        member_lst[2] = int(member_lst[2])
        PUSH(memberslist, member_lst)
    elif inp=="POP":
        POP(memberslist)
    elif inp=="EXIT":
        break
    print(memberslist)



TYPE C
def push(stack, item):
    stack.append(item)
def Pop(stack):
    if stack:
        return stack.pop()
    else:
        return "UNDERFLOW"

stack = []
while True:
    print("1)PUSH ITEM", "2)POP ITEM", "3EXIT", sep="\n")
    inp = int(input("CHoice: "))
    match inp:
        case 1:
            item = input()
            push(stack, item)
        case 2:
            print(Pop(item))
        case 3:
            break
    print(stack)

def sinsert(stack, item):
    stack.append(item)
def sdelete(stack):
    if stack:
        return stack.pop()
    else:
        return "UNDERFLOW"

stack = []
while True:
    print("1)INSERT ITEM", "2)DELETE ITEM", "3EXIT", sep="\n")
    inp = int(input("CHoice: "))
    match inp:
        case 1:
            item = input()
            sinsert(stack, item)
        case 2:
            print(sdelete(item))
        case 3:
            break
    print(stack)

def sinster(stack, item):
    stack.insert(0, item)

def sppop(stack):
    if stack:
        return stack.pop(0)

stack = []
while True:
    print("Commands:", "pop: POP the top element (1st)", "push {element}: PUSH the {element} above top (1st)", "display: DISPLAY the stack", "(anything else): Exit the Loop", sep='\n')
    inp = input("Command:")
    if inp=="pop":
        sppop(stack)
    elif inp.startswith("push"):
        sinster(stack, inp.partition(' ')[-1])
    elif inp=="display":
        print(stack)
    else:
        break
    print()


