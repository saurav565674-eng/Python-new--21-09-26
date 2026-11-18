def rightShift(arr: list[int], K: int) -> list[int]:
    for i in range (len(arr)-1,-1,-1):
        arr[i]=arr[i-K] if i>= K else 0
    return arr