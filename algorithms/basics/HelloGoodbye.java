/**
 * Example  of using  Java command line arguments based. This example is the 
 * first assignment from Algorithms Part I, lectured by Princeton University 
 * me on Coursera. 
 * 
 * One can enroll in this course through coursera.org/learn/algorithms-part1.
 * 
 */
public class HelloGoodbye {
    public static void main(String[] args) {
        if (args.length > 1) {
        System.out.println("Hello " + args[0] + " and " + args[1]);
        System.out.println("Goodbye " + args[1] + " and " + args[0]);
        } else {
            System.out.println("Usage: java HelloGoodbye Name1 Name2");
        }
    }
}
