__author__ = 'Tom'

class OptimalBST:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.root = dict()

    def optimal_bst(self, n):
        e = dict()
        w = dict()
        for i in range(1, n + 2):
            e[(i, i - 1)] = self.q[i - 1]
            w[(i, i - 1)] = self.q[i - 1]
        for l in range(1, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                e[(i, j)] = float("inf")
                w[(i, j)] = w[(i, j - 1)] + self.p[j - 1] + self.q[j]
                for r in range(i, j + 1):
                    t = round(e[(i, r - 1)] + e[(r + 1, j)] + w[(i, j)], 2)
                    if t < e[(i, j)]:
                        e[(i, j)] = t
                        self.root[(i, j)] = r
        return e

    def construct_optimal_bst(self):
        k = self.root[(1, len(self.p))]
        print "k[%d] is the root" % k
        l, r = [(1, k - 1,)], [(k + 1, len(self.p),)]
        p = [k]
        while p:
            if l:
                i, j = l.pop(0)
                if j < i:
                    print "d[%d] is the left child of k[%d]" % (j, p[0])
                else:
                    k = self.root[(i, j)]
                    print "k[%d] is the left child of k[%d]" % (k, p[0])
                    p[:0] = [k]
                    l.insert(0, (i, k - 1,))
                    r.insert(0, (k + 1, j))
            else:
                i, j = r.pop(0)
                if j < i:
                    print "d[%d] is the right child of k[%d]" % (j, p.pop(0))
                else:
                    k = self.root[(i, j)]
                    print "k[%d] is the right child of k[%d]" % (k, p.pop(0))
                    p[:0] = [k]
                    l.insert(0, (i, k - 1))
                    r.insert(0, (k + 1, j,))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Find the optimal binary search tree based on probabilities of keys')
    parser.add_argument('--p', metavar='P', type=float, nargs='+', help='A list of probabilities of each key')
    parser.add_argument('--q', metavar='Q', type=float, nargs='+', help='A list of probabilities of each dummy key')
    args = parser.parse_args()
    bst = OptimalBST(args.p, args.q)
    bst.optimal_bst(len(args.p))
    bst.construct_optimal_bst()
