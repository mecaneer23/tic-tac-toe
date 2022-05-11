#!/usr/bin/env python3

from tkinter import ttk, Tk, StringVar, messagebox
from functools import partial


def main():
    root = Tk()
    root.title("Tic-Tac-Toe")
    turn = True
    turn_display = StringVar(root, value="X's turn")
    buttons = [[StringVar(root, value="") for _ in range(3)] for _ in range(3)]

    def check_win(board_state):
        board = [board_state[i : i + 3] for i in range(0, 9, 3)]
        for i in range(3):  # check horizontals and verticals
            if (
                (board[0][i] == board[1][i] == board[2][i]) and board[0][i] is not None
            ) or (
                (board[i][0] == board[i][1] == board[i][2]) and board[i][0] is not None
            ):
                return "winner"
        if (
            (board[0][0] == board[1][1] == board[2][2])
            or (board[0][2] == board[1][1] == board[2][0])
        ) and board[1][
            1
        ] is not None:  # check diagonals
            return "winner"
        if None not in board_state:
            return "tie"
        return None

    def button_handler(x, y):
        nonlocal turn
        nonlocal turn_display
        nonlocal buttons
        if buttons[x][y].get() == "":
            buttons[x][y].set(f"{'X' if turn else 'O'}")
            turn = not turn
            turn_display.set(f"{'X' if turn else 'O'}'s turn")
        winner = check_win(
            [
                None if buttons[i][j].get() == "" else buttons[i][j].get() == "X"
                for i in range(3)
                for j in range(3)
            ]
        )
        if winner == "winner":
            win_message = f'{"O wins!" if turn else "X wins!"}'
        elif winner == "tie":
            win_message = "Tie!"
        else:
            return
        if messagebox.askyesno(
            title="Tic-Tac-Toe",
            message=f"{win_message}\nDo you want to play again?",
        ):
            root.destroy()
            main()
        else:
            exit()

    ttk.Style().configure("TLabel", font=("Helvetica", 32))
    ttk.Label(root, textvariable=turn_display).grid(
        row=0,
        column=1,
    )

    ttk.Style().configure("TButton", font=("Helvetica", 64), width=3)
    [
        ttk.Button(
            root,
            textvariable=buttons[i][j],
            command=partial(button_handler, i, j),
        ).grid(row=i + 1, column=j)
        for i in range(3)
        for j in range(3)
    ]
    root.mainloop()


if __name__ == "__main__":
    main()
