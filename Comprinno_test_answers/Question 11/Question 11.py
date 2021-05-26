for T in range(int(input())):
    N=input()
    if N=="b" or N=="B":
        print("BattleShip")
        #Since class id can be either "b" or "B" for the ship class Battleship
    elif N=="c" or N=="C":
        print("Cruiser")
        #Since class id can be either "c" or "C" for the ship class Cruiser
    elif N=="d" or N=="D":
        print("Destroyer")
        #Since class id can be either "d" or "D" for the ship class Destroyer
    elif N=="f" or N=="F":
        print("Frigate")
        #Since class id can be either "f" or "F" for the ship class Frigate
