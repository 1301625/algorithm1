def selection(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

    return list

def another_selection(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                list[i], list[j] = list[j], list[i]

    return list

if __name__ == '__main__':
    a= [4,2,5,1,8,3,9]
    print(selection(a))
    print(another_selection(a))



