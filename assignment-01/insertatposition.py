def  insertAtPosition(arr: list[int], X: int, P: int) -> list[int]:
    for i in range(len(arr)-1,P,-1):
        arr[i]=arr[i-1]
    arr[P]=X
    return arr