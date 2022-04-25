"""
深度优先一般用递归，广度优先一般用队列。一般情况下能用递归实现的算法大部分也能用堆栈来实现。
"""
# python表示二叉树节点及实现树的创建
class Node(object):
    """二叉树节点"""
    # 二叉树节点三个属性：值，左子节点，右子节点
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """(满)二叉树"""
    # 二叉树初始化时需要根节点
    def __init__(self):
        self.root = None

    def add(self, item):
        """添加元素"""
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            # 核心思想：将头节点加入至队列，先判断左节点，为空则将节点放置左侧；
            # 若不为空，判断右节点，为空则放置右节点。
            # 若左右都不为空，分别将左右节点加入至队列尾，再取队列首节点继续上面逻辑
            queue = list()
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)  # 注意是取第0个元素，与下面的append相斥
                if cur.lchild is None:
                    cur.lchild = node
                    return
                if cur.rchild is None:
                    cur.rchild = node
                    return
                # 左右都不为空，将左右节点放置队列尾
                queue.append(cur.lchild)
                queue.append(cur.rchild)

    """
    二叉树深度优先遍历根据遍历顺序不同可分为三类：
    先序遍历：先访问根节点，再访问左节点，最后右节点；
    中序遍历：先访问左节点，再访问根节点，最后右节点；
    后续遍历：先访问左节点，再访问右节点，最后根节点，注意左节点永远在右节点前，后续指根节点和右节点的顺序。
    """
    def preorder(self, root):
        """递归实现先序遍历"""
        if root is None:
            return
        print(root.item)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root is None:
            return
        self.inorder(root.lchild)
        print(root.item)
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归实现后续遍历"""
        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.item)

    def breadth_travel(self, root):
        """
        广度优先遍历
        广度优先遍历的核心：从根节点开始，从上到下，从左到右遍历整个树的节点
        """
        if root is None:
            return
        queue = list()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.item)
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)
