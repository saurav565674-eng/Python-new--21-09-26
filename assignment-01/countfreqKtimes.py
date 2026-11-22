def countFreq(n: int, k: int) -> list[int]:
    s=str(n)
    res=[]
    for i in range(10):
        if s.count(str(i))>=k:
            res.append(i)
    return res