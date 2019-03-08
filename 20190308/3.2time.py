time = 63320    #时间
hour = time//3600  #时
minute = (time - hour * 3600)//60 #分
second = time - hour * 3600 - minute * 60   #秒
print("现在是",hour,"时",minute,"分",second,"秒")