def is_in_check(board):
    size = len(board)  
    king_pos = None

    
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return "Error: No King on the board."

    king_row, king_col = king_pos

    
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  
        row, col = king_row, king_col
        while 0 <= row < size and 0 <= col < size:
            row += direction[0]
            col += direction[1]
            if row < 0 or row >= size or col < 0 or col >= size:
                break
            if board[row][col] == '.':
                continue
            if board[row][col] in ('R', 'Q'):
                return "Success"
            else:
                break

    
    for direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:  # ทิศทางทแยงทั้ง 4
        row, col = king_row, king_col
        while 0 <= row < size and 0 <= col < size:
            row += direction[0]
            col += direction[1]
            if row < 0 or row >= size or col < 0 or col >= size:
                break
            if board[row][col] == '.':
                continue
            if board[row][col] in ('B', 'Q'):
                return "Success"
            else:
                break

   
    for offset in [(-1, -1), (-1, 1)]:  # เฉียงซ้ายบน, เฉียงขวาบน
        row, col = king_row + offset[0], king_col + offset[1]
        if 0 <= row < size and 0 <= col < size and board[row][col] == 'P':
            return "Success"

    return "Fail"