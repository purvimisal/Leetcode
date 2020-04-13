arr = [['.','*','*','.'],
['*','.','*','.'],
['*','.','.','*'],
['*','*','*','*']]

r,c = 4,4

result = [[0]*c for i in range(r)]

visited = [[False]*c for i in range(r)]


def recurse(i,j,visited): 
    if i> 0 and j>0 and i <r and j <c and not visited[i][j] and arr[i][j] == '.':
        visited[i][j] = True
        result[i][j] = 1
        if i -1 >= 0:
            recurse(i-1,j,visited)
        if i+1 < r: 
            recurse(i+1,j,visited)
        if j-1>=0:
            recurse(i,j-1,visited)
        if j+1 < c:
            recurse(i,j+1,visited) 
        


i ,j = r//2, c//2

while(i<r):
    while(j<c):
        if arr[i][j] == '.':
            visited = [[False]*c for i in range(r)]
            recurse(i,j,visited)
            print(result)
        j+=1 
    i+=1

 
i ,j = r//2, c//2

while(i>0):
    while(j>0):
        if arr[i][j] == '.':
            visited = [[False]*c for i in range(r)]
            recurse(i,j,visited)
            print(result)
        j-=1 
    i-=1

for i in arr: print(i)
print('-------')
for i in result: print(i)
print('Result:', sum(sum(result,[])) )

