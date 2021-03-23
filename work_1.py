import itertools

if __name__ == '__main__':
    S = int(input())
    while S < 10**4:
        S = str(S)
        a_iter = itertools.groupby(S, lambda x : x[0])
        print (a_iter)
        break
