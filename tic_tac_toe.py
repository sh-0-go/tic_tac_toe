import pygame

pygame.init()

# グリッド線の描画
def drow_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * 200), (screen_width, i * 200), 5)
        pygame.draw.line(screen, BLACK, (i * 200, 0), (i * 200, screen_height), 5)

# ボードの描画
def drow_board():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                # 〇を描画
                pygame.draw.circle(screen, RED, (col_index * 200 + 100, row_index * 200 + 100), 80, 5)
            elif col == -1:
                # ×を描画
                pygame.draw.line(screen, BLUE, (col_index * 200 + 20, row_index * 200 + 20), (col_index * 200 + 180, row_index * 200 + 180), 5)
                pygame.draw.line(screen, BLUE, (col_index * 200 + 180, row_index * 200 + 20), (col_index * 200 + 20, row_index * 200 + 180), 5)

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
        winner_text_img = font.render(winner +' Win!', True, BLACK, GREEN)
        screen.blit(winner_text_img, (200, 150))
        reset_text_img = font.render('click to reset', True, BLACK, GREEN)
        screen.blit(reset_text_img, (100, 300))
        game_over = True
    
    return game_over

# ウィンドウの作成
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ox ゲーム")

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

# メインループ#####################################################
run = True
while run:

    # 背景の塗りつぶし
    screen.fill(WHITE)
    
    # グリッド線の描画
    drow_grid()

    # マウスの一の取得
    mx, my = pygame.mouse.get_pos()
    x = mx // 200
    y = my // 200

    # ボードの描画
    drow_board()

    # 勝者の確認
    game_over = check_winner()

    # イベントの取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board[y][x] == 0 and game_over == False:
                board[y][x] = number
                number *= -1
            if game_over:
                board = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
                number = 1
    
    # 更新
    pygame.display.update()

##################################################################

pygame.quit()