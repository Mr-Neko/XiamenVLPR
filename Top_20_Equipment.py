import pickle
import numpy as np
import matplotlib.pyplot as plt
f1 = open("MinC2015P20Top.txt", "w")
f2 = open("MinC2016P20Top.txt", "w")
f3 = open("MinE2015P20Top.txt", "w")
f4 = open("MinE2016P20Top.txt", "w")
count = 0
with open("MinC2015P.txt") as f:
    for lines in f:
        if count == 20:
            break
        else:
            f1.write(lines.split("'")[1] + "\n")
            count += 1
count = 0
with open("MinC2016P.txt") as f:
    for lines in f:
        if count == 20:
            break
        else:
            f2.write(lines.split("'")[1] + "\n")
            count += 1
count = 0
with open("MinE2015P.txt") as f:
    for lines in f:
        if count == 20:
            break
        else:
            f3.write(lines.split("'")[1] + "\n")
            count += 1
count = 0
with open("MinE2016P.txt") as f:
    for lines in f:
        if count == 20:
            break
        else:
            f4.write(lines.split("'")[1] + "\n")
            count += 1

f1.close()
f2.close()
f3.close()
f4.close()



