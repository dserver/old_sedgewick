

public class HelloWorld {

    public static void main(String[] args) {
        
        double t = 9.0;
        while (Math.abs(t - 9.0/t) > .001)
        {
            t = (9.0/t + t) / 2.0;
        }
        
        StdOut.printf("%.5f\n", t);
    }
    
    // Shows how to compute averages of numbers read in from a file
    public static void computeAverages()
    {
        In fileIn = new In("numbers.txt");
        double sum = 0.0;
        int cnt = 0;
        while (!fileIn.isEmpty())
        {
            sum += fileIn.readDouble();
            cnt++;
        }
        
        double avg = sum / cnt;
        StdOut.printf("Average: %.2f\n", avg);
    }
    
    // shows how to print graphs of functions
    public static void drawFunctionValues()
    {
        int[] values = new int[100];
        for (int i = 0; i < 100; i++)
        {
            values[i] = StdRandom.uniform(1, 100);
        }
        
        StdDraw.setXscale(0, 100);
        StdDraw.setYscale(0,100);
        StdDraw.setPenRadius(.05);
        
        for (int i = 0; i < 100; i++)
        {
            double x = i;
            double y = 0;
            double rw = .05;
            double rh = values[i];
            StdDraw.filledRectangle(x, y, rw, rh);
        }
        
        
    }

}
