"""
Problem Statement:
Given a list of n elements with values and target element, find the index/position of the target in list.

The linear search is a basic search algorithm which searches all the elements in the list and finds the required value. 

This is also known as sequential search.

Time Complexity:
Best Case: O(1)
Average Case: O(n)
Worst Case: O(n)
"""

def linearsearch(arr,n):
    for i in range(len(arr)): #traversing the list
        if(arr[i] == n): #comparing the list element with the target element
            return i #returning the index if list element is equal to target element
    return -1 #returning -1 if element not found

a = [1,2,5,7,9,4]
print(linearsearch(a,7)) #it will return 3 as 7 is present at 3rd index
print(linearsearch(a,3)) #it will return -1 as 3 is not present in list
