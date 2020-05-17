import sys
input = sys.stdin.readline
import math
def main():
    A, B, H, M = map(int, input().split())
    s_rad = 0
    if H == 0:
        s_rad = math.pi/2
    elif H <= 3:
        s_rad = (3-H)/12*2*math.pi
    else:
        s_rad = math.pi/2 + (12-H)/12*2*math.pi
    s_rad -= M/60*2*math.pi/12
    l_rad = 0
    if M == 0:
        l_rad = math.pi/2
    elif M <= 15:
        l_rad = (15-M)/60*2*math.pi
    else:
        l_rad = math.pi/2 + (60-M)/60*2*math.pi
    sx = A * math.cos(s_rad)
    sy = A * math.sin(s_rad)
    lx = B * math.cos(l_rad)
    ly = B * math.sin(l_rad)
    ans = math.sqrt(((sx-lx)**2) + ((sy-ly)**2))
    print(ans)
if __name__ == "__main__":
    main()