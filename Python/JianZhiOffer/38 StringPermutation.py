# recursive solution, two parts, part 1: first char, part 2: the other chars
# need rewrite.
class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s:
            return
        c, res = list(s), []

        def recur(x):
            if not x < len(c) - 1:
                res.append(''.join(c))
                return
            vis = set()
            for i in range(x, len(s)):
                if c[i] in vis:  # avoid overlap
                    continue
                vis.add(c[i])
                c[i], c[x] = c[x], c[i]  # swap
                recur(x + 1)
                c[x], c[i] = c[i], c[x]  # swap to recover

        recur(0)
        return res