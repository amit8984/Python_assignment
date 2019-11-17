
class Reverselter:
    def __init__(self, l):
        self.l = l[::-1]
        self.i = 0

    def __next__(self):
        if self.i < len(self.l):
            i = self.i
            self.i += 1
            return self.l[i]
        else:
            raise StopIteration()

    def next(self):
        return self.__next__()


listIter=[3,6,2,9]
reverseIter=Reverselter(listIter)
#out=next(reverseIter)
length=len(listIter)
while(length):
    print(next(reverseIter))
    length=length-1       

