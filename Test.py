class Node(object):
    """docstring for Node"""

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None

    # end of Class Note

    # get and set data/link function
    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n


class MyLList(object):

    def __init__(self):
        self.head = None

    def count(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def addtail(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next_node):
            last = last.next_node
        last.next_node = new_node

    def delete(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None:
                print("The entered number does not exist within the list!")
                break

            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous == None:
                self.head = current.next_node

            else:
                previous.set_next(current.next_node)

    def printList(self):
        node = self.head
        while node != None:
            print("|", node.data, "|", " -->", end="")
            node = node.next_node

    def reverseUtil(self, curr, prev):
        if curr.next_node is None:
            self.head = curr
            curr.next_node = prev
            return

        next = curr.next_node
        curr.next_node = prev
        self.reverseUtil(next, curr)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)
        node = self.head
        while node != None:
            print("|", node.data, "|", " -->", end="")
            node = node.next_node

    def min_node(self):
        curr = self.head
        if (self.head == None):
            print("The list is empty")
            return 0
        else:
            min = self.head.data
            while (curr != None):
                if (min > curr.data):
                    min = curr.data
                curr = curr.next_node
            return min

    def max_node(self):
        curr = self.head
        if (self.head == None):
            print("The list is empty")
            return 0
        else:
            max = self.head.data
            while (curr != None):
                if (curr.data > max):
                    max = curr.data
                curr = curr.next_node
        return max


while True:
    print("")
    print("+++++++++++++++++++++++++++++++++")
    print("1. Create List")
    print("2. Insert in beginning")
    print("3. Count element in the List")
    print("4. Enter Item to be deleted")
    print("5. Display")
    print("6. Insert at tail")
    print("7. List of element in forwand and reverse")
    print("8. Display min")
    print("9. Display max")
    print("10. Exit")
    print("+++++++++++++++++++++++++++++++++")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        myLList = MyLList()
        print("The linked list has been created.")
        print("")
    elif choice == 2:
        item = int(input("Enter number to add to the list: "))
        myLList.add(item)
    elif choice == 3:
        print("Number of element(s) in the linked list: ", myLList.count())
    elif choice == 4:
        number = int(input("Enter number you want to detele: "))
        myLList.delete(number)
    elif choice == 5:
        print("List of element(s):")
        myLList.printList()
    elif choice == 6:
        item = int(input("Enter number to add to the list: "))
        myLList.addtail(item)
    elif choice == 7:
        print("Forward: ")
        myLList.printList()
        print("\nReverse: ")
        myLList.reverse()
    elif choice == 8:
        print("The node with minimum value is : ", myLList.min_node())
    elif choice == 9:
        print("The node with maximum value is : ", myLList.max_node())
    else:
        break

