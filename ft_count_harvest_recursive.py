def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(n):
        if n == 0:
            return
        count(n - 1)
        print(f"Day {n}")

    count(days)
    print("Harvest time!")
