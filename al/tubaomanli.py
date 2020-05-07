import random
import itertools
import copy
from matplotlib import pyplot as plt

def generate_num(n):
    seq0=[(random.randint(0,100),random.randint(0,100)) for x in range(n)]
    seq0=list(set(seq0))
    return  seq0

#判断pi是否位于pj,pk,p0组成三角形内，返回t1,t2,t3三个变量
def isin(pi,pj,pk,p0):
    x1 = float(p0[0])
    x2 = float(pj[0])
    x3 = float(pi[0])
    x4 = float(pk[0])
    y1 = float(p0[1])
    y2 = float(pj[1])
    y3 = float(pi[1])
    y4 = float(pk[1])

    k_j0=0
    b_j0=0
    k_k0=0
    b_k0=0
    k_jk=0
    b_jk=0
    perpendicular1=False
    perpendicular2 = False
    perpendicular3 = False

    if x2 - x1 == 0:
        t1=(x3-x2)*(x4-x2)
        perpendicular1=True
    else:
        k_j0 = (y2 - y1) / (x2 - x1)
        b_j0 = y1 - k_j0 * x1
        t1 = (k_j0 * x3 - y3 + b_j0) * (k_j0 * x4 - y4 + b_j0)


    if x4 - x1 == 0:
        t2=(x3-x1)*(x2-x1)
        perpendicular2=True
    else:
        k_k0 = (y4 - y1) / (x4 - x1)
        b_k0 = y1 - k_k0 * x1
        t2 = (k_k0 * x3 - y3 + b_k0) * (k_k0 * x2 - y2 + b_k0)


    if x4 - x2 == 0:
        t3=(x3-x2)*(x1-x2)
        perpendicular3 = True
    else:
        k_jk = (y4 - y2) / (x4 - x2)
        b_jk = y2 - k_jk * x2
        t3 = (k_jk * x3 - y3 + b_jk) * (k_jk * x1 - y1 + b_jk)
    if (k_j0 * x4 - y4 + b_j0)==0 and (k_k0 * x2 - y2 + b_k0)==0 and  (k_jk * x1 - y1 + b_jk)==0 :
          t1=-1
    if perpendicular1 and perpendicular2 and perpendicular3:
          t1=-1

    return t1,t2,t3


def force(lis,n):
    if n==3:
        return  lis
    else:
        lis.sort(key=lambda x: x[1])
        p0=lis[0]
        lis_brute=lis[1:]
        temp=[]
        for i in range(len(lis_brute)-2):
            pi=lis_brute[i]
            if i in temp:
                continue
            for j in range(i+1,len(lis_brute) - 1):
                pj=lis_brute[j]
                if j in temp:
                    continue
                for k in range(j + 1, len(lis_brute)):
                    pk=lis_brute[k]

                    if k in temp:
                        continue
                    (it1,it2,it3)=isin(pi,pj,pk,p0)
                    if it1>=0 and it2>=0 and it3>=0:
                        if i not in temp:
                           temp.append(i)  
                    (jt1,jt2,jt3)=isin(pj,pi,pk,p0)
                    if jt1>=0 and jt2>=0 and jt3>=0:

                        if j not in temp:
                           temp.append(j)

                    (kt1, kt2, kt3) = isin(pk, pi, pj, p0)
                    if kt1 >= 0 and kt2 >= 0 and kt3 >= 0:

                        if k not in temp:
                            temp.append(k)
        lislast=[]
        for coor in lis_brute:
            loc = [i for i, x in enumerate(lis_brute) if x == coor]
            for x in loc:
                ploc = x
            if ploc not in temp:
                lislast.append(coor)
        lislast.append(p0)
        lislast.sort()
        # print(lislast)
        # print("\n")
        return  lislast


import math
def compare(p0,p1,p2):
    x1=p1[0]-p0[0]
    y1=p1[1]-p0[1]
    x2=p2[0]-p0[0]
    y2=p2[1]-p0[1]
    return x1*y2-x2*y1

#冒泡排序来比较极角大小，将极角由小到大排序
def bubble_sort(array,p0,temp):
    for i in range(len(array)-1):
        #current_status是用来判断冒泡是否结束
        current_status = False
        for j in range(len(array) - i -1):
            #比较array[j]和array[j+1]的极角大小，如果<0,交换array[j]和array[j+1]
            if compare (p0,array[j],array[j+1])<0:
                array[j], array[j+1] = array[j+1], array[j]
                current_status = True
         #如果array[j]和array[j+1]的极角相等，保留距离p0最远的点，删除另一个点
            elif compare(p0,array[j],array[j+1])==0:
                coordinatej=array[j]
                coordinatej1 = array[j+1]
                disj =math.sqrt(math.pow(coordinatej[0] - p0[0], 2) + math.pow(coordinatej[1] - p0[1], 2))
                disj1=math.sqrt(math.pow(coordinatej1[0] - p0[0], 2) + math.pow(coordinatej1[1] - p0[1], 2))
                #temp 存放要删除的点
                if disj <disj1:
                    if array[j] not in temp:
                        temp.append(array[j])
                else:
                    if array[j+1] not in temp:
                        temp.append(array[j+1])

        if not current_status:
            break
