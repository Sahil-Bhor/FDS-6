
def simple_matrix(array, row, cols):
    arr1 = array
    for i in range(row):
        ls1 = []
        for j in range(cols):
            number = int(input(f"Enter the no({i},{j}): "))
            ls1.append(number)
        arr1.append(ls1)
    return arr1


def sparse_matrix(mat, r, c):
    arr2 = []

    for i in range(r):
        for j in range(c):
            if (mat[i][j] != 0):
                arr2.append([i, j, mat[i][j]])
    return arr2


def addition_sparse(s1, s2):

    add_sparse = []
    for i in range(len(s1)):
        for j in range(len(s2)):

            if (s1[i][0] == s2[j][0]):
                if(s1[i][1] == s2[j][1]):
                    s3 = s1[i][2] + s2[j][2]
                    add_sparse.append([i, j, s3])
                else:
                    if(s1[i][1] < s2[j][1]):
                        add_sparse.append(s1[i])
                    else:
                        add_sparse.append(s2[j])
            else:
                if(s1[i][0] < s2[j][0]):
                    add_sparse.append(s1[i])
                else:
                    add_sparse.append(s2[j])
    return add_sparse

def multiply_sparse(s1,s2):
    
    multi_sparse = []
    for i in range(len(s1)): 
        ls1 = []
        for j in range(len(s2)):
            temp = 0 
            x = 0
            for k in range(len(s2[0])): 
                s3 = s1[i][k] * s2[x][j]
                temp += s3
                x += 1
        
            ls1.append(temp)
        multi_sparse.append(ls1)
    return multi_sparse


if __name__ == '__main__':
    row = int(input("Enter the no of rows: "))
    cols = int(input("Enter the no of cols: "))
    arr1 = []
    arr2 = []

    matrix1 = simple_matrix(arr1, row, cols)
    matrix2 = simple_matrix(arr2, row, cols)
    print("\n1.Regular matrix : ",matrix1)
    print("\n2.Regular matrix : ",matrix2)
    

    sparse1 = sparse_matrix(matrix1, row, cols)
    sparse2 = sparse_matrix(matrix2, row, cols)
    print("\n1.Sparse matrix :", sparse1)
    print("\n2.Sparse matrix :", sparse2)

    srow = len(sparse1)
    scols = len(sparse2)

    addition = addition_sparse(sparse1, sparse2)
    print("\nAddition of sparse matrix : ",addition)

    multi = multiply_sparse(sparse1, sparse2)
    print("\nMultiplication of sparse matrix : ",multi)