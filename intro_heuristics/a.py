import sys, random
input = sys.stdin.readline
def main():
    D = int(input())
    c = list(map(int, input().split()))
    s = []
    for _ in range(D):
        si = list(map(int, input().split()))
        s.append(si)
    last_list = [0] * 26
    minus_sat_list = [0] * 26
    for i in range(D):
        for j in range(26):
            minus_sat_list[j] += c[j] * (i+1-last_list[j])
        best_idx = 0
        worst_sat, worst_sat_idx  = 0, -1
        worst2_sat, worst2_sat_idx  = 0, -1
        worst3_sat, worst3_sat_idx  = 0, -1
        worst4_sat, worst4_sat_idx  = 0, -1
        worst5_sat, worst5_sat_idx  = 0, -1
        for j in range(26):
            if (minus_sat_list[j] > worst_sat) or (minus_sat_list[j] == worst_sat and s[i][j] > s[i][worst_sat_idx]):
                worst_sat = minus_sat_list[j]
                worst_sat_idx = j
            elif (minus_sat_list[j] > worst2_sat) or (minus_sat_list[j] == worst2_sat and s[i][j] > s[i][worst2_sat_idx]):
                worst2_sat = minus_sat_list[j]
                worst2_sat_idx = j
            elif (minus_sat_list[j] > worst3_sat) or (minus_sat_list[j] == worst3_sat and s[i][j] > s[i][worst3_sat_idx]):
                worst3_sat = minus_sat_list[j]
                worst3_sat_idx = j
            elif (minus_sat_list[j] > worst4_sat) or (minus_sat_list[j] == worst4_sat and s[i][j] > s[i][worst4_sat_idx]):
                worst4_sat = minus_sat_list[j]
                worst4_sat_idx = j
            elif (minus_sat_list[j] > worst5_sat) or (minus_sat_list[j] == worst5_sat and s[i][j] > s[i][worst5_sat_idx]):
                worst5_sat = minus_sat_list[j]
                worst5_sat_idx = j
        worst_val = s[i][worst_sat_idx] * 2 + worst_sat
        worst2_val = s[i][worst2_sat_idx] * 2 + worst2_sat
        worst3_val = s[i][worst3_sat_idx] * 2 + worst3_sat
        worst4_val = s[i][worst4_sat_idx] * 2 + worst4_sat
        worst5_val = s[i][worst5_sat_idx] * 2 + worst5_sat
        best_val = max(worst_val, worst2_val, worst3_val, worst4_val, worst5_val)
        if best_val == worst_val:
            best_idx = worst_sat_idx
        elif best_val == worst2_val:
            best_idx = worst2_sat_idx
        elif best_val == worst3_val:
            best_idx = worst3_sat_idx
        elif best_val == worst4_val:
            best_idx = worst4_sat_idx
        elif best_val == worst5_val:
            best_idx = worst5_sat_idx
        minus_sat_list[best_idx] = 0
        last_list[best_idx] = i + 1
        print(best_idx+1, minus_sat_list)
        print(s[i])
if __name__ == "__main__":
    main()