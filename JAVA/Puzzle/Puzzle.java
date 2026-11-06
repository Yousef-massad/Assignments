import java.util.Random;
import java.util.ArrayList; 

public class Puzzle {

    private Random randMachine = new Random();

    public int getRoll() {
        return randMachine.nextInt(20) + 1;
    }

    public ArrayList<Integer> getTenRolls() {
        ArrayList<Integer> randy = new ArrayList<Integer>();
        for (int i = 0; i < 10; i++) {
            randy.add(getRoll());
        }
        return randy;
    }


    public String getRandomLetter() {
        String[] letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};

        int i = randMachine.nextInt(letters.length);
        
        return letters[i];
        
    }

    public String generatePassword() {

        String word = "";   

        for (int i = 0; i < 8; i++) {
        
            word += getRandomLetter();
        }

        return word;
    }

    public ArrayList<String> getNewPasswordSet(int length) {
        ArrayList<String> romanreigns = new ArrayList<String>();   

        for (int i = 0; i < length; i++) {

            romanreigns.add(generatePassword());
        }
        return romanreigns;   
    }

} 
