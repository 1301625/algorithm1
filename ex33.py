i = 0
numbers = []

def repeat_while(list):
    i= 0
    while i<len(list):
        numbers.append(list[i])

        i+=1
        print(numbers)
    return numbers



q = [3,7,9,4,2,1]
a = repeat_while(q)

