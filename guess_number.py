# 產生一個隨機整數 1~100 （不要印出來）
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 “終於猜對了”
# 猜錯的話 要告訴他 比答案大/小
# 印出猜了幾次
# 讓使用者決定隨機數範圍
n1 = input ("隨機數起始值")
n2 = input ("隨機數結束值")
n1 = int(n1)
n2 = int(n2)
import random
r =  random.randint(n1,n2)
print (r)
time = 0
while True :
	num = input ("請猜數字  ： ")
	num = int(num)
	time = time + 1
	if num == r :
		print ("終於猜對了")
		print ("你猜了",time,"次")
		break
	elif num > r :
		
		print ("比答案大")
	else :

		print ("比答案小")
 	    
 			

