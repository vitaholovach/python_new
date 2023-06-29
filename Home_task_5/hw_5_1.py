import os
import random
import pickle

list_tuples = []
for _ in range(1, 100):
    list_tuples.append((random.randint(1, 100), random.randint(1, 100), random.randint(1, 3)))
os.makedirs('./test/data directory')
with open('./test/data directory/data_tuples.txt', 'w+b') as file:
    data_list_tuples = pickle.dumps(list_tuples)
    file.write(data_list_tuples)
