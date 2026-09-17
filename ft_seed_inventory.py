def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit.lower() == "packets":
        rest = f"{quantity} packets available"
    elif unit.lower() == "grams":
        rest = f"{quantity} grams total"
    else:
        rest = f"covers {quantity} square meters"
    print(f"{seed_type.capitalize()} seed:", rest)
