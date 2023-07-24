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

# ボード(0: 空白，1: 〇，-1: ×)
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

# メインループ#####################################################
run = True
while run:

    # 背景の塗りつぶし
    screen.fill(WHITE)
    
    # グリッド線の描画
    drow_grid()

    # ボードの描画
    drow_board()

    # イベントの取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    # 更新
    pygame.display.update()

##################################################################

pygame.quit()