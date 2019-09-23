def insertionsort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            while list[i] < list[j]:
                list[i],list[j] = list[j], list[i]
                if list[i]>list[j]:
                    break
    return list


def anthor_insertion_sort(input):

    for idx, valueToInsert in enumerate(input):
        # select the hole position where number is to be inserted
        holePosition = idx

        # check if previous no. is larger than value to be inserted
        while holePosition > 0 and input[holePosition-1] > valueToInsert:
            input[holePosition - 1], input[holePosition] = input[holePosition], input[holePosition-1]
            holePosition = holePosition - 1

    return input

if __name__ == '__main__':
    a= [4,6,1,3,5,2]
    b = [0,5,1,2,8,3,9,4]
    print(insertionsort(b))
    print(anthor_insertion_sort(a))

    k = int(input())
    if k <=100 and k >= 1:
        for i in range(1,k):
            for j in range(k):
                if i>j:
                    print("*", end="")
            print('')