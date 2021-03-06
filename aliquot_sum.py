
def solution6(n): #처음 작성코드
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer +=i
    return answer

def solution7(n): #sum 함수 활용과 list comprehension
    return sum([i for i in range(1,n+1) if n%i==0])

print(solution7(12))

'''
자연수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 자연수입니다.
입출력 예
n	return
12	28
5	6
입출력 예 설명
입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.
'''