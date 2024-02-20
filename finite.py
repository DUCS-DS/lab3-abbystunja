from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count = 0
    node = lst.head
    while node:
        count += 1
        node = node.next
    return count


def llprint(lst):
    if lst.head is None:
        print("Linked list is empty.")
    else:
        node = lst.head
        while node:
            print(node.val, end=" ")
            node = node.next
        print()


if __name__ == "__main__":
    list=LList()
    append(list, Node(1))
    append(list, Node(2))
    append(list, Node(4))
    append(list, Node(8))
    append(list, Node(16))
    append(list, Node(32))
    append(list, Node(64))
    append(list, Node(128))
    append(list, Node(256))
    append(list, Node(512))
    llprint(list)

from genfinite import lst
print(length(list))