def scan(lis):
    n=len(lis)
    Q = []
    lis_scan=copy.deepcopy(lis)
    #集合按纵坐标排序，找出y最小的点p0
    lis_scan.sort(key=lambda x: x[1])
    p0 = lis_scan[0]
    #除去p0的其余点集合
    lis_scan.remove(p0)
    #temp 存放要删除的点
    temp=[]
    bubble_sort(lis_scan,p0,temp)
    #print lis_scan
    #print temp
    #lis_scan_different存放删除相同极角点后的集合
    lis_scan_different=[]
    for coordinate in lis_scan:
        if coordinate not in temp:
            lis_scan_different.append(coordinate)
    #凸包为空
    if len(lis_scan)==0:
        print ("null")
    #p0,p1,p2压入栈
    Q.append(p0)
    Q.append(lis_scan_different[0])
    Q.append(lis_scan_different[1])
    n=len(lis_scan_different)
    for i in range(2,n):
        control = True
        while control:
            if len(Q)<3:
                break
            #判断topQ是否位于p0,pi,next_to_topQ三点构成的三角形内部
            (t1, t2, t3) = isin(Q[-1], lis_scan_different[i], Q[-2], p0)
            #topQ位于p0,pi,next_to_topQ三点构成的三角形内部，弹出topQ
            if t1 >= 0 and t2 >= 0 and t3 >= 0:
                Q.pop()
            else:
                control=False
        #将pi加入栈
        Q.append(lis_scan_different[i])
    Q.sort()
    # print(Q)
    return  Q
#分治算法
def dealleft(first,final,lis,temp):
    #temp用来标记位于凸包上的点
    max=0
    index=-1
    #处理first到final的上方，得到使first，final，i 三点组成的三角形面积最大的点i
    if first<final:
        for i in range(first,final):
            #获得first，final，i 的坐标
            firstcoordinate=lis[first]
            finalcoordinate=lis[final]
            icoordinate=lis[i]
            firstx=firstcoordinate[0]
            firsty = firstcoordinate[1]
            finalx=finalcoordinate[0]
            finaly = finalcoordinate[1]
            ix=icoordinate[0]
            iy = icoordinate[1]
            #计算first，final，i 三点组成的三角形面积
            triangle_area=firstx * finaly + ix * firsty + finalx * iy - ix * finaly - finalx * firsty - firstx * iy
            if triangle_area>max:
                max=triangle_area
                index=i
    # 处理first到final的下方，得到使first，final，i 三点组成的三角形面积最大的点i
    else:
        for i in range(final,first):
            firstcoordinate = lis[first]
            finalcoordinate = lis[final]
            icoordinate = lis[i]
            firstx = firstcoordinate[0]
            firsty = firstcoordinate[1]
            finalx = finalcoordinate[0]
            finaly = finalcoordinate[1]
            ix = icoordinate[0]
            iy = icoordinate[1]
            triangle_area = firstx * finaly + ix * firsty + finalx * iy - ix * finaly - finalx * firsty - firstx * iy
            if triangle_area > max:
                max = triangle_area
                index = i

    if index!=-1:
        temp[index]=1
        dealleft(first,index,lis,temp)
        dealleft(index,final,lis,temp)
def divide(lis):
    # temp用来标记位于凸包上的点
    temp = {}
    # lis_con_new为凸包集合
    n=len(lis)
    lis_con_new = []
    if n==3:
        return  lis
    for i in range(n):
        temp[i]=0
    lis_con=copy.deepcopy(lis)
    lis_con.sort()
    temp[0]=1
    temp[n-1]=1
    dealleft(0,n-1,lis_con,temp)
    dealleft(n-1,0,lis_con,temp)
    for i in temp:
        if temp[i]==1:
            lis_con_new.append(lis_con[i])
    # print(lis_con_new)
    return  lis_con_new

if __name__ == "__main__":
    import time
    nptime=[]
    npft=[]
    npst=[]
    npdt=[]
    for n in range(1000,6000,1000):
        nptime.append(n)
        lis = generate_num(n)
        start = time.time()
        lastlis = force(lis,n)
        end = time.time()
        npft.append(end-start)
        start = time.time()
        lastlis = scan(lis)
        end = time.time()
        npst.append(end-start)
        start = time.time()
        lastlis = divide(lis)
        end = time.time()
        npdt.append(end-start)
    import seaborn as sns  # 美化图形的一个绘图包
    sns.set_style("whitegrid")  # 设置图形主图
    fig=plt.figure(figsize=(16,9), facecolor='white')
    plt.xlabel('n')
    plt.ylabel('time/s')
    plt.plot(nptime,npft,label = "force")
    plt.plot(nptime,npdt,label = "divide")
    plt.plot(nptime,npst,label = "scan")
    plt.legend(loc='upper left')
    plt.show()