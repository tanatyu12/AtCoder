import sys
input = sys.stdin.readline
def main():
    N = input().rstrip()
    if N[-1] == "0" or N[-1] == "1" or N[-1] == "6" or N[-1] == "8":
        print("pon")
    elif N[-1] == "3":
        print("bon")
    else:
        print("hon")
if __name__ == "__main__":
    main()