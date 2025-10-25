EMPTY = 'x'

def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
        
    def remove():
        cnt = 0
        block_to_remove = []
        for r in range(m-1):
            for c in range(n-1):
                if (board[r][c] == board[r+1][c] == board[r][c+1] == board[r+1][c+1]) and board[r][c] != EMPTY:
                    block_to_remove.append((r, c))
        for r, c in block_to_remove:
            for dr, dc in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                nr, nc = r + dr, c + dc
                if board[nr][nc] != EMPTY:
                    cnt += 1
                    board[nr][nc] = EMPTY
        return cnt
    
    def fall():
        for c in range(n):
            valid_blocks = [board[r][c] for r in range(m) if board[r][c] != EMPTY]
            fallen_cols = [EMPTY] * (m - len(valid_blocks)) + valid_blocks
            for r in range(m):
                board[r][c] = fallen_cols[r]
    
    prev_answer = -1
    answer = 0
    while prev_answer != answer:
        prev_answer = answer
        answer += remove()
        fall()
    return answer