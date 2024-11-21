def cais_in_check(piece, position, king_pos, board):
    """
    ตรวจสอบว่าตัวหมากสามารถโจมตี King ได้หรือไม่
    """
    directions = {
        'P': [(-1, -1), (-1, 1)],  # Pawn เดินทแยงหน้า
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # Bishop เดินทแยงทุกทิศ
        'R': [(0, -1), (0, 1), (-1, 0), (1, 0)],  # Rook เดินแนวตั้งและแนวนอน
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]  # Queen เดินได้ทุกทิศ
    }

    if piece not in directions:
        return False  # ตัวหมากไม่ใช่ตัวที่สามารถโจมตีได้

    for dr, dc in directions[piece]:
        r, c = position
        if piece == 'P':  # Pawn ตรวจทิศทางเฉพาะจุดเดียว
            r += dr
            c += dc
            if (r, c) == king_pos:
                return True
            continue

        # เดินต่อไปในแนวทิศทางสำหรับ Bishop, Rook, Queen
        while 0 <= r < len(board) and 0 <= c < len(board[r]):  
            r += dr
            c += dc
            if (r, c) == king_pos:
                return True
            if 0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c] != '.':
                break  # มีตัวหมากขวางทาง

    return False


def is_in_check(board):
    """
    ตรวจสอบว่ามีตัวหมากใดสามารถโจมตี King ได้หรือไม่
    """
    # หา King (K) ในกระดาน
    king_pos = None
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return "Fail"  # หากไม่มีกษัตริย์ในกระดาน

    # ตรวจสอบตัวหมากแต่ละตัวว่าคุกคาม King ได้หรือไม่
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell in "PBRQ":  # Pawn, Bishop, Rook, Queen
                if cais_in_check(cell, (i, j), king_pos, board):
                    return "Success"  # กษัตริย์กำลังถูกคุกคาม

    return "Fail"  # ไม่มีภัยคุกคาม
