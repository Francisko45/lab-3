
def print_penguin():
    print("   _~_   ", end="")
    
def print_eyes():
    print("  (o o)  ", end="")

def print_beak():
    print(" /  V  \\ ", end="")

def print_body():
    print("/(  _  )\\", end="")

def print_feet():
    print("  ^^ ^^  ", end="")


def main():
    N = int(input("Введіть число (від 1 до 9): "))
    if 1 <= N <= 9:
       
        print_penguin()
        for _ in range(N):
            print_penguin()
        print()
        
        for _ in range(N):
            print_eyes()
        print()

        for _ in range(N):
            print_beak()
        print()

        for _ in range(N):
            print_body()
        print()

        for _ in range(N):
            print_feet()
        print()

    else:
        print("Невірне число, введіть число від 1 до 9.")


main()
