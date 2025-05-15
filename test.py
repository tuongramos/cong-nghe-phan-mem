
"""
Xuất dữ liệu:print(object(s), sep, end=end, file=file, flush=flush)
object(s): đối tượng, dữ liệu được xuất
sep: ngăn cách
end: kết thúc
file: tên tập tin
flush: đẩy dữ liệu

"""
#các lọai print
print(5);print("hello worldworld")
print("tên", "tôi là",sep="-",end=':')
print("tlinh")
print('Tên:{0},Họ:{1}'.format('Linh','lương'))

#Nhập dữ liệu: input(prompt) Prompt: chuỗi thông báo

input("Nhập vào tên của tôi:")
Linh = input("Nhập đầy đủ họ tên:")
print("Linh={0}".format(Linh))

input("Nhập số thứ tự sinh viên:")
LL = input("Linh Lương")
TT = input("Tú Linh")
print("LL={0},TT={1}".format("Linh Lương","Tú Linh"))

"""
Biến: x=... sau đó print ra
Hằng số: import math
         print(math.pi)
"""
a=9
print(a)
b=8
b=5
print(b)

x,y,z= 1,2,3

import math
print(math.pi)

#Cách kiểm tra kiểu dữ liệu của biến (vd: x=5, print(type(x)))
e=2.72
pi="3.14"
text ="Hello!"
print("Kiểu dữ liệu của biến e:", type(e))

#ép kiểu dữ liệu
n=100
m="200"
print(n+int(m))
print(str(n)+m)

a = 12
print(a)
a=9 
print(a)
a=a+1
print(a)

a=1
b=2
print(a==b)
bien = input('Nhap vao gia tri bien:')
print("Bien = ",bien)

a =float(input('nhap vao 1 so:'))
a=a+5
print(a)
print(type(a))

a= 19.5
print(type(a))

#trình bày kiểu string loại 1
chuoi1= "chuc mung nam moi"
chuoi2= 'happy new year'
chuoi3= """happy birthday"""
chuoi4='''happy new year'''

chuoi_moi= chuoi1 + chuoi2
print(chuoi_moi)

print(chuoi1)
print(chuoi2)
print(chuoi3)
print(chuoi4)

a= 4
b= 6
c= a//b
d= a%b
print(a)
print(b)
print(c)
print(d)

a=5
a+=7
print(a)