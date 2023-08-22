class Solution:
    
    def merge(self,arr1, arr2, n, m):
        
        def swap(arr1, arr2, i, j):
            if (arr1[i] > arr2[j]):
                arr1[i], arr2[j] = arr2[j], arr1[i]
        
        length = n + m
        gap = (length // 2) + (length % 2)
        while (gap > 0):
            left = 0
            right = left + gap
            while (right < length):
                if (left < n and right >= n):
                    swap(arr1, arr2, left, right - n)
                elif (left >= n):
                    swap(arr2, arr2, left - n, right - n)
                else:
                    swap(arr1, arr1, left, right)
                left += 1
                right += 1
            if (gap == 1):
                break
            gap = (gap // 2) + (gap % 2)
        return arr1 + arr2
