#!/usr/bin/env python3
"""Tic Tac Toe for Python tkinter."""

from enum import Enum
from functools import partial
from itertools import chain
from tkinter import StringVar, Tk, messagebox, ttk
from typing import Callable, Iterable, Iterator, TypeVar, cast

T = TypeVar("T")
S = TypeVar("S")


class PlayAgain(Enum):
    """
    PlayAgain variants. Basically a boolean with a NoneType.

    YES, NO, DUNNO_YET
    """

    YES = 0
    NO = 1
    DUNNO_YET = 2


def recursive_map(
    func: Callable[[S], T],
    seq: Iterable[Iterable[S] | S],
) -> Iterator[Iterable[T] | T | list[T]]:
    """Map a function to a potentially multidimensional sequence."""
    for item in seq:
        if isinstance(item, Iterable):
            yield type(cast(Iterable[T], item))(
                recursive_map(func, cast(Iterable[S], item)),
            )
            continue
        yield func(item)


class TicTacToe:
    """Helper methods for tic tac toe calculations."""

    def __init__(self, tk_window: Tk) -> None:
        self.turn: bool = True
        self.root = tk_window
        self.buttons = [
            [StringVar(self.root, value="") for _ in range(3)] for _ in range(3)
        ]
        self.turn_display = StringVar(self.root, value="X's turn")

    def check_linears(self, board: list[list[str]]) -> bool:
        """Return true if the board contains 3 in a row or column."""
        for i in range(3):
            if ((board[0][i] == board[1][i] == board[2][i]) and board[0][i] != "") or (
                (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != ""
            ):
                return True
        return False

    def check_diagonals(self, board: list[list[str]]) -> bool:
        """Return true if the diagonals of board have 3 in a row."""
        return (
            (board[0][0] == board[1][1] == board[2][2])
            or (board[0][2] == board[1][1] == board[2][0])
        ) and board[1][1] != ""

    def has_winner(self, board: list[list[str]]) -> bool:
        """Check if there is a winner for a given board."""
        return self.check_diagonals(board) or self.check_linears(board)

    @staticmethod
    def get_button(button: StringVar) -> str:
        """Turn a button into a string."""
        return button.get()

    def get_turn(self) -> str:
        """Return the character representing turn."""
        return "X" if self.turn else "O"

    def button_handler(self, row: int, col: int) -> None:
        """
        Handle a button press.

        If possible to add a symbol, add it. Then check for a winner.
        """
        win_message = f"{self.get_turn()} wins!"
        if self.buttons[row][col].get() == "":
            self.buttons[row][col].set(self.get_turn())
            self.turn = not self.turn
            self.turn_display.set(f"{self.get_turn()}'s turn")
        winner = self.has_winner(
            list(map(list, recursive_map(self.get_button, self.buttons))),
        )
        if not winner:
            return
        if "" not in list(map(self.get_button, chain.from_iterable(self.buttons))):
            win_message = "Tie!"
        if messagebox.askyesno(  # pyright: ignore
            title="Tic-Tac-Toe",
            message=f"{win_message}\nDo you want to play again?",
        ):
            self.root.destroy()
            main()
        else:
            self.root.destroy()


def main() -> None:
    """Entry point for tic tac toe games."""
    root = Tk()
    root.title("Tic-Tac-Toe")
    game = TicTacToe(root)

    ttk.Style().configure("TLabel", font=("Helvetica", 32))  # pyright: ignore
    ttk.Label(root, textvariable=game.turn_display).grid(
        row=0,
        column=1,
    )

    ttk.Style().configure("TButton", font=("Helvetica", 64), width=3)  # pyright: ignore
    for i in range(3):
        for j in range(3):
            ttk.Button(
                root,
                textvariable=game.buttons[i][j],
                command=partial(game.button_handler, i, j),
            ).grid(row=i + 1, column=j)
    root.mainloop()


if __name__ == "__main__":
    main()
