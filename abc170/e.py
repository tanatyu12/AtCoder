import sys
input = sys.stdin.readline
import random
class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
class Treap:
    def __init__(self):
        self.root = None
        self.order_list = []
    def right_rotate(self, t):
        s = t.left
        t.left = s.right
        s.right = t
        return s
    def left_rotate(self, t):
        s = t.right
        t.right = s.left
        s.left = t
        return s
    def find(self, key):
        x = self.root
        while x != None:
            if key == x.key:
                return x
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return None
    def insert(self, t, key, priority):
        if t == None:
            return Node(key, priority)
        if key == t.key:
            return t
        if key < t.key:
            t.left = self.insert(t.left, key, priority)
            if priority > t.priority:
                t = self.right_rotate(t)
        else:
            t.right = self.insert(t.right, key, priority)
            if priority > t.priority:
                t = self.left_rotate(t)
        return t
    def delete(self, t, key):
        if t == None:
            return None
        if key < t.key:
            t.left = self.delete(t.left, key)
        elif key > t.key:
            t.right = self.delete(t.right, key)
        else:
            return self.__delete(t, key)
        return t
    def __delete(self, t, key):
        if t.left == None and t.right == None:
            return None
        elif t.left == None:
            t = self.left_rotate(t)
        elif t.right == None:
            t = self.right_rotate(t)
        else:
            if t.left.priority < t.right.priority:
                t = self.left_rotate(t)
            else:
                t = self.right_rotate(t)
        return self.delete(t, key)
    def min(self):
        x = self.root
        y = None
        while x != None:
            y = x
            x = x.left
        return y
    def max(self):
        x = self.root
        y = None
        while x != None:
            y = x
            x = x.right
        return y
    def walk_preorder(self, node):
        if node == None:
            return None
        self.order_list.append(node.key)
        self.walk_preorder(node.left)
        self.walk_preorder(node.right)
    def walk_inorder(self, node):
        if node == None:
            return None
        self.walk_inorder(node.left)
        self.order_list.append(node.key)
        self.walk_inorder(node.right)
    def print_nodes(self):
        self.order_list = []
        self.walk_inorder(self.root)
        inorder_str = ' '.join(map(str, self.order_list))
        print(' {}'.format(inorder_str))
        self.order_list = []
        self.walk_preorder(self.root)
        preorder_str = ' '.join(map(str, self.order_list))
        print(' {}'.format(preorder_str))
def main():
    N, Q = map(int, input().split())
    enjis = [[0, 0] for _ in range(N)]
    rates = [Treap() for _ in range(2*10**5)]
    max_rates = Treap()
    for i in range(N):
        A, B = map(int, input().split())
        enjis[i][0] = A
        enjis[i][1] = B-1
        rates[B-1].root = rates[B-1].insert(rates[B-1].root, A, random.randint(1, 20000))
    for i in range(20000):
        if rates[i].root != None:
            max_rate = rates[i].max()
            max_rates.root = max_rates.insert(max_rates.root, max_rate.key, random.randint(1, 20000))
    for _ in range(Q):
        C, D = map(int, input().split())
        a, b = enjis[C-1][0], enjis[C-1][1]

        old_max_rate = rates[b].max()
        rates[b].root = rates[b].delete(rates[b].root, a)
        new_max_rate = rates[b].max()
        max_rates.root = max_rates.delete(max_rates.root, old_max_rate.key)
        if new_max_rate != None:
            max_rates.root = max_rates.insert(max_rates.root, new_max_rate.key, random.randint(1, 20000))

        old_max_rate = rates[D-1].max()
        rates[D-1].root = rates[D-1].insert(rates[D-1].root, a, random.randint(1, 20000))
        new_max_rate = rates[D-1].max()
        if old_max_rate != None:
            max_rates.root = max_rates.delete(max_rates.root, old_max_rate.key)
        max_rates.root = max_rates.insert(max_rates.root, new_max_rate.key, random.randint(1, 20000))

        enjis[C-1][1] = D-1

        ans = max_rates.min().key
        print(ans)
if __name__ == "__main__":
    main()