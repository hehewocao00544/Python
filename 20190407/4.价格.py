x = float(input("输入商品价格："))

if x < 0:
    print("请输入有效的价格！")
else:
    if(x < 1000):
        y = x
    elif (x < 2000):
        y = 0.9*x
    elif (x < 3000):
        y = 0.8*x
    elif (x >= 3000):
        y = 0.7*x
    print("应付",y,"元")