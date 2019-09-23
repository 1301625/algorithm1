
def merge_sort(a):
    if len(a) > 1:
        mid = len(a)//2
        print(mid)
        left_half = a[:mid]
        print(left_half)
        right_half = a[mid:]
        print(right_half)

        print(merge_sort(left_half))
        print(merge_sort(right_half))

        i,j,k  = 0,0,0
        while i <len(left_half) and j < len(right_half):
            if len(left_half)[i] > len(right_half)[j]:
                a[k]= right_half[j]
                j+=1
            else:
                a[k] = left_half[i]
                i+=1
            k+=1
    return a





if __name__ == '__main__':
    a=[53,13,1,4,3,42,11,8]

    print(merge_sort(a))