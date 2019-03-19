def watermelon(n):
    answer=''
    for i in range(n):
        if i%2==0:
            answer+="수"
        else:
            answer+="박"
    return answer
    #return "수박"*(n//2)+ "수"*(n%2)
print(watermelon(3))

'''
문제 설명
길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
입출력 예
n	return
3	수박수
4	수박수박
'''


def solution_seoul(seoul):
    for i in seoul:
        if i is "Kim":
            return "김서방은 {i}에 있다".format(i=seoul.index(i))
    return False

#def solution_seoul(seoul):
#    return "김서방은 {}에 있다".format(seoul.index("Kim"))
print(solution_seoul(["jana","Kim2","asdas","asdsadcxz","Kim"]))

'''
String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, 
solution을 완성하세요. seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한 사항
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
Kim은 반드시 seoul 안에 포함되어 있습니다.
입출력 예
seoul	return
[Jane, Kim]	김서방은 1에 있다'''


def solution(s):
    return True if s.isdigit() and len(s)==(4 or 6) else False
'''
문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
입출력 예
s	return
a234	false
1234'''