print("请输入一个三位及三位以上的整数：")
a = int(input())    #用户输入整数
if a//100 != 0:
        b = (a // 100)
        print(b)
else:
    print("数据有误！")