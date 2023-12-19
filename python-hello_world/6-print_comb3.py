for A in range(9):
    for B in range(A + 1, 10):
        print("{:d}{:d}".format(A, B), end=", " if A < 8 or B < 9 else "\n")