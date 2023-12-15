import sortfunc, searchfunc
from LinkedList import LinkedList

def even_odd(llist):
    temp_llist = LinkedList()
    n = llist.head
    ix = 0
    while n:
        if n.data % 2 != 0:
            temp_llist.push_at_end(n.data)
            llist.remove(ix)
            ix -= 1
        
        ix += 1
        n = n.next
    
    n = temp_llist.head
    while n:
        llist.push_at_end(n.data)
        n = n.next



def main():
    llist = LinkedList()
    print(llist)
    print(f"{'-'*40}\n")
    
    ## TASK 1
    print("Task 1")
    print("Adding at top of the linked list")
    print(llist)
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
    print("Updating a node in a of the linked list")
    print(llist)
    llist.update(3, 13)
    llist.update(9, 4)
    print(llist)
    print(f"\n{'-'*40}\n")

    ## TASK 3
    print("Task 3")
    print("Segregating evens and odds")
    print(llist)
    even_odd(llist)
    print(llist)
    llist = LinkedList()
    llist.push(42)
    llist.push(12)
    llist.push(10)
    print(llist)
    even_odd(llist)
    print(llist)
    llist = LinkedList()
    llist.push(13)
    llist.push(1)
    llist.push(5)
    print(llist)
    even_odd(llist)
    print(llist)
    print(f"\n{'-'*40}\n")

    ## TASK 4 is not clearly defined

    ## TASK 5
    print("Task 5")
    print("Sorting array using merge sort")
    arr = [8, 15, 3, 12, 5, 10, 2, 13, 9, 7, 4, 11, 6, 14]
    print(arr)
    sortfunc.merge(arr)
    print(arr)
    print(f"\n{'-'*40}\n")

    ## TASK 6
    print("Task 6")
    print("Searching value in array using binary search")
    val = int(input("Please input the number: "))
    print(f"Value={val}, Index={searchfunc.binary(arr, val) or 'not found'}")
    print(f"\n{'-'*40}\n")


if __name__=="__main__":
    main()