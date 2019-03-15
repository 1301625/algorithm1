

# permutations 활용하여 비 효율적인 코드
import itertools

def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    result2= list(map(''.join,itertools.permutations(numbers,len(numbers))))
    result2 = list(map(int,sorted(result2)))
    answer=str(result2[-1])
    return answer

numbers = [21,212]
print(solution(numbers))
