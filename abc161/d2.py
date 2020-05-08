import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
def f(v,i,ans):
    if i == 0:return
    if str(v)[-1] != "0":
        x = int(str(v)+str(int(str(v)[-1])-1))
        ans.add(x)
        f(x,i-1,ans)
    y = int(str(v)+str(v)[-1])
    ans.add(y)
    f(y,i-1,ans)
    if str(v)[-1] != "9":
        z = int(str(v)+str(int(str(v)[-1])+1))
        ans.add(z)
        f(z,i-1,ans)
def main():
    K = int(input())
    ans = set()
    for i in range(1,10):
        ans.add(i)
        f(i,10,ans)
    ans = list(ans)
    ans.sort()
    print(ans[K-1])
if __name__ == "__main__":
    main()