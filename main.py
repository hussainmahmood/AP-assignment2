from LinkedList import LinkedList

def orderEvenOdd(llist):
    


def main():
    llist = LinkedList()
    print(llist)
    print(f"{'-'*40}\n")
    
    ## TASK 1
    print("Task 1")
    print(llist)
    print("Adding at top of the linked list")
    llist.push(5)
    llist.push(10)
    print(llist)
    print(f"\n{'-'*40}\n")

    llist.push(23)
    llist.push(42)
    llist.push(1)
    llist.push(12)

    ## TASK 2
    print("Task 2")
    print(llist)
    print("Updating a node in a of the linked list")
    llist.update(3, 13)
    llist.update(9, 4)
    print(llist)
    print(f"\n{'-'*40}\n")

    ## TASK 3
    print("Task 3")
    print(llist)
    print("Updating a  in a of the linked list")
    llist.update(3, 13)
    llist.update(9, 4)
    print(llist)
    print(f"\n{'-'*40}\n")

if __name__=="__main__":
    main()