def deleteAllOccurrences(arr: List[int], X: int) -> List[int]:
    j=0
    for i in range(0,len(arr)):
        if arr[i] != X:
            arr[j]=arr[i]
            j+=1
    for i in range(j,len(arr)):
        arr[i]=0

    return arr