time = float(input("请输入员工工时:"))

if time < 60:
    pay = time * 80 - 700
elif time <= 120:
    pay = time * 80
elif time > 120:
    pay = 120 * 80 + (time - 120)*(80*(1+0.15))
print("该员工工资为:",pay,"元")