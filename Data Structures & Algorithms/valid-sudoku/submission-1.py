class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        tiles = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                element = board[i][j]
                if element != "." and (
                    element in rows[i]
                    or element in cols[j]
                    or element in tiles[(i // 3) * 3 + (j // 3)]
                ):
                    return False
                elif element != ".":
                    rows[i].add(element)
                    cols[j].add(element)
                    tiles[(i//3)*3+(j//3)].add(element)

                # print(i, j, board[i][j])
        return True
