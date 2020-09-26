# optimize_pickling

Runtime and space tests for Pickle in Python 3.

Create a virtuel environment:

```sh
python3 -m venv env
source env/bin/activate
pip install numpy
```

Run the tests:

```sh
python test_pickle.py
```

The effect of three parameters is tested:

1) zip method
    - 0: none
    - 1: `gzip`
    - 2: `bz2`
2) pickle protocol
    - 0: lowest (default)
    - 1: highest
3) optimize pickle string
    - 0: none
    - 1: `pickletools.optimize`

The output is saved in `results.csv`.

Results:

| method |  save in s | load in s | size in bytes |
| ------ | ---------: | --------: | ------------: |
| 0-0-0	 |        5.7 |       3.4 |        96889k |
| 0-0-1	 |       50.7 |       1.8 |        71000k |
| 0-1-0	 |        1.3 |       1.1 |        35007k |
| 0-1-1	 |       28.7 |       0.9 |        33007k |
| 1-0-0	 |        8.3 |       3.3 |         7706k |
| 1-0-1	 |       50.7 |       2.0 |          241k |
| 1-1-0	 |        1.4 |       1.1 |          108k |
| 1-1-1	 |       28.8 |       0.9 |          102k |
| 2-0-0	 |       14.8 |       4.9 |         4565k |
| 2-0-1	 |       68.4 |       2.4 |           18k |
| 2-1-0	 |       10.1 |       1.5 |           11k |
| 2-1-1	 |       35.7 |       1.3 |           10k |
