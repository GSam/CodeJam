def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

a = primes2(10**9)
primes = set(a)
class Node:
    def __init__(self, val):
        self.val = val
        self.child = []
        self.vv = set()

    def __repr__(self):
        return str(self.val)

    def add_to_tree(self, node):
        if node.val == self.val:
            return set()
        for c in self.child:
            if c.val == node.val:
                return set() # NO NEED TO ADD NODE TWICE
        #print node, self
        to_insert = set()
        self.walk_tree(node, [self], to_insert)
        return to_insert

    def walk_tree(self, node, path, to_insert):
        global minV, ans
        # At this point we know that the two can be added
        if len(path) >= 4:
            if minV == -1 or sum([x.val for x in path]) + node.val < minV:
                minV = sum([x.val for x in path]) + node.val
                ans = path + [node]
                print "FOUND:", ans, minV
            return
        for c in self.child:
            if (int(str(c.val) + str(node.val)) in primes and
                int(str(node.val) + str(c.val)) in primes):
                c.walk_tree(node, path[:] + [c], to_insert)

        self.child.append(Node(node.val))
        to_insert.add((self.val, node.val))

b = {}
minV = -1
ans = None
for prime in a:
    s = str(prime)
    for i in xrange(1, len(s)):
        start, end = s[:i], s[i:]
        if str(int(start)) + str(int(end)) == s and int(end + start) in primes and int(end) in primes and int(start) in primes:
            # Both [end][start], start and end in primes
            if int(start) > int(end):
                # You must have done this already?
                continue
            node1 = b.get(int(start))
            if node1 is None:
                 node1 = Node(int(start))
                 b[int(start)] = node1
            node2 = b.get(int(end))
            if node2 is None:
                node2 = Node(int(end))
                b[int(end)] = node2

            todo = node1.add_to_tree(Node(int(end)))
            todo = todo.union(node2.add_to_tree(Node(int(start))))
            while len(todo) > 0:
                g,h = todo.pop()
                gn = b.get(g)
                if gn is None:
                    gn = Node(g)
                    b[g] = gn
                todo = todo.union(gn.add_to_tree(Node(h)))
