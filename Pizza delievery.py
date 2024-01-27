def calculate_pizza_slices():

    num_individuals = int(input("Enter the number of individuals in the party: "))

    slices_per_large = 8
    slices_per_medium = 6
    slices_per_regular = 4
    slices_per_small = 1


    num_large_pizzas = num_individuals // slices_per_large
    num_medium_pizzas = 0
    num_regular_pizzas = 0
    num_small_pizzas = 0

    remaining_slices = num_individuals % slices_per_large


    if remaining_slices > 0:
        num_regular_pizzas = remaining_slices // slices_per_regular
        remaining_slices %= slices_per_regular

        if remaining_slices > 0:
            num_small_pizzas = remaining_slices // slices_per_small


    print(f"If there are {num_individuals} individuals:")
    print(f"1. we will have {num_large_pizzas} Large pizza")
    print(f"2. we will have {num_medium_pizzas} Medium pizza")
    print(f"3. we will have {num_regular_pizzas} Regular Pizza")
    print(f"4. we will have {num_small_pizzas} Small Pizza")


    total_slices = (num_large_pizzas * slices_per_large) + (num_medium_pizzas * slices_per_medium) + \
                   (num_regular_pizzas * slices_per_regular) + (num_small_pizzas * slices_per_small)

    print(f"\nTotal slices: {total_slices}")


calculate_pizza_slices()
