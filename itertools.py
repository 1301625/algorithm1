from __future__ import division
import os
import psutil
import random
import time
import itertools


names = ['최용호', '지길정', '진영욱', '김세훈', '오세훈', '김민우']
majors = ['컴퓨터 공학', '국문학', '영문학', '수학', '정치']
process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss / 1024 / 1024

def people_list(num_people):
    result = []
    for i in range(num_people):
        person= {
            'id': i,
            'name' :random.choice(names),
            'major':random.choice(majors),
        }


        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person ={
            'id': i,
            'name':random.choice(names),
            'major':random.choice(majors),
        }
        yield person


def square_number(nums):
    for i in nums:
        yield i*i

def square_list(nums):
    return nums*nums

def my_map(func, arg_list):
    result= []
    for i in arg_list:
        result.append(func(i))
    return result

horses = [1,2,3,4]
races = itertools.permutations(horses,2)
print(races)
pool = ['a','b','c']
print(list(map(''.join,itertools.permutations(pool,2))))


mynums= square_number(horses)
print(next(mynums))
#print(list(itertools.permutations(horses))[:])

t1= time.clock()
#aa= people_generator(10000000)
t2= time.clock()
mem_after = process.memory_info().rss / 1024 / 1024
total_time= t2-t1

print('시작전 메모리 {}MB'.format(mem_before))
print('종료후 메모리 {}MB'.format(mem_after))
print('소요된 시간 : {:.6f}'.format(total_time))

squares = my_map(square_list,horses)
print(squares)


def func_a(k):
    sum = 0
    for i in range(k+1):
        sum += i
        print(sum)
    return sum

sum_to_m = func_a(5)
sum_to_n = func_a(10-1)
answer = sum_to_m-sum_to_n
print(answer)

def solution(*args):
    list =  [args]
    print(list)

solution1 = solution(5,6,7,8,9)



class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song([
    "생일축하",
    "고소",
    '역서'
])

bulls_on_parade = Song(["조개로 가득 찬 주머니 차고",
                        "가족 주위에 모여든 그들"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()




