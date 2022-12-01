
import os
import time
os.system('cls')
n=3
product=['apple ','banana','Strawberries','Oranges','mango']
cost=[5,20,15,12,14]
mode='1'
repet=1
n=5
buy=[]
num=[]
conf=0

while (mode!=0):
	print("welcom to iti shop")
	print("for owner press [1]")
	print("for customer press [2]")
	print("for exit press [0]")
	mode=int(input("please select option  "))
	os.system('cls')
	o_mode=1
	c_mode=1
	#owner mode
	while ((mode==1)&(o_mode!=0)):
			print("to show product press [1]") 
			print("to add product press [2]") 
			print("to change cost press [3]")
			print("to delete product press [4]")
			print("for exit press [0]")
			o_mode=int(input("please select option: "))
			os.system('cls')
	
			new=1
			while(new):
				new=0
				if(o_mode==2):
					product.append(input("please enter product name: "))
					n=n+1;
					cost.append(int(input("please enter product cost: ")))
					print("to add new product press [1]") 
					print("to previos option press [0]")
					new=int(input("please select option: "))
				os.system('cls')
		
			new=1
			while(new==1):
				new=0
				os.system('cls')
				if (o_mode==1)|(o_mode==3)|(o_mode==4):
					print("our product is ")
					print("id   product          cost")
					for i in range(n):
							print("{:<5}{:<18}{}".format(i+1,product[i],cost[i]))
			

				if(o_mode==3):
					id=int(input("please enter product id: "))
					cost[id-1]=int(input("please enter new product cost: "))
					print("to adjust new price press [1]") 
					print("to last option press [0]")
					new=int(input("please select option: "))

				if(o_mode==4):
					id=int(input("please enter product id: "))
					product.pop(id-1)
					cost.pop(id-1)
					n=n-1
					print("tovremove new product press [1]") 
					print("to previos option press [0]")
					new=int(input("please select option: "))
		
		
		
	#customer mode
	while((mode==2)&(c_mode)):
		os.system('cls')
		print("To show our products press [1]") 
		print("To Buy from our products press [2]") 
		print("back to first menu [0]")
		c_mode=int(input("please select option  "))
		os.system('cls')

		if ((c_mode==1)|(c_mode==2)):
			print("id    product    cost")
			for i in range(n):
				print("{:<5}{:<18}{}".format(i+1,product[i],cost[i]))
			if (c_mode==1):
				print("To Buy from our products press [2]") 
				print("back to first menu [0]")
				c_mode=int(input("please select option  "))
				
	
		if (c_mode==2):
			i=0
			repet=1
			while (repet):
				buy.append(int(input("please choose product id ")))
				if (buy[i]<=n):
					num.append(int(input("please enter number of products ")))
					repet=int(input("to enter new product press [1] and to exit press [0] "))
					i=i+1
				else:
					print("wrong id")
					buy.pop()
			os.system('cls')
			print("your product is")
			for j in range(i):
				print(num[j-1],'number of ',product[buy[j]-1])
			conf=int(input("to confirm and print your bill press[1] to exit press [0]"))
			os.system('cls')
			
		if (conf==1):
			print("your bill is")
			for j in range(i):
				print(num[j],'number of ',product[buy[j]-1],"=",cost[buy[j]-1]*num[j-1],"pound")
			c_mode=int(input("to buy new product press [1] and to exit press [0] "))

			
			
