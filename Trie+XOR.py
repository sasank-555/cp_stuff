class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0  # Keep track of how many numbers pass through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, val):
        curr = self.root
        for i in reversed(range(32)):
            bit = (val >> i) & 1
            if curr.children[bit] is None:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
            curr.count += 1

    def find_max(self, val):
        curr = self.root
        ans = 0
        for i in reversed(range(32)):
            bit = (val >> i) & 1
            if curr.children[1 - bit] is not None and curr.children[1 - bit].count > 0:
                ans += 1 << i
                curr = curr.children[1 - bit]
            else:
                curr = curr.children[bit]
        return ans

    def remove(self, val):
        curr = self.root
        nodes = []
        for i in reversed(range(32)):
            bit = (val >> i) & 1
            nodes.append((curr, bit))
            curr = curr.children[bit]
            curr.count -= 1

        # Remove nodes if their count is 0
        for i in reversed(range(32)):
            parent, bit = nodes[i]
            if parent.children[bit].count == 0:
                parent.children[bit] = None
            else:
                break

    # count x^y < k
    def count(self,x,k):
        curr = self.root
        ans  = 0
        for i in range(31,-1,-1):
            kb = 1 if k&(1<<i) else 0
            xb = 1 if x&(1<<i) else 0
            if kb==1:
                # yb can be same as xb
                if xb in curr.child:
                    ans+=curr.child[xb].count
                if 1- xb not in curr.child:
                    break
                curr = curr.child[1 - xb]
            else:
                if xb not in curr.child:
                    break
                curr = curr.child[xb]
        return ans


