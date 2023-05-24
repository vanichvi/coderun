import sys


def main():
    s = sys.stdin.readline()
    j = sys.stdin.readline()
    ans = 0
    for ch in j:
        if ch in s:
            ans += 1
    print(ans-1)


if __name__ == '__main__':
    main()
