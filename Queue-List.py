queue = []
def enqueue():
    add1=int(input("Enter value to add in queue"))
    queue.append(add1)
    print(queue)

def dequeue():

    if len(queue)==0:

        print("EMPTY queue")
    else:

        p=queue.pop(0)
        print("Value dequeued is", p)
        print(queue)

while True:


    choice=int(input("1.ENQUEUE \n 2.DEQUEUE \n 3.Quit"))
    if choice==1:

        enqueue()
    elif choice==2:

        dequeue()
    else:

        exit()