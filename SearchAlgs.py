from pickle import FALSE, TRUE
import math

# Binary search function on sorted array A, where l & r are left and right indices
def BinarySearch(A, l, r, target, compCount, recCount):
    if (r >= len(A) or l < 0):
        return "Error, given bound(s) out of range"
    if (l>r):
        return -1, compCount, recCount
    mid = (l+r)//2
    if (A[mid] == target):
        compCount +=1
        return mid, compCount, recCount
    elif (A[mid] >= target):
        compCount += 1
        recCount += 1
        return BinarySearch(A, l, mid - 1, target, compCount, recCount)
    else:
        compCount += 1
        recCount+=1
        return BinarySearch(A, mid + 1, r, target, compCount, recCount)

# Trinary Search function
def TrinarySearch(A, l, r, target, compCount, recCount):
    if (r >= len(A) or l < 0) :
        return "Error, given bound(s) out of range"
    if (l>r):
        return -1, compCount, recCount
    leftPivot = l+((r-l)//3)
    rightPivot = r-((r-l)//3)
    if (target == A[leftPivot]):
        compCount += 1
        return leftPivot, compCount, recCount
    elif (target == A[rightPivot]):
        compCount += 1
        return rightPivot, compCount, recCount
    elif (target < A[leftPivot]):
        compCount += 1
        recCount += 1
        return TrinarySearch(A, l, leftPivot - 1, target, compCount, recCount)
    elif (target > A[rightPivot]):
        compCount += 1
        recCount += 1
        return TrinarySearch(A, rightPivot + 1, r, target, compCount, recCount)
    else:
        compCount += 1
        recCount += 1
        return TrinarySearch(A, leftPivot + 1, rightPivot - 1, target, compCount, recCount)

# Sorted list to work with
A = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,34,56,78,90,111,120,121,122,123,124,125]

## Testing Binary Search
print(BinarySearch(A, 0 , len(A), 9, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 125, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 123, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 121, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 111, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 78, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 56, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 34, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 8, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 1, 0, 0))
print(BinarySearch(A, 0 , len(A)-1, 0, 0, 0))
print("------")

## Testing Trinary Search
print(TrinarySearch(A, 0 , len(A), 9, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 125, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 123, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 121, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 111, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 78, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 56, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 34, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 8, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 1, 0, 0))
print(TrinarySearch(A, 0 , len(A)-1, 0, 0, 0))