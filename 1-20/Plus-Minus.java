import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
        // Write your code here
        int positiveCount = 0;
        int negativeCount = 0;
        int zeroCount = 0;
        
        for (int number : arr) {
            if (number > 0) {
                positiveCount++;
            }
            else if (number < 0) {
                negativeCount++;
            }
            else {
                zeroCount++;
            }
        }
        
        double totalNumbers = arr.size();
        
        double positiveRatio = (double) positiveCount/totalNumbers;
        double negativeRatio = (double) negativeCount/totalNumbers;
        double zeroRatio = (double) zeroCount/totalNumbers;
        
        System.out.println(String.format("%.6f", positiveRatio));
        System.out.println(String.format("%.6f", negativeRatio));
        System.out.println(String.format("%.6f", zeroRatio));
    }
}



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}
