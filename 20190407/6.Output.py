x = float(input("请输入x的值："))
y = float(input("请输入y的值："))
z = float(input("请输入z的值："))
sum = int(x**2 + y**2 + z**2)

if sum > 1000:
    print(sum//1000)
else:
    print(sum%10+sum//10%10+sum//100)