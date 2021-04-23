def gk():
    for i in range(len(pattern)):
        if pattern[i] =="G":
            # G
            print_g = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or (col == 4 and (row != 1 and row != 2))or (row == 0 or row == 6) and (col > 0 and col < 4) or (
                            row == 3 and (col== 3 or col == 5)):
                        print_g[row][col]="G"
            list.append(print_g)
        elif pattern[i] =="K":
            # K
            print_k = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or (col == 4 and (row != 2 and row != 0 and row != 3 and row != 6 and row != 4)) or (
                            col == 5 and (row != 5 and row != 2 and row != 3 and row != 4 and row != 1)) or (
                            col == 3 and (row != 1 and row != 0 and row != 3 and row != 6 and row != 5)) or (
                            row == 3 and (col > 0 and col < 3)):
                        print_k[row][col] = "K"
            list.append(print_k)

                # A
        elif pattern[i] =="A":
            print_a = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 5) and row != 0 or (row == 0 and (col > 0 and col < 5)) or (
                            row == 3 and (col > 0 and col < 5)):
                        print_a[row][col] = "A"
            list.append(print_a)
        elif pattern[i] =="T":
            print_t = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if row == 0 or col == 3:
                        print_t[row][col] = "T"
            list.append(print_t)
        elif pattern[i] =="U":
            print_u = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 5) or (row == 6 and (col > 0 and col < 5)):
                        print_u[row][col]="U"
            list.append(print_u)
        elif pattern[i] =="P":
            print_p = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or ((row == 0 or row == 3) and (col > 0 and col < 6)) or (
                            col == 5 and (row > 0 and row < 4)):
                        print_p[row][col]="P"
            list.append(print_p)
        elif pattern[i] =="R":
            print_r = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or ((row == 0 or row == 3) and (col > 0 and col < 6)) or (
                            col == 5 and (row > 0 and row < 4)) or (row == 4 and col == 2) or (
                            row == 5 and col == 3) or (row == 6 and col == 4):
                        print_r[row][col]="R"
            list.append(print_r)
        elif pattern[i] =="S":
            print_s = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 6)) or (
                            col == 0 and (row > -1 and row < 4)) or (col == 5 and (row > 2 and row < 7)) or (
                            col == 0 and row == 6):
                        print_s[row][col]="S"
            list.append(print_s)
        elif pattern[i] =="C":
            print_c = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or (row == 0 or row == 6):
                        print_c[row][col]="C"
            list.append(print_c)
        elif pattern[i] =="E":
            print_e = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or (row == 0 or row == 3 or row == 6):
                        print_e[row][col]="E"
            list.append(print_e)
        elif pattern[i] =="F":
            print_f = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or (row == 0 or row == 3):
                        print_f[row][col]="F"
            list.append(print_f)
        elif pattern[i] =="H":
            print_h = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 5) or row == 3:
                        print_h[row][col]="H"
            list.append(print_h)
        elif pattern[i] =="I":
            print_i = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (row == 0 or row == 6) or col == 3:
                        print_i[row][col]="I"
            list.append(print_i)
        elif pattern[i] =="L":
            print_l = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or row == 6:
                        print_l[row][col]="L"
            list.append(print_l)
        elif pattern[i] =="D":
            print_d = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(7):
                    if col == 0 or ((row == 0 or row == 6) and (col > -1 and col < 5)) or (
                            col == 5 and (row > 0 and row < 6)):
                        print_d[row][col]="D"
            list.append(print_d)
        elif pattern[i] =="B":
            print_b = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if col == 0 or (col == 5 and (row != 3 and row != 6 and row != 0)) or (
                            (row == 0 or row == 3 or row == 6) and (col > 0 and col < 5)):
                        print_b[row][col] = "B"
            list.append(print_b)
        elif pattern[i] =="O":
            print_o = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row==0 or row==6)and (col>0and col<5))or ((col==0 or col==5)and (row>0and row<6)):
                        print_o[row][col]="O"
            list.append(print_o)
        elif pattern[i] =="M":
            print_m = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if   (col==0 or col==5 or col==2)or row==0:
                        print_m[row][col]="M"
            list.append(print_m)
        elif pattern[i] =="N":
            print_n = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0 or col==3 or col==5)or(row==0 and (col!=4))or (row==6 and(col!=1and col!=2)):
                        print_n[row][col]="N"
            list.append(print_n)
        elif pattern[i] =="Q":
            print_q = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (((col==0 or col==4)and (row>-1 and row<6)) or (row==0 or row==5)and (col>0and col<5)) or (row==3 and( col!=1 and col!=3and  col!=5)) or (row==4 and(col!=1 and col!=2and col!=5))or (row==6 and (col!=0 and col!=1 and col!=2 and col!=3 and col!=4 )):
                        print_q[row][col]="Q"
            list.append(print_q)
        elif pattern[i] =="X":
            print_x = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0 and (row!=2and row!=3and row!=4 and row!=1)) or (col==1 and (row!=0 and row!=3and row!=2and row!=6and row!=5))or (col==2 and (row!=1 and row!=0and row!=4and row!=6and row!=5))or (col==3 and (row!=1 and row!=0and row!=4and row!=6and row!=5))or (col==4 and (row!=2 and row!=0and row!=3and row!=6and row!=5))or (col==5 and ( row!=1and row!=2and row!=3and row!=4)):
                        print_x[row][col]="X"
            list.append(print_x)
        elif pattern[i] =="Z":
            print_z = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (row == 0 or row == 6) or (
                            row == 1 and (col != 0 and col != 1 and col != 2 and col != 3 and col != 4)) or (
                            row == 2 and (col != 0 and col != 1 and col != 2 and col != 3 and col != 5)) or (
                            row == 3 and (col != 0 and col != 1 and col != 2 and col != 5 and col != 4)) or (
                            row == 4 and (col != 0 and col != 1 and col != 5 and col != 3 and col != 4)) or (
                            row == 5 and (col != 0 and col != 5 and col != 2 and col != 3 and col != 4)):
                        print_z[row][col]="Z"
            list.append(print_z)
        elif pattern[i] =="J":
            print_j = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (row == 0 or col == 3) or (row == 6 and (col != 5 and col != 4 and col != 6)) or (
                            col == 0 and (row != 1 and row != 2 and row != 3)):
                        print_j[row][col]="J"
            list.append(print_j)
        elif pattern[i] =="V":
            print_v = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col == 0 or col == 5) and (row > -1 and row < 4)) or (
                            row == 4 and (col != 6 and col != 0 and col != 2 and col != 3 and col != 4)) or (
                            row == 5 and (col != 6 and col != 0 and col != 1 and col != 3 and col != 5)) or (
                            row == 6 and (col != 6 and col != 0 and col != 2 and col != 1 and col != 5 and col != 4)):
                        print_v[row][col]="V"
            list.append(print_v)
        elif pattern[i] =="Y":
            print_y = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(7):
                    if (col==3 and (row>2and row<7))or(row==0 and(col!=1and col!=2and col!=3and col!=4))or(row==1and(col!=0and  col!=2and col!=3and col!=4))or(row==2 and(col!=1and col!=5and col!=0)):
                        print_y[row][col]="Y"
            list.append(print_y)
        elif pattern[i] =="W":
            print_w = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 2 or col == 5) or row == 6:
                        print_w[row][col]="W"
            list.append(print_w)
        else:
            print("INVALID INPUT")

    return list
print("PATTERN PRINTING OF ANY WORD MADE BY GK")
print("IMPORTANT !! ONLY CAPITAL WORDS CAN BE PRINTED")
pattern = input("enter any name:\n")
list = []
list2 = gk()
for i in range(7):
    for j in range(len(list2)):
        for k in range(6):
            print(list2[j][i][k], end=" ")
        print(end=" ")
    print()
