import random
import numpy as np
class sortnum:
    def __init__(self,t,n):
        self.num = [0 for i in range(n)]
        self.order = [i for i in range(n)]
        # a= [random.sample(range(0,100000,1),100000)]
        if n>1000:
            for i in range(n):
                self.num[i]=random.randint(0,1000000-n*10*0.01*t)
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
        self.change(start,i)
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



    def _partition(self, start, end):
        i = random.randint(start, end)
        self.change(start,i)
        x = self.num[start]
        lt = start  # num[start+1...lt] < x
        gt = end + 1  # num[gt...end] > x
        i = start + 1  # num[lt+1...i] == x
        while (i < gt):
            # i==gt时表示已经比较结束
            if (self.num[i] < x):
                self.change(i,lt+1)
                lt += 1
                i += 1
            elif (self.num[i] > x):
                self.change(i,gt-1)
                gt -= 1
            else:  # num[i] == x
                i += 1
        self.change(start,lt)
        return lt, gt


    def _quickSort(self, start, end):
        if start < end:
            lt, gt = self._partition(start, end)
            self._quickSort(start, lt - 1)
            self._quickSort(gt, end)

def change(num,x,y):
    temp1 = num[y]
    num[y] = num[x]
    num[x] = temp1

def Rand_Partion(num , start , end):
    i = random.randint(start,end-1)
    change(num,start,i)
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


def _partition(num, start, end):
    i = random.randint(start, end)
    change(num,start,i)
    x = num[start]
    lt = start  # num[start+1...lt] < x
    gt = end + 1  # num[gt...end] > x
    i = start + 1  # num[lt+1...i] == x
    while (i < gt):
        # i==gt时表示已经比较结束
        if (num[i] < x):
            num[i], num[lt+1] = num[lt+1], num[i]
            lt += 1
            i += 1
        elif (num[i] > x):
            num[i], num[gt-1] = num[gt-1], num[i]
            gt -= 1
        else:  # num[i] == x
            i += 1
    num[start], num[lt] = num[lt], num[start]
    return lt, gt


def _quickSort(num, start, end):
    if start < end:
        lt, gt = _partition(num, start, end)
        _quickSort(num, start, lt - 1)
        _quickSort(num, gt, end)


if __name__ == "__main__":
    import time
    n = 1000000
    a = [sortnum(i,n) for i in range(10)]
    num1 = []
    num2 = []
    num3 = []
    for i in range(10):
        for j in range(n):
            num1.append(a[i].num[j])
            num2.append(a[i].num[j])
            num3.append(a[i].num[j])
        b = np.array(num1)
        # start=time.time()
        # a[i].QuickSort(0,len(a[i].num)-1)
        # end=time.time()
        # print("a[i]quicksort",end - start)

        start=time.time()
        a[i]._quickSort(0,len(a[i].num)-1)
        end=time.time()
        print("a[i]_quicksort",end - start)

        # start=time.time()
        # QuickSort(num1,0,len(num1)-1)
        # end=time.time()
        # print("Quicksort",end - start)

        start=time.time()
        _quickSort(num2,0,len(num2)-1)
        end=time.time()
        print("_quicksort",end - start)


        start=time.time()
        # QuickSort(a[i].num,0,len(a[i].num)-1)
        b.sort(kind='quicksort')
        end=time.time()
        print("quicksort",end - start)

        start=time.time()
        num3.sort()
        end=time.time()
        print("sort:",end - start)
        print("\n")