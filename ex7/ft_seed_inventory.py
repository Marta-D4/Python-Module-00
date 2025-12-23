def ft_seed_inventory(type: str, quantity: int, units: str) -> None:
    seed = type.capitalize()
    if units == "packets":
        print(type, "seeds:", quantity, "packets available")
    elif units == "grams":
        print(type, "seeds:", quantity, "grams total")
    elif units == "area":
        print(type, "seeds:", quantity, "square meters")
