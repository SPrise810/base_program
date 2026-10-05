def fun1():
    for i in range(15):
        if i == 15:
            print('i have 15')
    else:
        print('i dont have 15')


def fun2():
    fun1()
    for i in range(16):
        if i == 15:
            print('i have 15')
            break


fun2()  # 嵌套调用

# 另外说明：一个py文件就是一个模块
# 多个.py文件放在一个文件夹下，这个文件夹就是一个包 相当于一个lib里的文件夹 eg: cv2....
