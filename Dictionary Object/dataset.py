class_names = ['jack', 'bob', 'mary', 'jeff', 'ann', 'pierre', 'martha', 'clause', 'pablo', 'susan', 'gustav']

def create_dataset():
    import random
    num_entries = 10000000
    fp = open("data.txt", "w")
    for i in range(num_entries):
        current = random.choice(class_names)
        fp.write(current+"\n")

def read_dataset_list():
    class_counts = []
    for c in class_names:
        class_counts.append(0)
    with open("data.txt", "r") as fp:
        for line in fp:
            line = line.strip()
            if line != "":
                class_counts[class_names.index(line)] += 1
    print(class_counts)

def read_dataset_dict():
    class_counts = {}
    for c in class_names:
        class_counts[c] = 0
    with open("data.txt") as fp:
        for line in fp:
            line = line.strip()
            if line != "":
                class_counts[line] += 1
    print(class_counts)

import time

t0 = time.time()
create_dataset()
t1 = time.time()
print("Create %0.1f \n" % (t1-t0))

t0 = time.time()
read_dataset_list()
t1 = time.time()
print("list %0.1f \n" % (t1-t0))

t0 = time.time()
read_dataset_dict()
t1 = time.time()
print("dictionary %0.1f \n" % (t1-t0))