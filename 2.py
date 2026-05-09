import matplotlib.pyplot as plt
import numpy as np
import os
import regex as re

def get_matrix(name):
    with open(name, 'r')  as file:
        mat = []
        for j in file.readlines():
            mat.append(j.strip().split())
        return np.array(mat, dtype=float)

def get_time(name):
    with open(name, 'r')  as file:
        text = [x.strip() for x in file.readlines() if x != '\n']
        num = re.sub(r'Calculation time: ', '', text[-1])
        num = re.sub(r' seconds', '', num)
    return float(num)

n = [200, 400, 800, 1200, 1600, 2000]
t = [1, 2, 4, 8, 16, 20, 22]

f_time={}

for j in t:
    time = []
    for l in n:
        time_file = os.path.join('time', f'Time (num of threads = {j}), size = {l}.out')
        time.append(float(get_time(time_file)))
    f_time[j] = time
    print(*time, sep='\n')


fig, ax = plt.subplots()
x, y = zip(*f_time.items())
for i in range(len(y)):
    ax.plot(n, y[i])
ax.set(xlabel='Matrix Size N', ylabel='Time (s)', title='Execution Time VS Matrix Size')
plt.xticks(np.arange(min(n), max(n)+1, 200))
plt.yticks(np.arange(0, 100+1, 10))
ax.legend(t, title='Number of Threads')
ax.grid(True)
plt.show()

fig, ax = plt.subplots()
for i in range(len(y)-1):
    y1 = []
    for j in range(len(y)):
        y1.append(y[j][i])
    ax.plot(t, y1)
plt.xticks(np.arange(1, 22+1, 1))
ax.set(xlabel = 'Number of Threads', ylabel = 'Time (s)', title='Execution Time VS Number of Threads')
ax.legend(n, title='Matrix Size N')
ax.grid(True)
plt.show()
