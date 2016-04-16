#coding:utf-8
import random
my_list=[]
result=[]
flag=0

#运算符枚举函数
def calc(var1,var2,sign):
    global flag
    if sign==1:
        return var1+var2
    elif sign==2:
        return var1-var2
    elif sign==3:
        return var1*var2
    #排除被除数为0的情况
    elif sign==4 and var2!=0:
        #排除无法整除情况
        if var1%var2==0:
            return var1/var2
        else:
            return 999
    else:
        #flag=1
        return 999
        

#运算符显示函数
def show_sign(sign):
    if sign==1:
        return '+'
    if sign==2:
        return '-'
    if sign==3:
        return '*'
    if sign==4:
        return '/'

#24点算法
def point24(list24):
    global flag
    a=list24
    #外部3层循环，枚举各种排列组合
    for i1 in a:
        b=a[:]
        b.remove(i1)
        for i2 in b:
            c=b[:]
            c.remove(i2)
            for i3 in c:
                d=c[:]
                d.remove(i3)
                i4=d[0]
                #内部3层循环，枚举各种运算组合
                for sign1 in range(1,5):
                    for sign2 in range(1,5):
                        for sign3 in range(1,5):
                            flag=0
                            #情况1，顺序运算：((a+b)+c)+d
                            i1,i2,i3,i4=int(i1),int(i2),int(i3),int(i4)
                            if calc(calc(calc(i1,i2,sign1),i3,sign2),i4,sign3)==24:
                                result='(('+str(i1)+str(show_sign(sign1))+str(i2)+')'+str(show_sign(sign2))+str(i3)+')'+str(show_sign(sign3))+str(i4)
                                return result
                            #情况2，变量2、3先计算：(a+(b+c))+d
                            elif calc(calc(i1,calc(i2,i3,sign2),sign1),i4,sign3)==24:
                                result='('+str(i1)+str(show_sign(sign1))+'('+str(i2)+str(show_sign(sign2))+str(i3)+'))'+str(show_sign(sign3))+str(i4)
                                return result
                            #情况3，两边先运算：(a+b)+(c+d)
                            elif calc(calc(i1,i2,sign1),calc(i3,i4,sign3),sign2)==24:
                                result='('+str(i1)+str(show_sign(sign1))+str(i2)+')'+str(show_sign(sign2))+'('+str(i3)+str(show_sign(sign3))+str(i4)+')'
                                return result
                            #情况4，
    #return 'No answer~'
    return '无解'

if __name__ == '__main__':
    #for i in range(1,5):
    #    my_list.append(random.randint(1,10))
    #my_list=[3,6,4,9]
    #print point24(my_list)
    #my_list=[4,5,8,5]
    my_list=[10,2,9,5]
    print point24(my_list)