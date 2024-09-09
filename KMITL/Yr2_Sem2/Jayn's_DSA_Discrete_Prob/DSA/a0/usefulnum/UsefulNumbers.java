// (Optional) Practice Exercise
// Inside a class named UsefulNumbers, write a program that prints out the number of seconds in a century (i.e., 100 years). 
// To practice declaring variables in Java, your code will perform exactly the following steps:

// Declare a variable secondsInAMinute of an appropriate type and set it to the correct value. Remember that there are 60 seconds in a minute.
// Declare a variable secondsInAnHour of an appropriate type and set it to the correct value by referring to the variable above. Remember that there are 60 minutes in an hour.
// Declare a variable secondsInADay of an appropriate type and set it to the correct value by referring to the variable above. Remember that there are 24 hours in a day.
// Declare a variable secondsInAYear of an appropriate type and set it to the correct value by referring to the variable above. Remember that there are 365 days in a year. (NB: We're cheating. Let's pretend we don't care about leap years!)
// Declare a variable secondsInACentury of an appropriate type and set it to the correct value by referring to the variable above . Remember that there are 100 years in a century.
// Print the final value out using printf, like so:

// // Your awesome computation leading up to
// // secondsInACentury

// System.out.printf("One century contains %d seconds.\n", secondsInACentury);
// Of course, all these should live inside the main function like we did for hello world. You should also learn more about Java's printf by googling the term.

// (Hint: The answer is 3153600000)

public class UsefulNumbers {
    public static void main(String[] args) {
        double secondsInAMinute = 60;
        double secondsInAnHour = secondsInAMinute * 60;
        double secondsInADay = secondsInAnHour * 24;
        double secondsInAYear = secondsInADay * 365;
        double secondsInACentury = secondsInAYear * 100;
        System.out.printf("One century contains %f seconds.\n", secondsInACentury);
    }
}