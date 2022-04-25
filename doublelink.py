class DNode(object):
    """双向链表节点"""

    def __init__(self, item):
        self.item = item
        self.pre = None
        self.next = None


class DoubleLinkList(object):
    """双向链表"""

    def __init__(self):
        self.__head = None
    # 判断是否为空
    def is_empty(self):
        return self.__head is None
    # 计算链表长度
    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count
    # 循环遍历链接
    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next
        print()
    # 添加元素
    def add(self, item):
        node = DNode(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.pre = node
            self.__head = node
    # 添加元素
    def append(self, item):
        if self.is_empty():
            self.append(item)
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            node = DNode(item)
            node.pre = cur
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            cur = self.__head
            index = 0
            while index < pos-1:
                cur = cur.next
                index += 1
            node = DNode(item)
            node.next = cur.next
            node.pre = cur
            cur.next.pre = node
            cur.next = node

    def remove(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                if cur.pre is None:  # 头节点
                    self.__head = cur.next
                else:
                    cur.pre.next = cur.next
                if cur.next is not None:
                    cur.next.pre = cur.pre
                return
            cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
