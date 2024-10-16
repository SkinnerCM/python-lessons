def staircase(num_steps):
    counter = 1

    for i in range(num_steps-1):
        print(counter)
        counter+=1

    for i in range(num_steps):
        print(counter)
        counter-=1   