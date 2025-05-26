print("shruthi.p/1AY24AI104/O")
def collatz_sequence(n):
    steps = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps.append(n)
    return steps

def main():
    try:
        number = int(input("Enter a positive integer: "))
        if number <= 0:
            print("Please enter a number greater than 0.")
            return
        sequence = collatz_sequence(number)
        print("Collatz sequence:")
        print(" → ".join(str(num) for num in sequence))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
