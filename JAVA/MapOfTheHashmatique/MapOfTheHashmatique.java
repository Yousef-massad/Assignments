
import java.util.HashMap;

public class MapOfTheHashmatique {

    public static void main(String[] args) {

        // Create a HashMap
        HashMap<String, String> trackList = new HashMap<String, String>();

        // Add songs to the HashMap
        trackList.put("Starlight", "Far away, this ship is taking me far away.");
        trackList.put("Uprising", "They will not force us, they will stop degrading us.");
        trackList.put("Madness", "I, I can't get these memories out of my mind.");
        trackList.put("Resistance", "Is our secret safe tonight?");

        // Retrieve a song using its title
        String songLyrics = trackList.get("Starlight");

        System.out.println("Starlight: " + songLyrics);

        // Print all songs and their lyrics
        System.out.println("\n===== COMPLETE TRACK LIST =====");

        for (String track : trackList.keySet()) {
            System.out.println(track + ": " + trackList.get(track));
        }
    }
}
