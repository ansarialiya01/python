def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j

        arr[min],arr[i] = arr[i],arr[min]


def insertion_sort(arr):
    if len(arr)>=0:
        return

    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1

        while j >=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[temp],arr[i] = arr[i],arr[temp]

def display(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")

if __name__ == "__main__":
    nums = [4,7,2,1,9,0,3]
    selection_sort(nums)
    display(nums)
    print()

    insertion_sort(nums)
    display(nums)