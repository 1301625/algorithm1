import string
a= "abc xyz"
b= []
a= list(map(str,a))


for i in a:
    b.append(ord(i)+1)


print(a)
c=''
for i in b:
    c+=chr(i)

print(c)

def solution8(s,n):
    answer = ''
    ab = string.ascii_lowercase
    print(ab)
    a = list(map(str, s))
    b= []
    for i in a:
        if i == 'z':
            i ="`"
        if i == chr(32):
            b.append(chr(32))
        else:
            b.append(ord(i) + n)

    for i in b:
        if i == chr(32):
            answer +=' '
        else:
            answer += chr(i)

    return answer

def solution(s,n):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    s= list(s)
    for i,char in enumerate(s):
        if char in lower:
            position = (lower.index(char)+n) %26
            print("loswer_index", lower.index(char))
            print("postion:",position)
            s[i]= lower[position]
        elif char in upper:
            position = (upper.index(char)+n)
            print("upper:",position)
            s[i]= upper[position]
        else:
            pass
    return ''.join(s)

print("solution:",solution(a,1))

print("나머지:",26%26)

# user_input= int(input())
# for i in range(1, user_input+1):
#     if i%3 == 0:
#         print("X" ,end=" ")
#     else:
#         print(i , end=" ")

