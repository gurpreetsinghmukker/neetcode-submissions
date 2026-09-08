class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def extract_valid_elems(elems):
            valid_elems = []
            for elem in elems:
                if not elem=='.':
                    valid_elems.append(elem)
            return valid_elems
        def check_row(vals):
            if not (len(set(vals)) == len(vals)):
                return False
            return True
        
        #Check all the rows:
        for row in board:
            if not check_row(extract_valid_elems(row)):
                return False

        #Check all the cols:
        boardT = [list(row) for row in zip(*board)]
        print(boardT)
        for col in boardT:
            if not check_row(extract_valid_elems(col)):
                return False
        
        for i in range(0, len(board), 3):      
            for j in range(0, len(board),3):
                print(f"Grid: {i},{j}")
                grid_33 = []
                for row in board[i:i+3]:
                    grid_33 = grid_33 + row[j:j+3]
                # print(grid_33)
                print(extract_valid_elems(grid_33))
                if not check_row(extract_valid_elems(grid_33)):
                    return False
        return True
