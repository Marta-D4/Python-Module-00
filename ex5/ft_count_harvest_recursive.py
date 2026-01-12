def ft_count_harvest_recursive():
    print(f"Days until harvest: {days}")

    def count(day):
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1)

    count(1)

# ft_count_harvest_recursive(5)
