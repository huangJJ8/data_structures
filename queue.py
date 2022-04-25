class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = list()  # 使用list实现队列

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def enqueue(self, item):
        """往队列中添加一个元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头中取出元素"""
        if self.is_empty():
            return None
        return self.__list.pop(0)
