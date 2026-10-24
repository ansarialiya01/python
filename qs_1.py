def linear_search(array,key):
    for i in range(len(array)):
        if(array[i]==key):
            return True;
        else:
            return False


def merge(arr,si,mid,ei):
    i = si
    j = mid+1
    temp = []

    while i <= mid and j <= ei:
        if(arr[i]<arr[j]):
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1

    while i <= mid:
        temp.append(arr[i])
        i+=1

    while j <= ei:
        temp.append(arr[j])
        j+=1

    for k in range(len(temp)):
        arr[si+k] = temp[k]

def merge_sort(arr,si,ei):
    if si>=ei:
        return

    mid = si+(ei-si)//2
    merge_sort(arr,si,mid)
    merge_sort(arr,mid+1,ei)
    merge(arr,si,mid,ei)





if __name__=="__main__":
    array = [2,4,1,5,6]
    print(linear_search(array,5))
    merge_sort(array,0,len(array)-1)
    print(array)