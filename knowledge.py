from itertools import count
from operator import index


email = ['user.trungio@gmail.com', 'user.lamio@gmail.com','trungopla@outlook.com.vn','trungthitbam@gmail.com']

num = [1 ,5,8,6,7,9,3,9]


#so nho nhat
print(min(num))
#so lon nhat
print(max(num))
#dao + tao list moi
print(list(reversed(num)))
#print(num[::-1])
#sap xep 
print(sorted(num))

#sap xep nguoc
num = [1,5,8,6,7,9,3,9]
num.sort(reverse=True)
print(num)
#xoa phan tu thu 3
print(num.pop(2)) 
#print(num.remove(2))
#del num[2]
print(num[::-1])

num1 = [1,5,8,6,7,9,3,9]
#cat lay 1,5
print(num1[:2])
#dem so phan tu trong list
#print(len(num1))
print(count(num1))

