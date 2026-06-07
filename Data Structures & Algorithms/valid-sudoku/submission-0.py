class Solution:
    def sub_box_helper(self, board, r_start: int, r_end: int, c_start: int, c_end: int):
        seen = []
        for i in range(r_start, r_end):
            for j in range(c_start, c_end):
                val = board[i][j]
                if val == ".": continue
                seen.append(val)
        
        if len(set(seen)) != len(seen): return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # check row validity
        for row in board:
            seen = set()
            for val in row:
                if val == ".": continue

                if val in seen:
                    return False
                
                seen.add(val)
        
        # check column validity
        for i in range(n):
            seen = set()
            for j in range(n):
                val = board[j][i]
                if val == ".": continue

                if val in seen:
                    return False
                
                seen.add(val)
        
        # check sub-boxes
        # rows(1-3) cols(1-3)
        check_one = self.sub_box_helper(board, 0, 3, 0, 3)

        # rows (1-3) cols (4-6)
        check_two = self.sub_box_helper(board, 0, 3, 3, 6)

        # rows (1-3) cols (7-9)
        check_three = self.sub_box_helper(board, 0, 3, 6, 9)

        # rows (4-6) cols(1-3)
        check_four = self.sub_box_helper(board, 3, 6, 0, 3)

        # rows (4-6) cols(4-6)
        check_five = self.sub_box_helper(board, 3, 6, 3, 6)

        # rows (4-6) cols(7-9)
        check_six = self.sub_box_helper(board, 3, 6, 6, 9)

        # rows (7-9) cols (1-3)
        check_seven = self.sub_box_helper(board, 6, 8, 0, 3)

        # rows (7-9) cols (4-6)
        check_eight = self.sub_box_helper(board, 6, 8, 3, 6)

        # rows (7-9) cols (7-9)
        check_nine = self.sub_box_helper(board, 6, 8, 6, 9)

        sub_box_checks = [check_one, check_two, check_three, check_four,
                        check_five, check_six, check_seven, check_eight, check_nine]
        
        if any(not val for val in sub_box_checks):
            return False
        
        return True