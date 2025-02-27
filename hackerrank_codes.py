
# Second greatest in given numbers
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)
    arr2 = sorted(arr1)
    print(arr2[-2])
    

#consecutive values has a string
if __name__ == '__main__':
    n = int(input())
    for i in range (1, n+1):
        print(i,end='')
