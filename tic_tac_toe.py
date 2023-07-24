import pygame

pygame.init()

# グリッド線の描画
def drow_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * 200), (screen_width, i * 200), 5)
        pygame.draw.line(screen, BLACK, (i * 200, 0), (i * 200, screen_height), 5)

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
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]]

for row_index, row in enumerate(board):
    for col_index, col in enumerate(row):
        if col == 1:
            print(col_index, col)

# メインループ#####################################################
run = True
while run:

    # 背景の塗りつぶし
    screen.fill(WHITE)
    
    # グリッド線の描画
    drow_grid()

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