class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s:
            return

        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))
                return
            vis = set()

            for i in range(x, len(c)):
                if c[i] in vis:
                    continue
                vis.add(c[i])
                c[x], c[i] = c[i], c[x]
                dfs(i + 1)
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res