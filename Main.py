import random
import matplotlib.pyplot as plt
import numpy as np

main_str: str
initial_strings = []
all_chromosomes = []


class Chromosome:
    def __init__(self, string: list, fitness: int):
        self.string = string
        self.fitness = fitness


def initial_population(string: str, number_of_chromosomes):
    length = len(string)
    random_list = []
    tmp_list = [0] * 3 + [1] + [2]
    for i in range(number_of_chromosomes):
        for j in range(length):
            random_list.append(random.choice(tmp_list))
        initial_strings.append(random_list.copy())
        random_list.clear()


def check_sequence(string: str):
    my_tuple: tuple
    check = True
    lost_points = []
    for i in range(len(main_str) - 1):
        # it will win string[i] == 1 or (string[i - 1] == 1 and i >= 1)
        if main_str[i + 1] == 'G' and not (string[i] == 1 or (string[i - 1] == 1 and i >= 1)):
            check = False
            break
        if main_str[i + 1] == 'L' and string[i] != 2:
            check = False
            break

    if check:
        steps_end = len(string)
    else:
        for i in range(len(main_str) - 1):
            if ((main_str[i + 1] == 'G') and not (string[i] == 1 or (string[i - 1] == 1 and i >= 1))) or \
                    (main_str[i + 1] == 'L' and string[i] != 2):
                lost_points.append(i)
        for i in range(1, len(lost_points)):
            lost_points[i] -= lost_points[i - 1]
        steps_end = max(lost_points)

    if len(lost_points) == 0:
        lost_points.append(steps_end)
    my_tuple = (check, max(max(lost_points), steps_end))
    return my_tuple


def fitness_function(string: list):
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
    for i in range(len(main_str) - 1):
        if main_str[i + 1] == 'M' and string[i] != 1:
            mushroom += 2
        if main_str[i + 1] == 'G' and string[i - 1] == 1:
            additional_score += 1
        # over jump reduces score
        if i != len(main_str) - 2:
            if main_str[i + 1] != 'G' and main_str[i + 2] != 'G' and string[i] == 1:
                additional_score -= 0.5

    last_jump = 0
    if string[len(string) - 1] == 1:
        last_jump += 1

    score += mushroom + additional_score + steps + last_jump + win
    # print("Score:", score, "steps:", steps, "win", win, "mushroom:", mushroom, "additional:", additional_score)
    return score


def select_delete_string():
    for i in range(len(all_chromosomes) - 1):
        for j in range(len(all_chromosomes) - i - 1):
            if all_chromosomes[j].fitness <= all_chromosomes[j + 1].fitness:
                all_chromosomes[j], all_chromosomes[j + 1] = all_chromosomes[j + 1], all_chromosomes[j]

    # remove from all chromosomes
    for i in range(int(len(all_chromosomes) / 2)):
        all_chromosomes.pop()


def selection_for_second_method():
    all_fitness = []
    for i in all_chromosomes:
        all_fitness.append(i.fitness)
    probabilities = []
    sum_fitness = sum(all_fitness)
    for i in all_chromosomes:
        probabilities.append(int(5000 * i.fitness / sum_fitness))
    # 5000 is good for 500 chromosome
    weighted_probability = []
    for i in range(len(probabilities)):
        for j in range(probabilities[i]):
            weighted_probability.append(all_chromosomes[i])
    random_list = random.sample(range(len(weighted_probability)), int(len(all_chromosomes) / 2))
    # sort in reverse, so that we can easily pop elements without changing index of them
    random_list = sorted(random_list, reverse=True)
    all_chromosomes.clear()
    for i in random_list:
        all_chromosomes.append(weighted_probability.pop(i))


def combine_string(string1: list, string2: list):
    list3 = []
    if len(string1) != len(string2):
        print("\n\n|||||Size of lists are not equal||||\n\n")
    for i in range(int(len(string1) / 2)):
        list3.append(string1[i])
    for i in range(int(len(string1) / 2), len(string2)):
        list3.append(string2[i])
    return list3


def combine_3_part(string1: list, string2: list):
    # list 3 = 1/3 * string1 + 1/3 * string2 + 1/3 * string1
    list3 = []
    if len(string1) != len(string2):
        print("\n\n|||||Size of lists are not equal||||\n\n")
    for i in range(int(len(string1) / 3)):
        list3.append(string1[i])
    for i in range(int(len(string1) / 3), 2 * int(len(string1) / 3)):
        list3.append(string2[i])
    for i in range(2 * int(len(string1) / 3), len(string1)):
        list3.append(string1[i])
    return list3


def save_good_gene():
    good_gene = []
    tmp_list = []
    for i in range(len(all_chromosomes)):
        tmp_list.append(all_chromosomes[i].fitness)
    average = sum(tmp_list) / len(tmp_list)
    for i in all_chromosomes:
        if i.fitness >= average:
            good_gene.append(i)
    return list(dict.fromkeys(good_gene))


def mutation(string: list):
    random_index = random.randint(0, len(string) - 1)

    if string[random_index] == 0:
        tmp = 1
    else:
        tmp = 0
    string[random_index] = tmp
    return string


