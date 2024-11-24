if __name__ == '__main__':
    lengthOfNumbers = int(input())
    arr = map(int, input().split())
    hashSet = set(arr)
    sortedHashSet = sorted(hashSet)
    print(sortedHashSet[-2])
