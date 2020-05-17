import sys
input = sys.stdin.readline
def main():
    S = input().rstrip()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    today = days.index(S)
    ans = 7 - today
    print(ans)
if __name__ == "__main__":
    main()