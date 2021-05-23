import random

main_str: str
all_answer = []


class Chromosome:
    def __init__(self, string: str, fitness: int, probability: int, level: int):
        pass


def initial_population(string: str):
    length = len(string)
    random_list = []
    tmp_list = [0] * 3 + [1] + [2]
    for i in range(10):
        for j in range(length):
            random_list.append(random.choice(tmp_list))
        all_answer.append(random_list)
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
    steps = 0
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
        if i != len(main_str) - 2:
            if main_str[i + 1] != 'G' and main_str[i + 2] != 'G' and string[i] == 1:
                pass
                # additional_score -= 0.5

    score += mushroom + additional_score
    my_list.append(score)
    my_list.append(steps)
    my_list.append(win)
    my_list.append(mushroom)
    my_list.append(additional_score)
    return my_list


# file_name = "level1.txt"
# f = open(file_name, "r")
# main_str = f.readline()
main_str = "____G_ML__G_"
initial_population(main_str)
# print(all_answer)
print("[", end="")
for k in range(len(main_str)):
    print(main_str[k], end=", ")
print()
print(all_answer[0])
the_list = fitness_function(all_answer[0])
print("Score:", the_list[0], ", Steps:", the_list[1], ", Win:", the_list[2], ", Mushroom:", the_list[3],
      ", Additional:", the_list[4])
