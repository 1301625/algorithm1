def solution(array,commands):
    answer=[]
    tmp = array
    for i in commands:
        array=array[i[0]-1:i[1]]
        array.sort()
        answer.append(array[i[2]-1])
        array = tmp
    return answer

def solution2(array,commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1],commands))





array = [1,5,2,6,3,7,4]
commnads = []
for i in range(3):
    tmp= []
    i = tmp.append(int(input()))
    j = tmp.append(int(input()))
    k = tmp.append(int(input()))
    commnads.append(tmp)

print(solution2(array,commnads))



