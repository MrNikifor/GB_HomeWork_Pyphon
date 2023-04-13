def expt(a, b):
    if b==0:
        return 1
    return a*expt(a, b-1)
print(expt(4,5))