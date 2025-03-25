from queue import PriorityQueue

class Element:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def push_back(self, data):      # add element to the list
        x = Element(data)
        if self.head == None:
            self.head = x
            self.tail = x
        else:
            self.tail.next = x
            self.tail = x
        self.length = self.length + 1
    def show_list(self):        # prints out the list
        tmp = self.head
        if tmp == None:
            print("\nList is empty\n")
            return
        while tmp != None:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print("\n")
    def return_k_element(self, k):    # in this function I use zero-based-indexing
        tmp = self.head
        x = -1
        if tmp == None:
            print("I cant find k element, if list don't have elements")
            return
        while tmp != None:
            x += 1
            if x == k:
                return tmp.data
            tmp = tmp.next
    def search(self, x):    #in this function we return index of searched element, if element doesn't exist function returns -1
        tmp = self.head
        index = 0
        while tmp != None:
            if tmp.data == x:
                return index
            else:
                index += 1
                tmp = tmp.next
        return -1
    def delete_k_element(self, k):  # in this function we delete k element from our list
        index = 0
        if self.head == None:
            return
        if k == 0:
            self.head = self.head.next
            return
        current = self.head
        while index < k-1 and current.next is not None:
            current = current.next
            index += 1
        if current.next is None:
            return
        current.next = current.next.next
    def len(self):      # return list length
        x = 0
        tmp = self.head
        while tmp != None:
            x += 1
            tmp = tmp.next
        return x