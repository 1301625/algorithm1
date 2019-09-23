
a = "try hello world"
b=''
c=''
a = a.split(" ")
s = []

for i in range(len(a)):
    for j in range(len(a[i])):
         if j%2==0 or j==0:
             s.append(a[i][j].upper())
         else:
             s.append(a[i][j].lower())


print("c:",s)
#TypeError: 'str' object does not support item assignment  유형 오류: ‘str’ 유형 객체의 항목에 다른 값을 대입할 수 없다
for i in range(len(a)):
    for j in range(len(a[i])):
        pass



print(a)
f= []
g=''
l = len(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        if j % 2 == 0 or j == 0:
            g+=a[i][j].upper()
        else:
            g += a[i][j].lower()
    if i != l-1:
        g+=' '

    f.append(g)


print(b)
print(c)
print("f:",f)
print(g)