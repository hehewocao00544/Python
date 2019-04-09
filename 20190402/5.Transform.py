ascii = ord(input("请输入一个大写字母："))
if ascii <=90 and ascii >= 65:
    ascii = ascii + 32
    c = chr(ascii)
    print("小写字母是：",c)
else :
    print("输入的字符不是一个大写字母！")