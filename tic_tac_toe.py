import pygame
import math

pygame.init()

# グリッド線の描画
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * 200), (screen_width, i * 200), 5)
        pygame.draw.line(screen, BLACK, (i * 200, 0), (i * 200, screen_height), 5)

# ボードの描画
def draw_board():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                # 〇を描画
                pygame.draw.circle(screen, RED, (col_index * 200 + 100, row_index * 200 + 100), 80, 5)
            elif col == -1:
                # ×を描画
                pygame.draw.line(screen, BLUE, (col_index * 200 + 20, row_index * 200 + 20), (col_index * 200 + 180, row_index * 200 + 180), 5)
                pygame.draw.line(screen, BLUE, (col_index * 200 + 180, row_index * 200 + 20), (col_index * 200 + 20, row_index * 200 + 180), 5)

# ボードの中身が0か確認
def all_elements_nonzero():
    for row in board:
        for element in row:
            if element == 0:
                return False
    return True

# 勝利の確認
def check_winner():
    winner = None
    game_over = False
    for row_index, row in enumerate(board):
        # 横軸の確認
        if sum(row) == 3:
            winner = 'o'
        if sum(row) == -3:
            winner = 'x'
        # 縦軸の確認
        if board[0][row_index] + board[1][row_index] + board[2][row_index] == 3:
            winner = 'o'
        if board[0][row_index] + board[1][row_index] + board[2][row_index] == -3:
            winner = 'x'
        # 斜めの確認
        if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3:
            winner = 'o'
        if board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3:
            winner = 'x'

    # 勝者の描画
    if winner == 'o' or winner == 'x':
        winner_text_img = font.render(winner + ' Win!', True, BLACK, GREEN)
        screen.blit(winner_text_img, (200, 150))
        reset_text_img = font.render('click to reset', True, BLACK, GREEN)
        screen.blit(reset_text_img, (100, 300))
        game_over = True
    
    elif all_elements_nonzero():
        draw_text_img = font.render('It is a draw.', True, BLACK, GREEN)
        screen.blit(draw_text_img,(110,150))
        reset_text_img = font.render('click to reset', True, BLACK, GREEN)
        screen.blit(reset_text_img, (100, 300))
        game_over = True
    
    return game_over

# ウィンドウの作成
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("OX ゲーム")

# 他の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 

# フォントの設定
font = pygame.font.SysFont(None, 100)

# ボード(0: 空白，1: 〇，-1: ×)
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

number = 1
turn_count = 1

# ミニマックス法でAIの手を計算
def minimax(depth, is_maximizing):
    if check_winner():
        if is_maximizing:
            return -1
        else:
            return 1
        
    if depth == 0:
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = -1
                    eval = minimax(depth - 1, False)
                    board[row][col] = 0
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = 1
                    eval = minimax(depth - 1, True)
                    board[row][col] = 0
                    min_eval = min(min_eval, eval)
        return min_eval

# AIの手を選択
def ai_move():
    best_eval = -math.inf
    best_move = None
    if board[1][1] == 0:
        board[1][1] = -1
    elif board[1][2] == 1 and board[2][0] == 1 and board[2][2] == 0 and turn_count == 4:
        board[2][2] = -1
    elif board[2][1] == 1 and board[0][0] == 1 and board[2][0] == 0 and turn_count == 4:
        board[2][0] = -1
    elif board[2][1] == 1 and board[0][2] == 1 and board[2][2] == 0 and turn_count == 4:
        board[2][2] = -1
    elif board[0][2] == 1 and board[2][0] == 1 and board[1][2] == 0 and turn_count == 4:
        board[1][2] = -1
    elif board[1][1] == 1 and board[2][2] == 1 and board[0][2] == 0 and turn_count == 4:
        board[0][2] = -1
    else:
        for row in range(3):
            for col in range(3):
                print(pygame.time.get_ticks())
                if board[row][col] == 0:
                    board[row][col] = -1
                    eval = minimax(1, False)
                    board[row][col] = 0
                    if eval > best_eval:
                        best_eval = eval
                        best_move = (row, col)
    if best_move:
        board[best_move[0]][best_move[1]] = -1

    # AIの手を選択した後に遅延を追加
    pygame.time.delay(500)  # 500ミリ秒（0.5秒）の遅延

# メインループ#####################################################
run = True
player_turn = True  # プレイヤーのターンかどうかを管理

while run:

    # 背景の塗りつぶし
    screen.fill(WHITE)
    
    # グリッド線の描画
    draw_grid()

    # マウスの位置を取得
    mx, my = pygame.mouse.get_pos()
    x = mx // 200
    y = my // 200

    # ボードの描画
    draw_board()

    # 勝者の確認
    game_over = check_winner()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        # プレイヤーのターンで、かつゲームが終了していない場合にのみプレイヤーの手を選択
        if player_turn and not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board[y][x] == 0:
                    board[y][x] = number
                    turn_count += 1
                    player_turn = False  # プレイヤーの手を選択したらAIのターンへ
                    number *= -1

        # AIの手を選択
        elif not player_turn and not game_over:
            ai_move()
            turn_count +=1
            player_turn = True  # AIの手を選択したらプレイヤーのターンへ
            number *= -1

        # ゲームが終了したら
        elif game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                board = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
                turn_count = 1
                player_turn = True
                number = 1


    # 更新
    pygame.display.update()

##################################################################

pygame.quit()
