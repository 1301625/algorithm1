
def bubblesoft(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list




if __name__ == '__main__':
    a= [6,8,9,1,4,7,2]
    print(bubblesoft(a))
