import sys
import numpy as np
from graphics import *

#GUI params
ROW = 10
COLUMN = 15
GRID_WIDTH = 40
BORDER = 50
TIPS_SPACE = 100

ai_points = []  
player_points = []  
ai_player_points = []  
points_all = []  

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]

ratio = 1  # 进攻的系数   大于1 进攻型，  小于1 防守型
DEPTH = 3  # 搜索深度,只能是单数。如果是负数，评估函数评估的的是自己多少步之后的自己得分的最大值，并不意味着是最好的棋，评估函数的问题

shape_score = [(50, (0, 1, 1, 0, 0)),
               (50, (0, 0, 1, 1, 0)),
               (200, (1, 1, 0, 1, 0)),
               (500, (0, 0, 1, 1, 1)),
               (500, (1, 1, 1, 0, 0)),
               (5000, (0, 1, 1, 1, 0)),
               (5000, (0, 1, 0, 1, 1, 0)),
               (5000, (0, 1, 1, 0, 1, 0)),
               (5000, (1, 1, 1, 0, 1)),
               (5000, (1, 1, 0, 1, 1)),
               (5000, (1, 0, 1, 1, 1)),
               (5000, (1, 1, 1, 1, 0)),
               (5000, (0, 1, 1, 1, 1)),
               (50000, (0, 1, 1, 1, 1, 0)),
               (99999999, (1, 1, 1, 1, 1))] # 棋型的评估分数


def ai():
    negamax(True, DEPTH, -sys.maxsize,sys.maxsize)   
    return ai_point[0], ai_point[1]


def negamax(is_ai,depth, alpha, beta):
    if game_win(ai_points[-1][0],ai_points[-1][1],ai_points) or game_win(player_points[-1][0],player_points[-1][1],player_points) or depth == 0:
        return evaluation(is_ai)

    blank_list = list(set(points_all).difference(set(ai_player_points)))
    order(blank_list)   # 搜索顺序排序  提高剪枝效率
    # 遍历每一个候选步
    for next_step in blank_list:


        # 如果要评估的位置没有相邻的子， 则不去评估  减少计算
        if not has_neightnor(next_step):
            continue

        if is_ai:
            ai_points.append(next_step)
        else:
            player_points.append(next_step)
        ai_player_points.append(next_step)

        value = -negamax(not is_ai, depth - 1, -beta, -alpha)
        if is_ai:
            ai_points.remove(next_step)
        else:
            player_points.remove(next_step)
        ai_player_points.remove(next_step)

        if value > alpha:

            print(str(value) + "alpha:" + str(alpha) + "beta:" + str(beta))
            print(ai_player_points)
            if depth == DEPTH:
                ai_point[0] = next_step[0]
                ai_point[1] = next_step[1]
            # alpha + beta剪枝点
            if value >= beta:
                return beta
            alpha = value

    return alpha


def game_win(point_x,point_y,list):
    for  i in range(len(dx)):
        total_closer=1
        for factor in [1,2,3,4]:
            if (point_x+dx[i]*factor,point_y+dy[i]*factor) in list:
                total_closer+=1
            else: break
        for factor in [-1,-2,-3,-4]:
            if (point_x+dx[i]*factor,point_y+dy[i]*factor) in list:
                total_closer+=1
            else: break
        if total_closer > 4: return True
    return False
        

    for m in range(COLUMN):
        for n in range(ROW):
            if n < ROW - 4 and (m, n) in list and (m, n + 1) in list and (m, n + 2) in list and (
                    m, n + 3) in list and (m, n + 4) in list:
                return True
            elif m < COLUMN - 4 and (m, n) in list and (m + 1, n) in list and (m + 2, n) in list and (
                        m + 3, n) in list and (m + 4, n) in list:
                return True
            elif m < COLUMN - 4 and n < ROW - 4 and (m, n) in list and (m + 1, n + 1) in list and (
                        m + 2, n + 2) in list and (m + 3, n + 3) in list and (m + 4, n + 4) in list:
                return True
            elif m < COLUMN - 4 and n > 3 and (m, n) in list and (m + 1, n - 1) in list and (
                        m + 2, n - 2) in list and (m + 3, n - 3) in list and (m + 4, n - 4) in list:
                return True
    return False

