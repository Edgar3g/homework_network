import sys

print("\t\t\t\tWellcome")
while True:
        
    try:
        options = int(input("Choose a option: \n\n\n\t 1) to Show Jump \t\t 2) to Show All BroadCast\n\n\t 3) to show all Valide IP's \t 4) Show All Sub-Network \n\n\t 0) to exit \n\nYour Choose: "))
    except ValueError:
        print("Coloque uma opção valida.")
        sys.exit(1)


    if options == 1: # Condition of the option !
        print(f"\nThe Jump of your Network is \n")
        for jump in range(32,193,32):
            print(f"{jump}\n")
   
    elif options == 2:  # Condition of the option !
        print("\nThe all broadcast are:\n")
        for jump in range(32,193,32):
            print(f"\n128.10.{jump - 1}.255")
   
    elif options == 3: # Condition of the option !
        
        for valideIP in range(0,256):
            print(f'128.10.0.{valideIP}')
            if valideIP == 255:
                print("\n \n Ok \n")
                for newClock in range(1, 32):
                    for valideIP in range(0,256):
                        print(f'128.10.{newClock}.{valideIP} ')

    elif options == 4:
        print("\nOr sub-network are\n")
        for subnetwork in range(0,193,32):
            print(f'128.10.{subnetwork}.0\n ')
    elif options == 0:
        print("\n\nTchau!!")
        sys.exit(1)
    else:
        pass

# Author : Edgar A. Dikenge