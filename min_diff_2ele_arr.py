#find the minimum difference between two elements of array
#i/p=> arr=[5,32,45,4,12,18,25]

# def min_difference(arr):
#     if len(arr) < 2:
#         return None  # Need at least 2 elements

#     arr.sort()
#     min_diff = float('inf')

#     for i in range(len(arr) - 1):
#         diff = abs(arr[i+1] - arr[i])
#         if diff < min_diff:
#             min_diff = diff

#     return min_diff

# # Example
# arr = [5, 32, 45, 4, 12, 18, 25]
# result = min_difference(arr)
# print("Minimum difference:", result)


#another methods
def min_diff_ele(a):
    a=sorted(a)
    size=len(a)
    min_diff=9999*999

    for i in range(size-1):
        if(a[i+1]- a[i] < min_diff):
            min_diff=a[i+1] - a[i]
    return min_diff
a=[2,32,4,35,65,54]
print("minimum difference between element of an array is :",min_diff_ele(a))
