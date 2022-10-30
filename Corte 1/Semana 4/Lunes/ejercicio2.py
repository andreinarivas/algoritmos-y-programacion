A=[(1,2,3),(4,5,6)]
B=[(-1,0),(0,1),(1,1)]
result=[[0,0],[0,0]]
product=0
for x in range(len(A)):
  for y in range(len(B[0])):
    sum=0
    for z in range(len(B)):
      product=A[x][z]*B[z][y]
      sum+=product
    result[x][y]=sum

print(result)

