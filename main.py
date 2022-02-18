'''Two arrays
Remove Duplicates arr1=[3,1,2]
Combine both arrays
Sort it
Find the Median or middle element'''
arr1=[3,1,1,2]
arr2=[4,3,3,2,1]
dup1=[]
dup2=[]
for i in arr1:
    if i not in dup1:
        dup1.append(i)
for j in arr2:
    if j not in dup2:
        dup2.append(j)
f=sorted(dup1+dup2)
print(f[len(f)//2])