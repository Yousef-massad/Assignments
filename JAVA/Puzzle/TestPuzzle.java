public class TestPuzzle {

   
    public static void main(String[] args) {

        Puzzle puzzle = new Puzzle();

        System.out.println(puzzle.getRoll());

        
        System.out.println(puzzle.getTenRolls());

        System.out.println(puzzle.getRandomLetter());

        
        System.out.println(puzzle.generatePassword());

        // Test getNewPasswordSet(): the number you pass = how many passwords you get
        System.out.println(puzzle.getNewPasswordSet(5));
    }
}
