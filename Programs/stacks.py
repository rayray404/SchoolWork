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



def POP(Arr):
    if Arr:
        return Arr.pop()

Arr = eval(input("Input Stack (in list form): "))
while True:
    inp = input("Type pop to POP from Stack (quit to exit): ")
    if inp == "quit":
        break
    else:
        print("Popped element:", POP(Arr)) 
        print("New Stack:", Arr)