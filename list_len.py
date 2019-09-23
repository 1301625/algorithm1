import itertools
import collections

def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer
def two_times(x):
    return x*2



list1= []

a= [1,2]
b= [2,3]
c= [5,6,7,8,9,10,11,12]
list1.append(a)
list1.append(b)
list1.append(c)

print(list(map(two_times,a)))
print(list(map(lambda a:a*a, a)))


#f,b= map(int,input().split(' '))
print("c:",c)
print("c[:-1]",c[:-1])
print("c[:]",c[:])
print("c[::]:",c[::])
print("c[::-1]:",c[::-1])
print(c[:-3:-1])
print(c[-3::-1])

num= '444'
base = 5
answer =0
for idx,i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx)
    print("idx: ",idx,"i: ",i)
    print(base**idx)

print(int(str(num),base))
print(solution(list1))


s='abc'
n=30
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))
print(s.upper())
print(s.lower())


def solution2(mylist):
    answer = [[],[],[]]
    for i in range(3):
        for j in range(3):
            answer[i].append(mylist[j][i])

    return answer
mylist= [[1,2,3],[4,5,6],[7,8,9] ]
new_list = list(map(list,zip(*mylist)))

print(solution2(mylist))
print(new_list)

def solution3(mylist):
    answer = list(map(int, mylist))
    #for i in mylist:
    #    if type(i) == str:
    #        answer.append(int(i))
    return answer

#f,b= map(str,input().split(' '))
disk= []
#disk.append(f)
#disk.append(b)
#print(solution3(disk))

def list_add(mylist):
        answer = ""
        for i in mylist:
            answer+=i
        return answer
    #return "".join(mylist)
mylist = ['1','100','33']
print(list_add(mylist))
print(map(list_add,mylist))
print(map(lambda a:a[i],mylist))


#n = int(input())
#for i in range(1,n+1):
#    print("*"*i)

def solution4(mylist):
    answer = sum(mylist,[])
    # for i in range(len(mylist)):
    #     for j in range(len(mylist[i])):
    #         answer.append(mylist[i][j])
    return answer

mylist3=[['A', 'B'], ['X', 'Y'], ['1']]
#print(mylist3[1][0].pop())
#solution4(mylist3)
print(solution4(mylist3))

#경우의 수
horses = [4,2,3,6,7]
#races = itertools.permutations(horses,2)
#print(list(itertools.permutations(horses,len(horses))))
#print(list(itertools.chain(horses)))


#알파벳 갯수
#string = input("영어 문자열 입력 : ")
#
# answer= {}
# for i in string:
#     try:
#         answer[i] +=1
#     except KeyError:
#         answer[i] =1
#
# print(collections.Counter(string))
#
# print(answer)
# print(max(answer.keys(),key=(lambda k:answer[k])))


def solution5(mylist):
    answer=[i**2 for i in mylist if i%2==0]
    # answer= []
    # for i in mylist:
    #     if i%2==0:
    #         answer.append(i**2)
    # return answer
print(solution5(horses))

