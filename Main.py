import random

main_str: str
all_answer = []


def initial_population(string: str):
    length = len(string)
    random_list = []
    tmp_list = [0] * 3 + [1] + [2]
    for i in range(10):
        for j in range(length):
            random_list.append(random.choice(tmp_list))
        all_answer.append(random_list)
        random_list = []


def fitness_function(string: str):
    score = 0
    steps = 1
    win = 5
    mushroom = 2




file_name = "level1.txt"
f = open(file_name, "r")
main_str = f.readline()
initial_population(main_str)
print(all_answer)
