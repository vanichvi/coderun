import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = sorted(list(map(int, sys.stdin.readline().split())))
        r = a[0] ^ a[1]
        for i in range(1, n):
            r = min(r, a[i - 1] ^ a[i])

        print(r)


if __name__ == "__main__":
    main()
