class Node:
    '''单链表节点'''
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linkedlist:
    '''单链表'''
    def __init__(self):
        self.head = None
        self._size = 0

    def is_empty(self):
        '''判断链表是否为空'''
        return self.head is None

    def __len__(self):
        '''支持len操作'''
        return self._size

    def add_first(self, data):
        '''头部插入: O(1)'''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def add_last(self, data):
        '''尾部插入: O(n)'''
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self._size += 1

    def insert_at(self, data, index = -1):
        '''插入元素: O(n)'''
        if index < 0 or index > self._size:
            raise IndexError('索引越界')
        if index == 0:
            self.add_first(data)
            return
        if index == self._size:
            self.add_last(data)
            return
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        new_node = Node(data)
        new_node.next = cur.next
        cur.next = new_node
        self._size += 1

    def remove_at(self, index):
        '''删除元素: O(n)'''
        if index < 0 and index > self._size:
            raise IndexError('索引越界')
        if index == 0:
            self.remove_first()
            return 
        if index == self._size:
            self.remove_last()
            return 
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        pre = cur
        cur = cur.next
        re = cur.data
        pre.next = cur.next
        self._size -= 1
        return re
        
        

    def remove_first(self):
        '''删除头部元素: O(1)'''
        if self._size == 0:
            raise Exception('空链表')
        cur = self.head
        re = cur.data
        self.head = cur.next
        self._size -= 1
        return re    

    def remove_last(self):
        '''删除尾部元素: O(n)'''
        if self._size == 0:
            raise Exception('空链表')
        if self.size == 1:
            self.remove_first()
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        re = cur.next.data
        cur.next = None
        self._size -= 1
        return re
    
    def remove_value(self, data):
        '''删除第一个值为value的节点，成功返回True,否则返回False'''
        if self._size == 0:
            raise Exception('空链表')
        if self.head.data == data:
            self.remove_first()
            return True
        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                self._size -= 1
                return True
            cur = cur.next
        return False
    
    def find(self, data):
        '''查找第一个值为value的节点索引，找到返回节点，找不到返回-1'''
        if self._size == 0:
            raise Exception('空链表')
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return -1
    

    def get(self, index):
        '''获取指定索引处的数据'''
        if self._size == 0:
            raise Exception('空链表')
        if index < 0 and index >= self._size:
            raise IndexError('索引越界')
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.data

    def reverse(self):
        '''反转链表'''
        cur = self.head
        if cur is None or cur.next is None:
            return 
        rev_head = self.reverse(cur.next)
        nxt = cur.next
        nxt.next = cur
        cur.next = None
        return rev_head


    def clear(self):
        '''清空链表'''
        self.head = None
        self._size = 0
    def __str__(self):
        '''便于打印，返回形如 1 -> 2 -> 3 -> 4 -> None 的字符串'''
        if self._size == 0:
            return 'None'
        cur = self.head
        res = ''
        while cur:
            res += f'{cur.data} ->'
            cur = cur.next
        return res + 'None'





