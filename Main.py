import random

main_str: str
initial_strings = []
all_strings = []
all_chromosomes = []


class Chromosome:
    def __init__(self, string: str, fitness: int, probability):
        self.string = string
        self.fitness = fitness
        self.probability = probability


def initial_population(string: str):
    length = len(string)
    random_list = []
    tmp_list = [0] * 3 + [1] + [2]
    for i in range(10):
        for j in range(length):
            random_list.append(random.choice(tmp_list))
        initial_strings.append(random_list)
        random_list = []


def check_sequence(string: str):
    my_tuple: tuple
    check = True
    steps_g = 0
    steps_l = 0
    steps_end = 0

    for i in range(len(main_str) - 1):
        if main_str[i + 1] == 'G' and string[i] != 1:
            check = False
            steps_g = i
            break

    for i in range(len(main_str) - 1):
        if main_str[i + 1] == 'L' and string[i] != 2:
            check = False
            steps_l = i
            break

    if check:
        steps_end = len(string)
    else:
        for i in range(len(main_str) - 1):
            if (main_str[len(main_str) - 1 - i] == 'G' and string[len(main_str) - 2 - i] != 1) or (
                    main_str[len(main_str) - 1 - i] == 'L' and string[len(main_str) - 2 - i] != 2):
                steps_end = i

    my_tuple = (check, max(steps_l, steps_g, steps_end))
    return my_tuple


def fitness_function(string: str):
    my_list = []
    score = 0
    win = 5
    mushroom = 0
    additional_score = 0
    my_tuple = check_sequence(string)
    if my_tuple[0]:
        steps = my_tuple[1]
    else:
        steps = my_tuple[1]
        win = 0

    score += my_tuple[1] + win
    for i in range(len(main_str) - 1):
        if main_str[i + 1] == 'M' and string[i] != 1:
            mushroom += 2
        if main_str[i + 1] == 'G' and string[i - 1] == 1:
            additional_score += 1
        # over jump reduces score
        # if i != len(main_str) - 2:
        #     if main_str[i + 1] != 'G' and main_str[i + 2] != 'G' and string[i] == 1:
        # additional_score -= 0.5

    score += mushroom + additional_score
    # my_list.append(score)
    # my_list.append(steps)
    # my_list.append(win)
    # my_list.append(mushroom)
    # my_list.append(additional_score)
    # return my_list
    return score


def give_probability(string: str):
    sum_of_fitness = 0
    for i in range(len(all_strings)):
        sum_of_fitness += fitness_function(all_strings[i])
    return fitness_function(string) / sum_of_fitness


def delete_string():
    avg = 0
    for i in range(len(all_strings)):
        avg += fitness_function(all_strings[i])
    avg /= len(all_strings)
    for i in range(len(all_strings)):
        if fitness_function(all_strings[i]) < avg:
            all_strings.pop(i)


def crossover(string1: str, string2: str):
    pass


# file_name = "level1.txt"
# f = open(file_name, "r")
# main_str = f.readline()

main_str = "____G_ML__G_"
initial_population(main_str)
for k in range(len(initial_strings)):
    all_strings.append(initial_strings[k])

print(initial_strings)
print("[", end="")
for k in range(len(main_str)):
    print(main_str[k], end=", ")
print()
# print(initial_strings[0])
# the_list = fitness_function(initial_strings[0])
# print("Score:", the_list[0], ", Steps:", the_list[1], ", Win:", the_list[2], ", Mushroom:", the_list[3],
#       ", Additional:", the_list[4])

delete_string()
for k in range(len(all_strings)):
    all_chromosomes.append(
        Chromosome(all_strings[k], fitness_function(all_strings[k]), give_probability(all_strings[k])))
