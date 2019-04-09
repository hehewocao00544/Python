num1 = float(input("输入第一个数："))
t = input("输入运算符：")
num2 = float(input("输入第二个数："))

if t == '+':
    num = num1 + num2
elif t == '-':
    num = num1 - num2
elif t == '*':
    num = num1 * num2
elif t == '/':
    num = num1/num2
else:
    print("请输入四则运算符！")
    exit()
print("The resualt is ",num)