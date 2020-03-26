pos = -1

def search(list1,n):
    l=0
    u=len(list1)-1

    while l <= u:
        mid = (l+u)//2
        if n == list1[mid]:
            globals()['pos']=mid
            return True
        else:
            if n>list1[mid]:
                l=mid
            else:
                u=mid
    return False




elements = [4,5,6,7,8,9,10]
n=4

if search(elements,n):
    print('Found at index', pos+1)
else:
    print('Not Found')