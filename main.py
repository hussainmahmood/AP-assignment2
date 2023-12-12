from LinkedList import LinkedList

def main():
    list = LinkedList()
    print(list)
    print(f"{'-'*40}\n")
    
    ## TASK 1
    print("Task 1")
    print("Adding at top of the linked list")
    list.push(5)
    print(list)
    list.push(10)
    print(list)
    print(f"\n{'-'*40}\n")

    list.push(23)
    list.push(42)
    list.push(1)
    list.push(12)

    ## TASK 2
    print("Task 2")
    print("Updating a node in a of the linked list")
    list.updateNode(7, 15)
    print(list)
    list.push(10)
    print(list)
    print(f"\n{'-'*40}\n")

if __name__=="__main__":
    main()