def fun2():
    for i in range(15):
        if i == 15:
            print('i have 15')
            break
    else:
        print("don't find ",end='')
        print("测试end=空，这样就不会换行了")
        print("for和else可以配对！")

fun2() # range 左闭右开
# range(a,b,c)   c为步长，  ab为范围，左闭右开[a,b)