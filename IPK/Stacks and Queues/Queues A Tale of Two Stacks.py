
class MyQueue(object):
    def __init__(self):
        self.q = []
    
    def peek(self):
        if self.q!=[]:
            return self.q[0]
        else:
            return None
        
    def pop(self):
        p = self.q[0]
        self.q = self.q[1:]
        return p
        
    def put(self, value):
         self.q.append(value)
