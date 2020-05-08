import sys
input = sys.stdin.readline
def main():
    S = input().rstrip("\r\n")
    ans = 0
    for i in range(2**(len(S)-1)):
        nums = []
        num_str = S[0]
        for j in range(len(S)-1):
            if (i >> j) & 1:
                nums.append(int(num_str))
                num_str = S[j+1]
            else:
                num_str += S[j+1]
        if num_str != "":nums.append(int(num_str))
        ans += sum(nums)
    print(ans)
if __name__ == "__main__":
    main()