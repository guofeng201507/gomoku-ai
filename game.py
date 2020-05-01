from sys import exit

import pygame

from gomoku_ai import *
from gomoku import *
from render import GameRender

# run in terminal
if __name__ == '__main__':
    gomoku = Gomoku()
    render = GameRender(gomoku)

    # change the AI here, bigger the depth stronger the AI
    ai = gomokuAI(gomoku, BoardState.BLACK, 2)
    ai2 = gomokuAI(gomoku, BoardState.WHITE, 1)

    result = BoardState.EMPTY

    # enable ai here
    enable_ai = True
    enable_ai2 = False

    # edit if ai plays first
    ai.first_step()
    result = gomoku.get_chess_result()
    render.change_state()

    while True:
        # ai vs ai section
        if enable_ai2:
            ai2.one_step()
            result = gomoku.get_chess_result()
            if result != BoardState.EMPTY:
                print(result, "wins")
                break
            if enable_ai:

                ai.one_step()
                result = gomoku.get_chess_result()

                if result != BoardState.EMPTY:
                    print(result, "wins")
                    break
            else:
                render.change_state()

        # pygame event, player vs. ai section
        for event in pygame.event.get():
            # exit

            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # play a step
                if render.one_step():
                    result = gomoku.get_chess_result()
                else:
                    continue
                if result != BoardState.EMPTY:
                    break
                if enable_ai:

                    ai.one_step()
                    result = gomoku.get_chess_result()
                else:
                    render.change_state()

        # draw
        render.draw_chess()
        render.draw_mouse()

        if result != BoardState.EMPTY:
            render.draw_result(result)

        # update
        pygame.display.update()
