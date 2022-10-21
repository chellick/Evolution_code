
# Генетический алгоритм + PSO оптимизация
Задача моего проекта заключается в том, чтобы используя метод генетичской алгоритмизации найти лучшие допустимые значения, а затем, при помощи роевого метода PSO оптимизации отфильтровать полученные решения. 

$$
p_{i}={\frac {1}{N}}(a-(a-b){\frac {i-1}{N-1}})
$$

Метод ранжирования — вероятность выбора зависит от места в списке особей отсортированном по значению функции приспособленности


![пример работы ген. алгоритма](img/%D0%B3%D0%B5%D0%BD%20%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC.png)

```python


from random import randint
import time

count = 0
count2 = 0
best = 0
space = ""
parent1 = []
parent2 = []
population = []
countc = 0
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
    print(population, "популяция")
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
    print(child, "ребёнок")

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
                #  print(countc)
    if countc < d:
        countc = 0
    #  print(countc, d)
    population.append(child)
    del population[:b]
print(child)
exit(10)
```
Генети́ческий алгори́тм  — это эвристический алгоритм поиска, используемый для решения задач оптимизации и моделирования путём случайного подбора, комбинирования и вариации искомых параметров с использованием механизмов, аналогичных естественному отбору в природе. Является разновидностью эволюционных вычислений, с помощью которых решаются оптимизационные задачи с использованием методов естественной эволюции, таких как наследование, мутации, отбор и кроссинговер. Отличительной особенностью генетического алгоритма является акцент на использование оператора «скрещивания», который производит операцию рекомбинации решений-кандидатов, роль которой аналогична роли скрещивания в живой природе.
Используется цикл `while` ,  usage of ``:``