# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("SP500.csv")

data['Work Day'] = data.index

data.plot(kind='line', x='Work Day', y='SP500')
plt.show()

avg_3 = []
# print(data.at[n, 'SP500'])

for n in range(2, len(data.index)):
    calc = (1 / 3) * (data.at[n, 'SP500'] + data.at[n - 1, 'SP500'] + data.at[n - 2, 'SP500'])
    avg_3.append(calc)
run_avg_3 = pd.DataFrame(avg_3, columns=['Moving Average'])
run_avg_3.index += 2
# run_avg_3.rename(columns = {'0': 'Moving Average'})
run_avg_3['Day'] = run_avg_3.index
print(run_avg_3.head())

run_avg_3.plot(kind='line', x='Day', y='Moving Average')

plt.plot(run_avg_3)


def running_avg_fun(n, data):
    # ex: n = 15
    index_to_subtract = n - 1
    average = []
    for n1 in range(n, len(data.index)):
        # calculate the summation
        summing = 0
        for k in range(0, index_to_subtract + 1):
            summing += data.at[k, 'SP500']

        summing = summing * (1 / n)
        average.append(summing)

    avg_run = pd.DataFrame(average, columnds=['Moving Average'])
    avg_run.index += n
    avg_run['Day'] = avg_run.index
    return avg_run


test1 = running_avg_fun(15, data)
print(test1.head())
# %%

# %%

# %%
