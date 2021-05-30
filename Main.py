import random

main_str: str
initial_strings = []
all_chromosomes = []


class Chromosome:
    def __init__(self, string: list, fitness: int):
        self.string = string
        self.fitness = fitness


def initial_population(string: str):
    length = len(string)
    random_list = []
    tmp_list = [0] * 3 + [1] + [2]
    for i in range(20):
        for j in range(length):
            random_list.append(random.choice(tmp_list))
        initial_strings.append(random_list.copy())
        random_list.clear()


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
        if i != len(main_str) - 2:
            if main_str[i + 1] != 'G' and main_str[i + 2] != 'G' and string[i] == 1:
                additional_score -= 0.5

    score += mushroom + additional_score
    # my_list.append(score)
    # my_list.append(steps)
    # my_list.append(win)
    # my_list.append(mushroom)
    # my_list.append(additional_score)
    # return my_list
    return score


# def give_probability(string: str):
#     sum_of_fitness = 0
#     for i in range(len(all_strings)):
#         sum_of_fitness += fitness_function(all_strings[i])
#     return fitness_function(string) / sum_of_fitness


def select_delete_string():
    for i in range(len(all_chromosomes) - 1):
        for j in range(len(all_chromosomes) - i - 1):
            if all_chromosomes[j].fitness <= all_chromosomes[j + 1].fitness:
                all_chromosomes[j], all_chromosomes[j + 1] = all_chromosomes[j + 1], all_chromosomes[j]

    # remove from all chromosomes
    for i in range(int(len(all_chromosomes) / 2)):
        all_chromosomes.pop()


def combine_string(string1: str, string2: str):
    list3 = []
    if len(string1) != len(string2):
        print("\n\n|||||Size of lists are not equal||||\n\n")
    for i in range(int(len(string1) / 2)):
        list3.append(string1[i])
    for i in range(int(len(string1) / 2), len(string2)):
        list3.append(string2[i])
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


# file_name = "level1.txt"
# f = open(file_name, "r")
# main_str = f.readline()

main_str = "_G_ML_G_"
initial_population(main_str)
for k in range(len(initial_strings)):
    all_chromosomes.append(
        Chromosome(initial_strings[k], fitness_function(initial_strings[k])))


# for k in range(len(initial_strings)):
#     print("initial: ", initial_strings[k], fitness_function(initial_strings[k]))
# print("[", end="")
# for k in range(len(main_str)):
#     print(main_str[k], end=", ")
# print()

# print(initial_strings[0])
# the_list = fitness_function(initial_strings[0])
# print("Score:", the_list[0], ", Steps:", the_list[1], ", Win:", the_list[2], ", Mushroom:", the_list[3],
#       ", Additional:", the_list[4])


def first_method():
    # delete half of all_chromosome, the chromosomes have low fitness
    select_delete_string()
    # save good genes, the genes have higher fitness than average
    good_gene = save_good_gene()
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


"""
first method:
    initial population: 200
    fitness: consider win
    selection: half of the best
    crossover: divide each string into 2 part
    mutation: 0.2
"""
for k in range(10):
    if len(all_chromosomes) == 0:
        print("No Chromosomes")
        break
    print("---------------------")
    first_method()
    avg = 0
    for z in range(len(all_chromosomes)):
        avg += all_chromosomes[z].fitness

    avg = avg / len(all_chromosomes)
    for z in all_chromosomes:
        print(z.string, z.fitness)
    print("avg: ", avg)

"""
first method:
    initial population: 500
    fitness: do not consider win
    selection: weighted random
    crossover: divide each string into 3 part
    mutation: 0.5
"""
for k in range(10):
    if len(all_chromosomes) == 0:
        print("No Chromosomes")
        break
    print("---------------------")
    first_method()
    avg = 0
    for z in range(len(all_chromosomes)):
        avg += all_chromosomes[z].fitness

    avg = avg / len(all_chromosomes)
    for z in all_chromosomes:
        print(z.string, z.fitness)
    print("avg: ", avg)