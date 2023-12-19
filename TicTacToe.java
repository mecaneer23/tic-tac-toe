public class TicTacToe {
    public int turn;
    private String[][] board = new String[3][3];

    public TicTacToe() {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                board[i][j] = "-";
            }
        }
    }

    public int getTurn() {
        return turn;
    }

    public String getReadableTurn() {
        return turn % 2 == 0 ? "X" : "O";
    }

    public void printBoard() {
        String[] keys = { "  ", "0 ", "1 ", "2 " };

        System.out.println("  0 1 2");
        for (int i = 0; i < board.length; i++) {
            System.out.print(keys[i + 1]);
            for (String play : board[i]) {
                System.out.print(play + " ");
            }
            System.out.println();
        }
    }

    public boolean pickLocation(int row, int col) {
        if (!(row < board[0].length && col < board.length)) {
            return false;
        }
        return board[row][col].equals("-");
    }

    public void takeTurn(int row, int col) {
        if (pickLocation(row, col)) {
            board[row][col] = getReadableTurn();
            turn++;
        }
    }

    public boolean checkRow() {
        for (int i = 0; i < 3; i++) {
            if (board[i][0].equals(board[i][1]) && board[i][0].equals(board[i][2]) && !board[i][0].equals("-")) {
                return true;
            }
        }
        return false;
    }

    public boolean checkCol() {
        for (int i = 0; i < 3; i++) {
            if (board[0][i].equals(board[1][i]) && board[0][i].equals(board[2][i]) && !board[0][i].equals("-")) {
                return true;
            }
        }
        return false;
    }

    public boolean checkDiag() {
        return ((board[0][0].equals(board[1][1]) && board[0][0].equals(board[2][2]))
                || (board[2][0].equals(board[1][1]) && board[2][0].equals(board[0][2]))
                        && !board[1][1].equals("-"));
    }

    public boolean checkWin() {
        return checkCol() ^ checkRow() ^ checkDiag();
    }

    public boolean checkTie() {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == "-") {
                    return false;
                }
            }
        }
        return true;
    }
}