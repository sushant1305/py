if __name__ == '__main__':
    x = int(input("X:"))
    y = int(input("Y:"))
    z = int(input("Z:"))
    n = int(input("n:"))
    newlist = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    print ([[i,j,k] for [i,j,k] in newlist if i+j+k < n])