# 每个方向上的分值计算
def cal_score(m, n, x_vector, y_vector, enemy_list, my_list, score_all_arr):
    add_score = 0  # 加分项
    # 在一个方向上， 只取最大的得分项
    max_score_shape = (0, None)

    # 如果此方向上，该点已经有得分形状，不重复计算
    for item in score_all_arr:
        for pt in item[1]:
            if m == pt[0] and n == pt[1] and x_vector == item[2][0] and y_vector == item[2][1]:
                return 0

    # 在落子点 左右方向上循环查找得分形状
    for offset in range(-5, 1):
        # offset = -2
        pos = []
        for i in range(0, 6):
            if (m + (i + offset) * x_vector, n + (i + offset) * y_vector) in enemy_list:
                pos.append(2)
            elif (m + (i + offset) * x_vector, n + (i + offset) * y_vector) in my_list:
                pos.append(1)
            else:
                pos.append(0)
        tmp_shap5 = (pos[0], pos[1], pos[2], pos[3], pos[4])
        tmp_shap6 = (pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

        for (score, shape) in shape_score:
            if tmp_shap5 == shape or tmp_shap6 == shape:
                if tmp_shap5 == (1,1,1,1,1):
                    print('wwwwwwwwwwwwwwwwwwwwwwwwwww')
                if score > max_score_shape[0]:
                    max_score_shape = (score, ((m + (0+offset) * x_vector, n + (0+offset) * y_vector),
                                               (m + (1+offset) * x_vector, n + (1+offset) * y_vector),
                                               (m + (2+offset) * x_vector, n + (2+offset) * y_vector),
                                               (m + (3+offset) * x_vector, n + (3+offset) * y_vector),
                                               (m + (4+offset) * x_vector, n + (4+offset) * y_vector)), (x_vector, y_vector))

    # 计算两个形状相交， 如两个3活 相交， 得分增加 一个子的除外
    if max_score_shape[1] is not None:
        for item in score_all_arr:
            for pt1 in item[1]:
                for pt2 in max_score_shape[1]:
                    if pt1 == pt2 and max_score_shape[0] > 10 and item[0] > 10:
                        add_score += item[0] + max_score_shape[0]

        score_all_arr.append(max_score_shape)

    return add_score + max_score_shape[0]

# 评估函数
def evaluation(is_ai):
    total_score = 0

    if is_ai:
        my_list = ai_points
        enemy_list = player_points
    else:
        my_list = player_points
        enemy_list = ai_points

    score_all_arr = []  # 得分形状的位置 用于计算如果有相交 得分翻倍
    my_score = 0
    for pt in my_list:
        m = pt[0]
        n = pt[1]
        my_score += cal_score(m, n, 0, 1, enemy_list, my_list, score_all_arr)
        my_score += cal_score(m, n, 1, 0, enemy_list, my_list, score_all_arr)
        my_score += cal_score(m, n, 1, 1, enemy_list, my_list, score_all_arr)
        my_score += cal_score(m, n, -1, 1, enemy_list, my_list, score_all_arr)

    score_all_arr_enemy = []
    enemy_score = 0
    for pt in enemy_list:
        m = pt[0]
        n = pt[1]
        enemy_score += cal_score(m, n, 0, 1, my_list, enemy_list, score_all_arr_enemy)
        enemy_score += cal_score(m, n, 1, 0, my_list, enemy_list, score_all_arr_enemy)
        enemy_score += cal_score(m, n, 1, 1, my_list, enemy_list, score_all_arr_enemy)
        enemy_score += cal_score(m, n, -1, 1, my_list, enemy_list, score_all_arr_enemy)

    total_score = my_score - enemy_score*ratio*0.1

    return total_score


#  离最后落子的邻居位置最有可能是最优点
def order(blank_list):
    last_pt = ai_player_points[-1]
    for item in blank_list:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (last_pt[0] + i, last_pt[1] + j) in blank_list:
                    blank_list.remove((last_pt[0] + i, last_pt[1] + j))
                    blank_list.insert(0, (last_pt[0] + i, last_pt[1] + j))


def has_neightnor(pt):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (pt[0] + i, pt[1]+j) in ai_player_points:
                return True
    return False






def Chessboard():
    chessboard = GraphWin("Gobang Game based on Alpha-Beta MGT", GRID_WIDTH * COLUMN+BORDER*2+TIPS_SPACE, GRID_WIDTH * ROW+BORDER*2)
    chessboard.setBackground("brown")
    short_side=min(COLUMN,ROW)
    for i in range(0,GRID_WIDTH * short_side+1,GRID_WIDTH):
        Line(Point(i+BORDER,BORDER),Point(i+BORDER,GRID_WIDTH * ROW+BORDER)).draw(chessboard)
        Line(Point(BORDER,i+BORDER),Point(GRID_WIDTH * COLUMN+BORDER,i+BORDER)).draw(chessboard)
    start_line=GRID_WIDTH * (short_side+1)
    if ROW == short_side:
        while(start_line<=GRID_WIDTH * COLUMN):
            Line(Point(start_line+BORDER,BORDER),Point(start_line+BORDER,GRID_WIDTH * ROW+BORDER)).draw(chessboard)
            start_line=start_line+GRID_WIDTH
    else:
        while(start_line<=GRID_WIDTH * ROW):
            Line(Point(BORDER,start_line+BORDER),Point(GRID_WIDTH * COLUMN+BORDER,start_line+BORDER)).draw(chessboard)
            start_line=start_line+GRID_WIDTH
    return chessboard

def points_all_Init():
    for c in range(BORDER,BORDER+COLUMN+1):
        for r in range(BORDER,BORDER+ROW+1):
            points_all.append((c, r))

# True AI先手 False 玩家先手
def First_Hand():
    return False




if __name__ == '__main__':
    win = Chessboard()
    points_all_Init()

    replay = 0
    hand = First_Hand()

    while not replay:
        if hand:
            pos = ai()
            if pos in ai_player_points:
                message = Text(Point(200, 200), "不可用的位置" + str(pos[0]) + "," + str(pos[1]))
                message.draw(win)
                replay = 1

            ai_points.append(pos)
            ai_player_points.append(pos)

            piece = Circle(Point(GRID_WIDTH * pos[0], GRID_WIDTH * pos[1]), 16)
            piece.setFill('white')
            piece.draw(win)

            if game_win(ai_points):
                message = Text(Point(100, 100), "white win.")
                message.draw(win)
                replay = 1
            hand = hand + 1

        else:
            p2 = win.getMouse()
            if not ((round((p2.getX()) / GRID_WIDTH), round((p2.getY()) / GRID_WIDTH)) in ai_player_points):

                a2 = round((p2.getX()) / GRID_WIDTH)
                b2 = round((p2.getY()) / GRID_WIDTH)
                player_points.append((a2, b2))
                ai_player_points.append((a2, b2))

                piece = Circle(Point(GRID_WIDTH * a2, GRID_WIDTH * b2), 16)
                piece.setFill('black')
                piece.draw(win)
                if game_win(player_points):
                    message = Text(Point(100, 100), "black win.")
                    message.draw(win)
                    replay = 1

                hand = not hand

    message = Text(Point(100, 120), "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()
