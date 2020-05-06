#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import math
import matplotlib.pyplot as plt

filename = "output"
base = math.sqrt(4)
max_value = 1e12
i = []
x = []
y = []
acc_y = []
for index in range(0, round(math.log(max_value, base))):
    i.append(index)
    x.append(10**index)
    y.append(0)
    acc_y.append(0)

input_file = open(filename, "r")
for line in input_file:
    number = int(re.search(r".*?([0-9]+)$", line).group(1))
    if number == 0:
        number = 1
    number = round(math.log(number, base))
    y[number] += 1
print(y)
acc = 0
for j in range(len(i) - 1, -1, -1):
    acc += y[j]
    acc_y[j] = acc
print(acc_y)
y_log = []
for j in range(len(y)):
    y_log.append(math.log(acc_y[j]+1, base))
print(len(i), len(y_log))
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(i, acc_y)
ax.scatter(i, y)
ax.set_yscale('log')
ax.set_ylim([0.7, max(acc_y)*1.25])
plt.show()
