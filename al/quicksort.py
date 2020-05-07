import random

class sortnum:
    def __init__(self,t,n):
        self.num = [0 for i in range(n)]
        self.order = [i for i in range(n)]
        # a= [random.sample(range(0,100000,1),100000)]
        if n>1000:
            for i in range(n):
                self.num[i]=random.randint(0,1000000-n*0.01*t)
        else:
            for i in range(n):
                self.num[i]=random.randint(0,n)
    def change(self,x,y):
        temp1 = self.num[y]
        temp2 = self.order[y]
        self.num[y] = self.num[x]
        self.order[y] = self.order[x]
        self.num[x] = temp1
        self.order[x] = temp2

    def Rand_Partion(self , start , end):
        i = random.randint(start,end-1)
        self.change(start,end)
        x = self.num[end]
        i = start-1
        for j in range(start,end):
            if self.num[j]<=x:
                i=i+1
                self.change(i,j)
        self.change(i+1,end)
        return i+1


    def QuickSort(self , start , end):
        if start<end :
            q = self.Rand_Partion(start,end)
            self.QuickSort(start,q-1)
            self.QuickSort(q+1,end)

def change(num,x,y):
    temp1 = num[y]
    num[y] = num[x]
    num[x] = temp1

def Rand_Partion(num , start , end):
    i = random.randint(start,end-1)
    change(num,start,end)
    x = num[end]
    i = start-1
    for j in range(start,end):
        if num[j]<=x:
            i=i+1
            change(num,i,j)
    change(num,i+1,end)
    return i+1


def QuickSort(num , start , end):
    if start<end :
        q = Rand_Partion(num,start,end)
        QuickSort(num,start,q-1)
        QuickSort(num,q+1,end)

if __name__ == "__main__":
    import time
    # a = [[0 for i in range(1000000)] for j in range(10)]
    # # a= [random.sample(range(0,100000,1),100000)]
    # for i in range(10):
    #     for j in range(1000000):
    #         a[i][j]=random.randint(0,1000000-10000*i)
    n = 1000000
    a = [sortnum(i,n) for i in range(10)]
    num = []
    for i in range(10):
        # start=time.time()
        # a[i].QuickSort(0,len(a[i].num)-1)
        # end=time.time()
        # print("quicksort",end - start)
        for j in range(n):
            num.append(a[i].num[j])
        start=time.time()
        QuickSort(a[i].num,0,len(a[i].num)-1)
        end=time.time()
        print("a[i]quicksort",end - start)
        start=time.time()
        QuickSort(a[i].num,0,len(a[i].num)-1)
        end=time.time()
        print("quicksort",end - start)
        start=time.time()
        a[i].num.sort()
        end=time.time()
        print("sort:",end - start)