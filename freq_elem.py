import sys


def main():
    d = {}
    n = sys.stdin.readline()
    numbers = list(map(int, sys.stdin.readline().split()))
    for a in numbers:
        chk = d.get(a)
        if chk is None:
            d[a] = 1
        else:
            d[a] = chk + 1
    freq = list(d.values())
    mf = max(freq)
    res = []
    for (k, v) in d.items():
        if v == mf:
            res += [k]
    print(max(res))


if __name__ == "__main__":
    main()
