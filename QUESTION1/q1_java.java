public class ReverseStringRecursive {
    public static void main(String[] args) {
        String input = "Hello, World!";
        String reversed = reverseString(input);
        System.out.println("Original: " + input);
        System.out.println("Reversed: " + reversed);
    }

    public static String reverseString(String str) {
        // Base case: If the string is empty or has only one character, return it.
        if (str.isEmpty() || str.length() == 1) {
            return str;
        }

        // Recursive case: Reverse the substring excluding the first character,
        // and then append the first character at the end.
        return reverseString(str.substring(1)) + str.charAt(0);
    }
}
