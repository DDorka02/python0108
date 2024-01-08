def jatek():
    print("I/A:")
    nev = input("\tJátékos neve: ")
    szerep = input("\tszerepkör: ")
    print("I/B:")
    if szerep == "varázsló":
        print(f"\tÜdvözlünk {nev}, 2 életed van!")
    elif szerep == "harcos":
        print(f"\tÜdvözlünk {nev}, 10 életed van!")
    else:
        print(f"\tÜdvözlünk {nev}, 8 életed van!")