def first_method():
    # delete half of all_chromosome, the chromosomes have low fitness
    good_gene = save_good_gene()
    # save good genes, the genes have higher fitness than average
    select_delete_string()

    random_list = random.sample(range(int(len(all_chromosomes) / 2)), int(len(all_chromosomes) / 2))
    combined_string = []
    # combine random chromosomes
    for i in range(len(random_list)):
        combined_string.append(combine_string(all_chromosomes[random_list[i]].string,
                                              all_chromosomes[len(all_chromosomes) - 1 - random_list[i]].string))
    all_chromosomes.clear()
    for i in range(len(combined_string)):
        all_chromosomes.append(
            Chromosome(combined_string[i], fitness_function(combined_string[i])))
    for i in range(len(good_gene)):
        all_chromosomes.append(good_gene[i])
    # mutation
    mutation_number = 0.1
    number = int(len(all_chromosomes) * mutation_number)
    for i in range(number):
        tmp_string = mutation(all_chromosomes[i].string)
        all_chromosomes[i] = Chromosome(tmp_string.copy(), fitness_function(tmp_string.copy()))


def second_method():
    # save good genes, the genes have higher fitness than average
    good_gene = save_good_gene()
    # delete half of chromosomes randomly(weighted)
    selection_for_second_method()
    random_list = random.sample(range(int(len(all_chromosomes) / 2)), int(len(all_chromosomes) / 2))
    combined_string = []
    # combine random chromosomes
    for i in range(len(random_list)):
        combined_string.append(combine_3_part(all_chromosomes[random_list[i]].string,
                                              all_chromosomes[len(all_chromosomes) - 1 - random_list[i]].string))
    all_chromosomes.clear()
    for i in range(len(combined_string)):
        all_chromosomes.append(
            Chromosome(combined_string[i], fitness_function(combined_string[i])))
    for i in range(len(good_gene)):
        all_chromosomes.append(good_gene[i])
    # mutation
    mutation_number = 0.5
    number = int(len(all_chromosomes) * mutation_number)
    for i in range(number):
        tmp_string = mutation(all_chromosomes[i].string)
        all_chromosomes[i] = Chromosome(tmp_string.copy(), fitness_function(tmp_string.copy()))


def draw(y1: list, y2: list, y3: list):
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(122)
    ax3 = fig.add_subplot(223)

    ax1.title.set_text('Max fitness')
    ax2.title.set_text('Average fitness')
    ax3.title.set_text('Min fitness')

    ax1.set_ylim([0, 20])
    ax2.set_ylim([0, 20])
    ax3.set_ylim([0, 20])

    tmp_list = list(range(0, 21, 2))
    ax1.set_xticks(tmp_list)
    ax2.set_xticks(tmp_list)
    ax3.set_xticks(tmp_list)

    ax1.plot(y1)
    ax2.plot(y2)
    ax3.plot(y3)
    plt.show()
    pass


file_name = "level1.txt"
f = open(file_name, "r")
main_str = f.readline()


command = int(input("first(1) or second(2) method?"))
save_chromosomes = []
"""
first method:
    initial population: 200
    fitness: consider win
    selection: half of the best
    crossover: divide each string into 2 part
    mutation: 0.2
"""
if command == 1:
    initial_population(main_str, 200)
    for k in range(len(initial_strings)):
        all_chromosomes.append(
            Chromosome(initial_strings[k], fitness_function(initial_strings[k])))
    for k in range(20):
        if len(all_chromosomes) == 0:
            print("No Chromosomes")
            break
        print("---------------------")
        first_method()
        avg = 0
        for z in range(len(all_chromosomes)):
            avg += all_chromosomes[z].fitness

        avg = avg / len(all_chromosomes)
        # for z in all_chromosomes:
        #     print(z.string, z.fitness)
        print("avg: ", avg)
        save_chromosomes.append(all_chromosomes.copy())
"""
second method:
    initial population: 500
    fitness: do not consider win
    selection: weighted random
    crossover: divide each string into 3 part
    mutation: 0.5
"""
if command == 2:
    initial_population(main_str, 500)
    for k in range(len(initial_strings)):
        all_chromosomes.append(
            Chromosome(initial_strings[k], fitness_function(initial_strings[k])))

    for k in range(20):
        if len(all_chromosomes) == 0:
            print("No Chromosomes")
            break
        print("---------------------")
        second_method()
        avg = 0
        for z in range(len(all_chromosomes)):
            avg += all_chromosomes[z].fitness
        avg = avg / len(all_chromosomes)
        # for z in all_chromosomes:
        #     print(z.string, z.fitness)
        print("avg: ", avg)
        save_chromosomes.append(all_chromosomes.copy())

all_fitness_each_level = []
my_list = []
for k in range(len(save_chromosomes)):
    for j in range(len(save_chromosomes[k])):
        my_list.append(save_chromosomes[k][j].fitness)
    all_fitness_each_level.append(my_list.copy())
    my_list.clear()

avg_fitness = []
max_fitness = []
min_fitness = []
for k in all_fitness_each_level:
    avg_fitness.append(sum(k) / len(k))
    max_fitness.append(max(k))
    min_fitness.append(min(k))

draw(max_fitness, avg_fitness, min_fitness)
