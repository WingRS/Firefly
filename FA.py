import math


class Firefly:
    def __init__(self, pos):
        self.position = [None] * pos
        self.accuracy = 0.0
        self.intensity = 0.0

    def __eq__(self, other):
        if self.accuracy < other.accuracy:
            return -1
        elif self.accuracy > other.accuracy:
            return 1
        else:
            return 0


def function_to_optimize(pos):
    rest = 0.0
    for i in range(0, len(pos)):
        rest += -pos[i] * math.sin(math.sqrt(abs(pos[i])))
    return rest


def error_calc(pos):
    res = function_to_optimize(pos)
    return math.pow((-40 * 418.9829 - res), 2)


def euclidian_distance(x, y):
    distance = 0
    for i in range(0, len(x)):
        distance = math.pow(x[i] - y[i], 2)
    return math.sqrt(distance)


def global_calc(firefly_index, x_variables_quantity, seed, max_generations_count):
    import random
    random.seed(seed)

    min_x_value = -500
    max_x_value = 500

    attractiveness = 1.0
    g = 1.0 # attractiveness absortion
    a = 0.20

    generation = 0
    display_delay = max_generations_count / 10

    import sys
    best_accuracy = sys.float_info.max
    best_positions = [None] * x_variables_quantity

    firefly_swarm = [None] * firefly_index

    for i in range(0, len(firefly_swarm)):
        firefly_swarm[i] = Firefly(x_variables_quantity)
        for k in range(0, x_variables_quantity):
            firefly_swarm[i].position[k] = (max_x_value - min_x_value) * random.random() + min_x_value
        firefly_swarm[i].accuracy = error_calc(firefly_swarm[i].position)
        firefly_swarm[i].intensity = 1 / (firefly_swarm[i].accuracy + 1) # +1 to avoid dividing by zero!
        if firefly_swarm[i].accuracy < best_accuracy:
            best_accuracy = firefly_swarm[i].accuracy
            for k in range(0, x_variables_quantity):
                best_positions[k] = firefly_swarm[i].position[k]

    while generation < max_generations_count:
        if generation % display_delay == 0:
            best_positions_str = ""
            for i in range(len(best_positions)):
                best_positions_str += ",        x" + str(i) + " = " + str(best_positions[i])
            print("generation " + str(int(generation + display_delay)), ":      accuracy = " + str(1 / best_accuracy),
                  best_positions_str, sep="")
        for i in range(0, firefly_index):
            for j in range(0, firefly_index):
                if firefly_swarm[i].intensity < firefly_swarm[j].intensity:
                    r = euclidian_distance(firefly_swarm[i].position, firefly_swarm[j].position)
                    beta = attractiveness * math.exp(-g * (r ** 2))
                    for k in range(0, x_variables_quantity):
                        firefly_swarm[i].position[k] += beta * (
                            firefly_swarm[j].position[k] - firefly_swarm[i].position[k])
                        firefly_swarm[i].position[k] += a * (random.random() - 0.5)
                        # avoiding fireflies going out of the max min borders of our function
                        if firefly_swarm[i].position[k] < min_x_value:
                            firefly_swarm[i].position[k] = (max_x_value - min_x_value) * random.random() + min_x_value
                        if firefly_swarm[i].position[k] > max_x_value:
                            firefly_swarm[i].position[k] = (max_x_value - min_x_value) * random.random() + min_x_value
        firefly_swarm[i].accuracy = error_calc(firefly_swarm[i].position)
        firefly_swarm[i].intensity = 1 / (firefly_swarm[i].accuracy + 1)
        firefly_swarm.sort(key=lambda x: x.accuracy)
        if firefly_swarm[0].accuracy < best_accuracy:
            best_accuracy = firefly_swarm[0].accuracy
            for f in range(0, x_variables_quantity):
                best_positions[f] = firefly_swarm[0].position[f]
        generation += 1
    return best_positions


def give_a_try():
    number_of_fireflies = 60
    x_variables_quantity = 1
    max_quantity_of_generations = 1000
    seed = 0
    print("Number of fireflies: " + str(number_of_fireflies),
          "\nMax generations quantity: " + str(max_quantity_of_generations))
    print("\nStarting firefly algorithm!\n")
    best_position = global_calc(number_of_fireflies, x_variables_quantity, seed, max_quantity_of_generations)
    print("\nEnd of firefly algorithm!")
    print("\nBest position(s):", best_position)
    print("Value of function in best position:", function_to_optimize(best_position), "\n")


give_a_try()
