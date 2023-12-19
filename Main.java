import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        TicTacToe ttt = new TicTacToe();
        int row, col;
        while (true) {
            System.out.println("It's player " + ttt.getReadableTurn() + "'s turn");
            ttt.printBoard();
            System.out.print("Enter a row: ");
            row = scan.nextInt();
            System.out.print("Enter a column: ");
            col = scan.nextInt();
            if (!ttt.pickLocation(row, col)) {
                System.out.println("That isn't a valid input!");
                continue;
            }
            ttt.takeTurn(row, col);
            if (ttt.checkWin()) {
                ttt.turn++;
                System.out.println(ttt.getReadableTurn() + " won!");
                break;
            }
            if (ttt.checkTie()) {
                System.out.println("Tie game!");
                break;
            }
        }
        scan.close();
    }
}