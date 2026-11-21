def insertZeroAfterEveryElement(arr: list[int] ) -> list[int]:
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