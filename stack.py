class Stack(object):
    """栈"""

    def __init__(self):
        """创建一个新的空栈"""
        self.__list = list()  # 栈底层使用list来实现

    def is_empty(self):
        """判空"""
        return self.__list == []

    def size(self):
        """返回栈中元素个数"""
        return len(self.__list)

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        if self.is_empty():
            return None
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            return None
        return self.__list[self.size()-1]
