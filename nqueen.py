def main():
    n  = int(input ("Enter the number of Queen : "))
    grid = [[0 for _ in range(n)]for _ in range (n)]
    solution = []
    queen(grid,0,n,solution)
    k = 1

    for i in solution:
        print(f"Solution {k}")
        k = k +1
        for j in i:
            print(j)


def queen(grid,col,n,solution):
    if col==n:
        solution.append([row[:] for row in grid])
        return
    
    for i in range(n):
        if(issafe(grid,i,col,n)):
            grid[i][col]=1
            queen(grid,col+1,n,solution)
            grid[i][col]=0


def issafe(grid,row,col,n):
    for i in range(col):
        if grid[row][i] == 1:
            return False
        

    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if grid[i][j]==1:
            return False

    for i,j in zip(range(row,n),range(col,-1,-1)):
        if grid[i][j]==1:
            return False

    return True


if __name__ == '__main__':
    main()

