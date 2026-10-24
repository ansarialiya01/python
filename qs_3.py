def division_hashing(key,size):
    return key % size

def mid_sqr(key,size):
    sqr = str(key*key)
    mid = len(sqr)//2
    return int(sqr[mid])%size

def linear_probing(key,size):
    table = [-1]*size
    for keys in key:
        i = keys % size
        while table[i] != -1:
            i = (i+1) % size
        table[i] = keys

    print(table)

def saperate_chaining(key,size):
    table = [[-1] for i in range(size)]
    for keys in key:
        index = keys % size
        table[index].append(keys)
    print(table)

if __name__ == "__main__":

    key = [12,43,53,92,55,98,45,36]
    for ele in key:
        index = division_hashing(ele,10)
        print(f"key:{ele}, hash index:{index}")

    for ele in key:
        index = mid_sqr(ele,10)
        print(f"key:{ele}, square:{ele*ele}, hash index:{index}")

    # linear_probing(key,10)

    saperate_chaining(key,10)