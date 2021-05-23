from node2 import Node2

class Cursor(object):

    def __init__(self):
        self._header = Node2(None)
        self._trailer = Node2(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0

    def hasNext(self):
        if self.isEmpty():
            return False
        return self._current.getNext() != self._trailer

    def hasPrevious(self):
        if self.isEmpty():
            return False
        return self._current.getPrevious() != self._header

    def first(self):
        if self.isEmpty():
            raise AttributeError("Empty list has no first item")
        self._current = self._header.getNext()

    def last(self):
        if self.isEmpty():
            raise AttributeError("Empty list has no last item")
        self._current = self._trailer.getPrevious()

    def next(self):
        if not self.hasNext():
            raise AttributeError('List has no further next item!')
        self._current = self._current.getNext()

    def previous(self):
        if not self.hasPrevious():
            raise AttributeError('List has no further previous item!')
        self._current = self._current.getPrevious()

    def insertAfter(self, item):
        if self.isEmpty():
            n = Node2(item)
            n.setNext(self._trailer)
            self._trailer.setPrevious(n)

            n.setPrevious(self._header)
            self._header.setNext(n)
            self._current = n
            self._size += 1
            return

        n = Node2(item)
        n.setPrevious(self._current)
        n.setNext(self._current.getNext())
        self._current.getNext().setPrevious(n)
        self._current.setNext(n)
        self._current = n
        self._size += 1

        if not self.hasNext():
            self._trailer.setPrevious(n)

    def insertBefore(self, item):
        if self.isEmpty():
            n = Node2(item)
            n.setNext(self._trailer)
            self._trailer.setPrevious(n)

            n.setPrevious(self._header)
            self._header.setNext(n)
            self._current = n
            self._size += 1
            return

        n = Node2(item)
        n.setNext(self._current)
        n.setPrevious(self._current.getPrevious())
        self._current.getPrevious().setNext(n)
        self._current.setPrevious(n)
        self._current = n
        self._size += 1

        if not self.hasPrevious():
            self._header.setNext(n)

    def getCurrent(self):
        if self.isEmpty():
            raise AttributeError("Empty list has no current item")
        return self._current.getData()

    def remove(self):
        if self.isEmpty():
            raise AttributeError("Empty list has no current item")

        removed = self._current
        self._current.getPrevious().setNext(self._current.getNext())

        if self.hasNext():
            self._current.getNext().setPrevious(self._current.getPrevious())
            self._current = self._current.getNext()

        elif self.hasPrevious():
            self._current.getNext().setPrevious(self._current.getPrevious())
            self._current = self._current.getPrevious()

        else:
            self._current.getNext().setPrevious(self._current.getPrevious())
            self._current = None

        self._size -= 1
        removed.setNext(None)
        removed.setPrevious(None)
        removed_value = removed.getData()
        del removed
        return removed_value

    def replace(self, newItemValue):
        if self.isEmpty():
            raise AttributeError("Uderflow! List has no current item")

        self._current.setData(newItemValue)

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __str__(self):
        lst = ''
        counter = self._header.getNext()
        while counter.getData() != None:
            lst += str(counter.getData()) + ' '
            counter = counter.getNext()
        return lst

    def __iter__(self):
        counter = self._header.getNext()
        while counter.getData() != None:
            yield counter.getData()
            counter = counter.getNext()

    def HeaderNode(self):
        return self._header.getNext()

    def TrailerNode(self):
        return self._trailer.getPrevious()

    def getHeader(self):
        return self.HeaderNode().getData()

    def getTrailer(self):
        return self.TrailerNode().getData()