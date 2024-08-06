nrows = 2
ncols = 3
for i in range (1, nrows + 1):
    for j in range (1, ncols + 1):
        print("%d - %d = %d" % (i, j, i - j))