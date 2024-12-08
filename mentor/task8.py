def th(arr, k):
    arr.sort()
# k დან 1 ელემენტი არის k ელემენტი 0 დან ითვლება ინდქსები
    return arr[k - 1]

arr = [3, 2, 1, 5, 6, 4]
k = 2


print(th(arr,k))
arr = [3, 2, 1, 5, 6, 4]
k = 4
print(th(arr,k))
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(th(arr,k))
arr = [1, 2, 3, 4, 5]
k = 1
print(th(arr,k))
arr = [1, 2, 3, 4, 5]
k = 5
print(th(arr,k))
