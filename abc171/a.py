import sys
input = sys.stdin.readline
import string
def main():
    c = input().rstrip()
    if c in string.ascii_lowercase:
        print('a')
    else:
        print('A')
if __name__ == "__main__":
    main()