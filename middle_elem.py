import sys


def main():
    numbers = list(map(int, sys.stdin.readline().split()))
    numbers.sort()
    print(numbers[1])


if __name__ == '__main__':
    main()
