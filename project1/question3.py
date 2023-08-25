def move_one_tall (tall_right_counts, tall_left_counts, steps, right_persons, left_persons, actions):
    left_persons.append (['L'] * tall_left_counts)
    right_persons.append ((['L'] * tall_right_counts) + ['S', 'S'])

    if (len (actions) == 0 or actions[len (actions) - 1] == "Left"):
        actions.append ("Right")
    else:
        actions.append ("Left")
    
    steps[0] = steps[0] + 1
        
    left_persons.append ((['L'] * tall_left_counts) + ['S'])
    right_persons.append ((['L'] * tall_right_counts) + ['S'])

    if (actions[len (actions) - 1] == "Left"):
        actions.append ("Right")
    else:
        actions.append ("Left")
        
    steps[0] = steps[0] + 1

    left_persons.append ((['L'] * (tall_left_counts - 1)) + ['S'])
    right_persons.append ((['L'] * (tall_right_counts + 1)) + ['S'])

    if (actions[len (actions) - 1] == "Left"):
        actions.append ("Right")
    else:
        actions.append ("Left")
    
    steps[0] = steps[0] + 1

    left_persons.append ((['L'] * (tall_left_counts - 1)) + ['S', 'S'])
    right_persons.append (['L'] * (tall_right_counts + 1))

    if (actions[len (actions) - 1] == "Left"):
        actions.append ("Right")
    else:
        actions.append ("Left")
    
    steps[0] = steps[0] + 1


def solve_robots (tall_right_counts, tall_left_counts, steps, right_persons, left_persons, actions):
    if (tall_left_counts == 0):
        left_persons.append ([])
        right_persons.append ((['L'] * tall_right_counts) + ['S', 'S'])

        if (len (actions) == 0 or actions[len (actions) - 1] == "Left"):
            actions.append ("Right")
        else:
            actions.append ("Left")

        steps[0] = steps[0] + 1
    else:
        move_one_tall (tall_right_counts, tall_left_counts, steps, right_persons, left_persons, actions)

        solve_robots (tall_right_counts + 1,  tall_left_counts - 1, steps, right_persons, left_persons, actions)

right_persons = []
left_persons = []
actions = []
steps = [1]
number_of_tall_robots = 2

left_persons.append ((['L'] * number_of_tall_robots) + ['S', 'S'])
right_persons.append ([])

solve_robots (0, number_of_tall_robots, steps, right_persons, left_persons, actions)

print ("Solution: " + str (steps[0] - 1))

for i in range (steps[0]):
    if (i > 0):
        print ("Action:", actions[i - 1])

    print ("State" + str (i + 1) + ":", left_persons[i], end="")
    print (right_persons[i])