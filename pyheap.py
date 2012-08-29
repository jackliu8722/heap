'''
Created on 2012-7-9

@author: jackliu
'''
"""
   a min-heap written by python
   python version 2.7.2
"""

class NotImplement(Exception):
    pass

class Heap(object):
    
    def __init__(self):
        self.elements = []
    
    def insert(self,*emlemnt):
        """
          insert element into thr heap,this is interface,
          it must be implemented by subclass
        """
        raise NotImplement
    def top(self):
        """
            return the first emelent
        """
        if len(self.elements)>0:
            return self.elements[0]
        return None
    def push(self,elm):
        """
          insert a element into the heap
        """
        raise NotImplement
    def pop(self):
        """
        not only return the first element but also delete is
        """
        raise NotImplement
    def leftchild(self,index):
        """
        return the index of the left child 
        """
        if index * 2 + 1 < len(self.elements):
            return index *2 +1
        return None
    
    def rightchild(self,index):
        """
        return the index of the right child
        """
        if index * 2 + 2 < len(self.elements):
            return index *2 +2
        return None
    def parent(self,index):
        """
        return current index's parent
        """
        parent = (index -1)/2
        if parent < 0:
            return None
        return parent
    def _up(self,index):
        """
        adjust the element from down to up
        """
        raise NotImplement
    def _down(self,index):
        """
        adjust the element from up to down
        """
        raise NotImplement
    
class MaxHeap(Heap):
    def  __init__(self,*arg):
        Heap.__init__(self)
        for i in range(len(arg)):
            self.push(arg[i])
    def push(self,elm):
        self.elements.append(elm)
        self._up(len(self.elements)-1)
    def _up(self,index):
        elm = self.elements[index]
        parent = self.parent(index)
        while parent is not None:
            
            if self.elements[parent] < elm:
                self.elements[index] = self.elements[parent]
                index = parent
                parent = self.parent(index)
            else:
                break
        self.elements[index] = elm
    def pop(self):
        max = self.top()
        try:
            last = self.elements.pop()
        except:
            last = None
        if max is not None and len(self.elements) > 0:
            self.elements[0] = last
            self._down(0)
        return max
    def _down(self,index):
        while True:
            left = self.leftchild(index)
            right = self.rightchild(index)
            if left is not None and right is not None:
                if self.elements[left] < self.elements[right]:
                    max = right
                else:
                    max = left
            elif left is not None:
                max = left
            elif right is None:
                max = right
            else:
                max = None
            if max is None:
                break
            if self.elements[max] > self.elements[index]:
                temp = self.elements[index]
                self.elements[index] = self.elements[max]
                self.elements[max] = temp
                index = max
            else:
                break
        
def testMaxHeap():
    heap = MaxHeap(5,3,7,9,1,2);
    print heap.elements
    print heap.pop()
    print heap.elements
    print heap.pop()
    print heap.elements
    print heap.pop()
    print heap.elements
    print heap.pop()
    print heap.elements
    print heap.pop()
    print heap.elements
    print heap.pop()
    print heap.elements

if __name__ == '__main__':
    testMaxHeap()