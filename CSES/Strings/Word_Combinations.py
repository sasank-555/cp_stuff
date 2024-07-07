from functools import lru_cache
import sys
sys.setrecursionlimit(2000006)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# @lru_cache(None)
# def helper(i):
#   if i>=len(s):
#     return 1
#   ans = 0
#   curr = trie.root
#   for j in range(i,len(s)):
#     if s[j] in curr.children:
#         curr = curr.children[s[j]]
#         if curr.word:
#             ans+=helper(j+1)
#     else:
#         break
#   return ans
s = input()
N = len(s)
k = int(input())
mod = 10**9 + 7
trie = Trie()
for _ in range(k):
   trie.insert(input())
dp = [0]*(N+1)
dp[N] =1
for i in reversed(range(N)):
  ans = 0
  curr = trie.root
  for j in range(i,len(s)):
    if s[j] in curr.children:
        curr = curr.children[s[j]]
        if curr.word:
            ans+=dp[j+1]
    else:
        break
  dp[i]= ans
print(dp[0]%mod)