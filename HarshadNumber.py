

x= 10000
y=x
number_sum =0
while 1:
    if x >= 10000:
        number_sum += x//10000
        x = x % 10000
        break
    if x >= 1000:
        number_sum += x//1000
        x = x % 1000
    if x >= 100:
        number_sum += x//100
        x = x % 100
    if x >= 10:
        number_sum += x//10+int(x%10)
        x = int(x // 10)
    if x < 10:
        break

if y%number_sum == 0:
    print(True)
else:
    print(False)


def Harshad(n):
    sum= 0
    for i in str(n):
        sum += int(i)
        print(sum)
    return False if n%sum else True


Harshad(18)
"""
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 
18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
arr	return
10	true
12	true
11	false
13	false
입출력 예 설명
입출력 예 #1
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

입출력 예 #2
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

입출력 예 #3
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

입출력 예 #4
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.
"""
