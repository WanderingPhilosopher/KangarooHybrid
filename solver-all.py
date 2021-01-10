#!/usr/bin/python

import sys


def comparatora(tame0, wild0):
    A, Ak, B, Bk = [], [], [], []
    with open('check1.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                A.append(a)
                Ak.append(b)
   
    with open('check2.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                B.append(a)
                Bk.append(b)
    
    result = list(set(A) & set(B))
    if len(result) > 0:
        sol_kt = A.index(result[0])
        sol_kw = B.index(result[0])
        d = Ak[sol_kt] - Bk[sol_kw]
        print('\n' + '\n' + 'SOLVED: ' + hex(d) + '\n')
        file = open("KeyFound.txt", 'a')
        file.write("----------------------------------------\n")
        file.write(hex(Ak[sol_kt] - Bk[sol_kw]) + "\n")
        file.write("----------------------------------------\n")
        file.close()
        sys.exit(0)
    else:
        sys.exit(1)

def main():

    s_tame0 = 'check1.txt'
    s_wild0 = 'check2.txt'
    
    
    comparatora(s_tame0, s_wild0)
    

if __name__ == "__main__":
    main()
