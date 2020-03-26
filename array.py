from array import array

# values = array('i',[1,2,3,4,5,6])
#
# print(values)
#
# for i in range(len(values)):
#     print(values[i])
#
# newArr = array(values.typecode, (a*a for a in values))
#
# for i in range(len(values)):
#     print(newArr[i])

#

# val = int(input('Enter the element to be deleted '))
#
# for i in range(len(arr)):
#     if arr[i] == val:
#         for j in range(i,len(arr)-1):
#             arr[j] = arr[j+1]
#         break
# print(arr)
# j=0
# for i in range(len(arr),1):
#     arr[i] = arr[j]
#     j=j+1
#
# print(arr)

a=array('i',[1,2,3,4])
n=len(a)

print(a)
# x=n-0
# print(a[x])


for i in range(n//2):
    temp = a[i]
    a[i] = a[n-(i+1)]
    a[n-(i+1)] = temp

print(a)