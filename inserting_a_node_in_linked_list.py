from main import printLinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeInLinkedList(head, data):
    if head == None:
        return

    node = Node(data)
    node.next = head

    return node


if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head = insertNodeInLinkedList(head, 30)
    printLinkedList(head)
