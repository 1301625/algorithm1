

# permutations 활용하여 비 효율적인 코드
import itertools

def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    result2= list(map(''.join,itertools.permutations(numbers,len(numbers))))
    result2 = list(map(int,sorted(result2)))
    answer=str(result2[-1])
    return answer

def perm(a): # permutation을 얻어내기 위한 함수를 정의한다. 인수로는 나열해야할 숫자들을 리스트로 받는다.
    length=len(a) # 나열해야할 리스트의 길이(개수)를 계산한다.
    if length==1: # 만약 나열해야할 리스트에 원소가 1개 밖에 없다면 그냥 인수로 받았던 리스트를 반환한다.
        return [a]
    else:
        result=[]
        for i in a:
            b=a.copy()
            b.remove(i)
            b.sort()
            for j in perm(b):
                j.insert(0,i)
                if j not in result:
                    result.append(i)
    return result



numbers = [3,88,66]
print(solution(numbers))
print(perm(numbers))
