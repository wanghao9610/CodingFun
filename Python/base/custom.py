# class Node(object):
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
#     def __str__(self):
#         return self.item


class SingleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)  # may error
        elif pos > (self.length() - 1):
            self.append(item)  # may error
        else:
            node = Node(item)
            cur = self.__head
            index = 0
            while index < pos - 1:
                index += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.item == item:
                if pre is not None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            pre = cur
            cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


class Stack(object):
    def __init__(self):
        self.__list = list()

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.__list.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__list[self.size() - 1]


class Queue(object):
    def __init__(self):
        self.__list = list()

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.__list.pop(0)


class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None

    def has_value(self, value):
        if self.val == value:
            return True
        else:
            return False
