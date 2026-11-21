def insertZeroAfterEveryElement(arr: List[int] ) -> List[int]:
    new=[]
    for i in arr:
        new.append(i)
        if len(new) == len(arr):
            break
        new.append(0)
        if len(new)==len(arr):
            break
    arr[:]=new
    return arr