class GeneratorIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self.generator()
        
    def generator(self):
        for i in range(self.start, self.end):
            yield i
            
iterable = GeneratorIterable(1, 5)
for x in iterable:
    print(x)