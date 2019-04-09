x = float(input("请输入x的值："))
if (x < -4):
    y = x + 9
elif (x < 4):
    y = x**2 + 2*x + 1
else:
    y = 2*x -15
print(y)