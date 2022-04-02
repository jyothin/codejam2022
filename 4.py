#!python3

import sys
import itertools

T = int(input())
# T = 2

class Node:

    f = 0
    p = 0
    ini = None
    ts = None

    def __init__(self, f, p):
        self.f = f
        self.p = p
        self.ini = True
        self.ts = []

class Graph:

    N = 0
    nodes = None
    iniNodes = None

    def __init__(self, N, F, P):
        self.N = N
        self.nodes = []
        self.iniNodes = []

        node = Node(0, 0)
        self.nodes.append(node)

        i = 0
        while i < N:
            # print(i)
            node = Node(F[i], P[i])
            self.nodes[node.p].ini = False
            self.nodes.append(node)
            i = i + 1
            # self.printChain(i)

        i = 1
        while i <= N:
            if self.nodes[i].ini:
                self.iniNodes.append(i)
                # print(i, self.iniNodes)
            i = i + 1

    def printNode(self, i):
        node = self.nodes[i]
        print("{}, {}, {}, {}".format(node.f, node.p, node.ini, node.ts))

    def printNodes(self):
        i = 0
        while i < self.N+1:
            node = self.nodes[i]
            print("{}, {}, {}, {}".format(node.f, node.p, node.ini, node.ts))
            i = i + 1

    def printChain(self, i):
        node = self.nodes[i]
        self.printNode(i)
        print("->")
        while node.f:
            self.printNode(node.p)
            node = self.nodes[node.p]
            print("->")

    def getNodes(self):
        return self.nodes

    def getIniNodes(self):
        return self.iniNodes

for t in range(1, T+1):
    N = int(input())
    F = [int(f) for f in input().split(" ")]
    P = [int(p) for p in input().split(" ")]
    # print("{}, {}, {}".format(N, F, P))

    graph = Graph(N, F, P)
    # graph.printNodes()

    nodes = graph.getNodes()
    iniNodes = graph.getIniNodes()
    # print(iniNodes)

    ttf = 0
    sNum = 0
    for subset in itertools.permutations(iniNodes, len(iniNodes)):
        # print("sNum: {}".format(sNum))
        # print(subset)
        subset = list(subset)
        
        tf = 0
        while len(subset) != 0:
            ss = subset.pop(0)
            cf = []

            # print("Initiator node {}".format(ss))
            node = nodes[ss]

            # print("{}, {}, {}, {}".format(node.f, node.p, node.ini, node.ts))
            node.ts.append(True)
            cf.append(node.f)
            # print("cf = {}".format(cf))
            # print("{}, {}, {}, {}".format(node.f, node.p, node.ini, node.ts))

            # graph.printChain(ss)
            # graph.printNodes()

            while node.p:
                node = nodes[node.p]
                # print("{}, {}, {}, {}".format(node.f, node.p, node.ini, node.ts))
                if len(node.ts) == 0 or len(node.ts) == sNum or not node.ts[sNum]:
                    cf.append(node.f)
                    # print("cf = {}".format(cf))
                    node.ts.append(True)
                # print("{}, {}, {}, {}".format(node.f, node.p, node.ini, node.ts))

            if len(cf) == 0:
                max_cf = 0
            else:
                max_cf = max(cf)
            # print("max_cf: {}".format(max_cf))
            tf = tf + max_cf

        # print("tf: {}".format(tf))
        sNum = sNum + 1

        ttf = max(ttf, tf)

    print("Case #{}: {}".format(t, ttf))
