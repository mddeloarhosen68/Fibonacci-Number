#Ex:1
list1 = [0, 1]
for i in range(48):
    list1.append(list1[-1] + list1[-2])

print(list1)
#Ex:2
a = [0,1]
for i in range(0,49):
    b = a[-1] + a[-2]
    a.append(b)
print(a)

#Ex:3
a=0
b=1
print(a)
print(b)
for i in range(0,48):
 c=a+b
 print(c)
 a=b
 b=c


