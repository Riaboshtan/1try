import random

class List:
    d={}
    for i in range(10):
        d[i]=random.randint(0,100)
    print(d)

    def remove(self):
        for i in range(10):
            m = (max(self.d.keys(), key=lambda k: self.d[k]))
            del self.d[m]
        return 'Finish'

l=List()
print(l.remove())
print('chanck brach switch')




