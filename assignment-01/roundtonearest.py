def roundToNearest(s: str) -> int:
    n = int (s)
    remainder = n % 10 
    if remainder <5:
        return n-remainder
    elif remainder >5:
        return n +(10 - remainder)
    else:
        return n - remainder