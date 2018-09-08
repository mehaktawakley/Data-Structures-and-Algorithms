"""
Binary search is the most popular Search algorithm.It is efficient and also one of the most commonly used techniques 
that is used to solve problems.
Binary search works only on a sorted set of elements. To use binary search on a collection, the collection must first be sorted.
Binary search looks for a particular item by comparing the middle most item of the collection. If a match occurs, 
then the index of item is returned. If the middle item is greater than the item, then the item is searched in the sub-array 
to the left of the middle item. Otherwise, the item is searched for in the sub-array to the right of the middle item. 
This process continues on the sub-array as well until the size of the subarray reduces to zero.

Time Complexity:
Best Case O(1)
Average Case O(log n)
Worst Case O(log n)
"""

def binarysearch(arr,n):
    l = len(arr) - 1 #getting the length of array
    start,end = 0,l #initializing start and end of array
    mid = (start+end)//2 #finding index of middle element
    while start <= end:
        if arr[mid] == n:
            return mid #if element is found at middle position then middle index will be return
        elif arr[mid] < n:
            start = mid + 1 #if element is greater than element at middle index then element will be searched in sub-array on left of middle element
        elif arr[mid] > n:
            end = mid - 1 #if element is smaller than element at middle index then element will be searchered in sub-array on right of middle element
        mid = (start+end)//2
    return -1 #if element is not found then -1 will be returned

a = [1,2,3,4,5,6,7]
print(binarysearch(a,6)) #it will return 5 as 6 is present at 5th index
print(binarysearch(a,0)) #it will return -1 as 0 is not present in list
