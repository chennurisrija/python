class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for _ in range(numRows)]
        idx, d = 0, 1
        
        for c in s:
            rows[idx].append(c)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        
        return ''.join(''.join(row) for row in rows)
