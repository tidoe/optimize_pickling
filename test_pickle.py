import bz2
import csv
import gzip
import numpy as np
import os
import pickle
import pickletools
import time


# src: https://stackoverflow.com/a/18475192
class Test(object):
    def __init__(self):
        self.x = 3841984789317471348934788731984731749374
        self.y = 'kdjsaflkjda;sjfkdjsf;klsdjakfjdafjdskfl;adsjfl;dasjf;ljfdlf'


def save(obj, xopen, protocol, optimize):
    with xopen('test.pickle', 'wb') as f:
        if optimize:
            f.write(pickletools.optimize(pickle.dumps(obj, protocol=protocol)))
        else:
            pickle.dump(obj, f, protocol=protocol)


def load(xopen):
    with xopen('test.pickle', 'rb') as f:
        return pickle.load(f)


rows = []
for i, xopen in enumerate([open, gzip.open, bz2.open]):
    for protocol in [0, -1]:
        for optimize in [False, True]:
            save_time, load_time, file_size = [], [], []
            for k in range(3):
                obj = [Test() for i in range(1000000)]
                time1 = time.time()
                save(obj, xopen, protocol, optimize)
                time2 = time.time()
                save_time.append(time2-time1)
                time1 = time.time()
                obj = load(xopen)
                time2 = time.time()
                load_time.append(time2-time1)
                file_size.append(os.stat("test.pickle").st_size)
                os.remove("test.pickle")
            save_time = np.median(save_time)
            load_time = np.median(load_time)
            file_size = np.median(file_size)
            method = "-".join([str(i), str(abs(protocol)), str(int(optimize))])
            row = [method, save_time, load_time, file_size]
            rows.append(row)
            print(method)
            print("Save:", save_time)
            print("Load:", load_time)
            print("Size:", file_size)
            print()
with open("results.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["method", "save", "load", "size"])
    for row in rows:
        writer.writerow(row)