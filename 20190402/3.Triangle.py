import math
a = float(input("请输入一条边："))
b = float(input("请输入一条边："))
c = float(input("请输入一条边："))
s = (a + b + c)/2.0
if a + b > c and a + c > b and b + c > a:
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("面积为：",area)
else:
    print("无法构成三角形！")