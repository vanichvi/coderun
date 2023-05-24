from collections import Counter


def main():
    input()
    print(sum(v == 1 for k, v in Counter(map(int, input().split())).items()))


if __name__ == '__main__':
    main()
