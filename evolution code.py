from random import randint
import numpy as np
import matplotlib.pyplot as plt

count = 0
count2 = 0
best = 0
space = ""
parent1 = []
parent2 = []
population = []
countc = 0
count_str = []


#  code = int(input("сколько хотите популяций?  "))

b = int(input("сколько хотите индивидов?  "))
d = int(input("длина индивидов  "))
#  while countc != d:
while countc < d:
    for i in range(b):
        c1 = []
        for i in range(d):
            a = randint(0, 1)
            c1.append(a)
        population.append(c1)
    #  print(population, "популяция")
    #  print(space, c1, "\n", c2, "\n", c3, "\n", c4, "\n", c5, "\n", c6)
    #  print(len(population))
    #  if countc == d:
    #    print(child)
    #  else:
    #    continue
    tournament = randint(0, len(population) - 1)
    #  print(tournament)
    fp = population[tournament]
    tournament = randint(0, len(population) - 1)
    #  print(tournament)
    sp = population[tournament]

    #  print(fp, sp, "players")

    for i in fp:
        if i == 1:
            count += 1
    for i in sp:
        if i == 1:
            count2 += 1
            if count > count2:
                parent1 = fp
            elif count == count2:
                parent1 = fp
            else:
                parent1 = sp

    # print(parent1, "РОДИТЕЛЬ 1", "\n", "\n")

    tournament = randint(0, len(population) - 1)
    fp = population[tournament]
    #  print(tournament)
    tournament = randint(0, len(population) - 1)
    sp = population[tournament]
    # print(fp, sp, "\n")
    #  print(tournament)
    for i in fp:
        if i == 1:
            count += 1
    for i in sp:
        if i == 1:
            count2 += 1
            if count > count2:
                parent2 = fp
            elif count == count2:
                parent2 = fp
            else:
                parent2 = sp
    # print(fp, sp, "players2")
    # print(parent2, "РОДИТЕЛЬ 2", "\n", "\n", "\n")

    rand = randint(0, d - 1)
    fh = parent1[:rand]  # first half
    sh = parent2[rand::]  # second half
    child = fh + sh

    #   print(rand, "рандомное число из fh, sh списка", "\n")
    #   print(space, parent1, "родитель 1", "\n", parent2, "родитель 2", "\n", "\n")
    #   print(space, fh, "генотип 1", "\n", sh, "генотип 2", "\n", "\n")
    #  print(child, "ребёнок")

    for i in range(len(child)):
        rand = randint(1, 100)
        if rand == 1:
            child[[i] == 0] = 1
            child[[i] == 1] = 0  # метод замена элементов на основе одного условия
    #  print(rand,"число", "\n")
    #  print(child, "ребенок мутант")

    #  print(population)

    for i in child:
            if i == 1:
                countc += 1
                count_str.append(countc)#  print(countc)
                
    if countc < d:
        countc = 0
    #  print(countc, d)
    population.append(child)
    

    del population[:b]
for ex in range(len(count_str) + 1):
    count_str_x = list(range(1, ex + 1))
#  print(count_str_x, "len str x")
#  print(count_str, "len str")
print(child)


fig, ax = plt.subplots()
x = count_str_x
y = count_str
ax.plot(x, y)
plt.show()
