# def string() -> str:
#     return "Hello from function town"

# print(string())


def towns(amount: int):
    for x in range(1, amount + 1):
        print(f"Hello from function town {x}!")
    print()

towns(3)

towns(7)