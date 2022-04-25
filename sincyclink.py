class Node(object):
    """单向链表节点"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkList(object):
    """单向循环链表"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        if self.is_empty():
            return
        while cur.next != self.__head:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item)

    def add(self, item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        while cur.next != self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        cur.next = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.add(item)
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node.next = self.__head
        cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            index = 0
            while index < pos-1:
                cur = cur.next
                index += 1
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        # 要删除的是头节点的话需要知道尾节点，因此先判断是头节点的情况
        if cur.item == item:
            while cur.next != self.__head:
                pre = cur
                cur = cur.next
            # 循环执行完后，cur为尾节点
            if pre is None:  # 只有头节点
                self.__head = None
            else:
                cur.next = self.__head.next
                self.__head = self.__head.next
        else:
            while cur.next != self.__head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:
                pre.next = self.__head

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:
            return True
        return False
