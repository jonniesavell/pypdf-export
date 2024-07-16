USE a python environment. you don't want to mess up your system.
$ python3 -m venv env

problem with stanza's transitive dependencies: it uses Numpy 1
https://endoflife.date/numpy#:%7E:text=NumPy%20stopped%20supporting%20Python%203.7,support%20Python%203.8%20and%20above.

$ pip install numpy==1.26
$ pip install stanza
$ pip install pypdf

$ python main.py
