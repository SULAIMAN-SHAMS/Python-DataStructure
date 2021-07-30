stack = []
def push():
    add1=int(input("Enter value to add in stack"))
    stack.append(add1)
    print(stack)

def pop():

    if len(stack)==0:

        print("EMPTY STACK")
    else:

        p=stack.pop()
        print("Value popped out is", p)
        print(stack)

while True:


    choice=int(input("1.PUSH \n 2.POP \n 3.Quit"))
    if choice==1:

        push()
    elif choice==2:

        pop()
    else:

        exit()