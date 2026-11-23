class Solution(object):
    def duplicateZeros(self, arr):
        i=0
        while i < len(arr) - 1:
            if arr[i] == 0:
                for j in range(len(arr) - 1, i + 1, -1):
                    arr[j] = arr[j - 1]
                i += 1  
                arr[i]=0
            i += 1
        return arr

