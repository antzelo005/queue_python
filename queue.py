

class Queue:
    def __init__ (self):
        self.array = []
    
    def enqueue(self,elem):
        self.array.append(elem)
        
    def dequeue(self):
        if not self.array:
            return None
        return self.array.pop(0)
    def __str__(self):
        return "\n".join(self.array)
    
    def __add__(self, other):
        result = Queue()
        result.array = self.array.copy()
        if isinstance(other, (int, float, str)):
            result.enqueue(other)
        elif isinstance(other, Queue):
            result.array += other.array
        else:
            return NotImplemented
        return result
            
    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.array += other.array
            return self
        if isinstance(other, (int, float, str)):
            self.enqueue(other)
            return self
        return NotImplemented

    def __neg__ (self):
        return self.dequeue()
            
    def __len__(self):
        return len(self.array)