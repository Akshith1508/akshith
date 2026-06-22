class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head =None
    def mid_end(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new.next = slow.next
        slow.next = new
    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end=' ')
            itr = itr.next
ll = Linkedlist()
ll.mid_end(50)
ll.display()
        