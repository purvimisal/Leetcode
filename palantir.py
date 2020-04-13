def findHighPoints(mat):
    r,c = len(mat), len(mat[0])
    res = [[0]*c for i in range(r)]
    for i in range(0,r):
        for j in range(0,c):
            flag = []
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if not (k < 0 or l < 0 or k >= r or l >= c or (k == i and l == j)):
                        if mat[i][j] > mat[k][l]:
                            flag.append(1)
                        else:
                            flag.append(0) 

            if len(flag) == sum(flag):
                res[i][j] = 1
    return res
                        
def waterFall(mat):
    r,c = len(mat), len(mat[0])
    res = [[0]*c for i in range(r)]
    highpoints = findHighPoints(mat)
    # print(highpoints)
    visited = [[False]*c for i in range(r)]
    def recurse(i,j,visited):
        for k in range(i-1,i+2):
            for l in range(j-1,j+2):
                if not (k < 0 or l < 0 or k >= r or l >= c or (k == i and l == j)) and not visited[k][l]:
                    if mat[k][l] < mat[i][j]:
                        visited[k][l] = True
                        res[k][l] += 1
                        recurse(k,l,visited)

    for i in range(0,r):
        for j in range(0,c):
            if highpoints[i][j]:
                res[i][j] += 1
                visited = [[False]*c for i in range(r)]
                recurse(i,j, visited)
    return res

def findplateaus(mat):
    r,c = len(mat), len(mat[0])
    res = [[0]*c for i in range(r)]
    for i in range(0,r):
        for j in range(0,c):
            flag = []
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if not (k < 0 or l < 0 or k >= r or l >= c or (k == i and l == j)):
                        if mat[i][j] >= mat[k][l]:
                            flag.append(1)
                        else:
                            flag.append(0) 

            if len(flag) == sum(flag):
                res[i][j] = 1

    return res

def findplateausandpeaks(mat):
    r,c = len(mat), len(mat[0])
    res = findplateaus(mat)
    print(res)

    def helper(i,j):
        for k in range(i-1,i+2):
            for l in range(j-1,j+2):
                if not (k < 0 or l < 0 or k >= r or l >= c or (k == i and l == j)):
                    if mat[k][l] > mat[i][j]:
                        res[k][l] = 0
                        helper(k,l)
                    elif(mat[k][l] == mat[i][j]):
                        if res[k][l]:
                            res[i][j] = 0

    for i in range(0,r):
        for j in range(0,c):
            helper(i,j) 
    return res

    




mat = [[1,2,1,3,4],[1,5,2,2,2],[4,5,1,9,7],[3,5,3,7,6],[4,3,1,7,3]]
mat2 = [[1,1,1,1,1],[1,2,2,2,1],[1,2,3,2,1],[1,2,2,2,1],[1,1,1,1,1],[1,1,1,1,3]]

for i in mat:
    print(i)
print('----------------')
 
# for i in findHighPoints(mat2):
#     print(i)

# print('----------------')

# for i in (waterFall(mat2)):
#     print(i)

for i in findplateausandpeaks(mat):
    print(i)