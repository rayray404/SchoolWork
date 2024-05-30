# def push(stack, item):
#     stack.append(item)

# def pop(stack):
#     if stack:
#         return stack.pop()

# def odd_push(num):
#     if num%2:
#         push(stack, num)

# def get_largest(stack):
#     elem = pop(stack)
#     large = elem

#     while elem!=None:
#         if elem > large:
#             large = elem
#         elem = pop(stack)
#     return large

# n = int(input("Count: "))
# stack = []

# for i in range(n):
#     number = int(input("Number: "))
#     odd_push(number)

# print("Stack: ", stack)
# large = get_largest(stack)
# print("Largest in Stack: ", large)


# def push(stack, item, repeat=1):
#     while repeat>0:
#         stack.append(item)
#         repeat-=1

# def pop(stack):
#     if stack:
#         return stack.pop()

# inp_text = input("Input Text Line: ")
# stack=[]
# for i in inp_text:
#     push(stack, i, 2)

# out_text = ""
# while stack:
#     out_text+=pop(stack)

# print("Output Text Line: ", out_text)



# def POP(Arr):
#     if Arr:
#         return Arr.pop()

# Arr = eval(input("Input Stack (in list form): "))
# while True:
#     inp = input("Type pop to POP from Stack (quit to exit): ")
#     if inp == "quit":
#         break
#     else:
#         print("Popped element:", POP(Arr)) 
#         print("New Stack:", Arr)


# def push(stack, item):
#     stack.insert(0, item)

# def pop(stack):
#     if stack:
#         return stack.pop(0)

# stack = []
# while True:
#     print("Commands:", "pop: POP the top element (1st)", "push {element}: PUSH the {element} above top (1st)", "display: DISPLAY the stack", "(anything else): Exit the Loop", sep='\n')
#     inp = input("Command:")
#     if inp=="pop":
#         pop(stack)
#     elif inp.startswith("push"):
#         push(stack, inp.partition(' ')[-1])
#     elif inp=="display":
#         print(stack)
#     else:
#         break
#     print()


# def PUSH(stack, node):
#     stack.append(node)

# def POP(stack):
#     if stack:
#         return stack.pop()
    
# stack = []
# while True:
#     print("Commands:", "PUSH: add node", "POP: remove node", "EXIT: exit", sep="\n")
#     inp = input("Command: ")
#     if inp=="PUSH":
#         pin = input("Pin Code of Node City: ")
#         name = input("Name of Node City: ")
#         PUSH(stack, {"pincode":pin, "name":name})
#     elif inp=="POP":
#         POP(stack)
#     elif inp=="EXIT":
#         break
#     print(stack)



# def PUSH(books, book_name):
#     books.append(book_name)

# def POP(books):
#     if books:
#         return books.pop()

# books = []
# while True:
#     print("Commands:", "PUSH {BOOK_NAME}: add {BOOK_NAME} to books", "POP: remove book from books", "EXIT: exit", sep="\n")
#     inp = input("Command: ")
#     if inp.startswith("PUSH"):
#         PUSH(books, inp.partition(' ')[-1])
#     elif inp=="POP":
#         POP(books)
#     elif inp=="EXIT":
#         break
#     print(books)


# def push(stack, element, check_divisible=1):
#     if element%check_divisible==0:
#         stack.append(element)

# def PUSH(Arr):
#     num_stack = []
#     for num in Arr:
#         push(num_stack, num, 5)
#     return num_stack

# num_list = eval(input("List of Numbers: "))
# num_stack = PUSH(num_list)

# if num_stack:
#     print("Stack with elements divisible by 5:", num_stack)
# else:
#     print("ERROR: Empty Stack Generated")