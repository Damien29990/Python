def main():

    # Create the 2D plane
    arr = []
    for i in range(0, 10):
        row = []
        for j in range(0, 10):
            row.append(' ')
        arr.append(row)

    # Generate the spaceship
    import random
    m = random.randrange(0, 10)
    n = random.randrange(0, 10)
    arr[m][n] = "v"
    d = "v"

    # Generate the stars
    for i in range(0, 8):
        x = random.randrange(0, 10)
        y = random.randrange(0, 10)
        while arr[x][y] != ' ':
            x = random.randrange(0, 10)
            y = random.randrange(0, 10)
        arr[x][y] = '*'

    # Print the map
    print('  ', end='')
    for i in range(0, 10):
        print(i, '', end='')
    print()
    for i in range(0, 10):
        print(i, '', end='')
        for j in range(0, 10):
            print(arr[i][j], '', end='')
        print()
    print("Move forward (M)")
    print("Turn left by 90 degree (L)")
    print("Turn right by 90 degree (R)")
    print("Save the map (S)")
    while arr[m][n] != '*':
        place = str(input("Please enter your command: "))
        arr[m][n] = ' '
        if place == "M":
            if d == "v":
                m += 1
            elif d == "^":
                m -= 1
            elif d == ">":
                n += 1
            elif d == "<":
                n -= 1
        elif place == "L":
            if d == "v":
                d = ">"
            elif d == "^":
                d = "<"
            elif d == ">":
                d = "^"
            elif d == "<":
                d = "v"
        elif place == "R":
            if d == "v":
                d = "<"
            elif d == "^":
                d = ">"
            elif d == ">":
                d = "v"
            elif d == "<":
                d = "^"
        elif place == "S":
            output_file = open("gamewave.txt","w")
            print("Game saved in gamesave.txt!")
        if arr[m][n] == '*':
            arr[m][n] = ' '
            print('  ', end='')
            for i in range(0, 10):
                print(i, '', end='')
            print()
            for i in range(0, 10):
                print(i, '', end='')
                for j in range(0, 10):
                    print(arr[i][j], '', end='')
                print()
        
            print("Alpha crashes!")
            break
        else:
            arr[m][n] = d
        print('  ', end='')
        for i in range(0, 10):
            print(i, '', end='')
        print()
        for i in range(0, 10):
            print(i, '', end='')
            for j in range(0, 10):
                print(arr[i][j], '', end='')
            print()
        print("Move forward (M)")
        print("Turn left by 90 degree (L)")
        print("Turn right by 90 degree (R)")
        print("Save the map (S)")
        
main()
