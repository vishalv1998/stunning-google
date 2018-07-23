a=int(input("A: "))
count_lower=0
count_upper=0
temp=a
while(a>0):
     z=[z for z in list(str(a)) if z not in list('13579')]
     z1=[z for z in list(str(temp)) if z not in list('13579')]
     if len(z)!=len(str(a)):
     	#print("A: ",a)
     	a-=1
     	count_lower+=1
     else:
     	print(a)
     	print(count_lower)
     	break
     if len(z1)!=len(str(temp)):
     	#print("TEMP: ",temp)
     	temp+=1
     	count_upper+=1
     else:
     	print(temp)
     	print(count_upper)
     	break