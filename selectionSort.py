
def sort(a):
    for i in range(len(a)):
        minpos=i
        for j in range(i+1,len(a)):
            if a[j]<a[minpos] :
                minpos=j

        temp = a[i]
        a[i] = a[minpos]
        a[minpos] = temp
        #print(a)


a = [4,6,2,7,9,8]

sort(a)

print(a)