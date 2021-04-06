//import java.lang.Math;

public class Gg 
{
    static void drei(long n)
    {
        int x = (int) Math.sqrt(n / 2);
        int y, p;
        y = p = 0;
        int count;
    
        if (x % 2 == 0)
            x--; 

        while (x > 0)
        {
            y = 2;
            if (n % x == 0)
            {
                count = 0;
            
                while (y <= x / 2)
                {
                    if (x % y == 0)
                    {
                        count++;
                    }
                    y++;
                }
            
                if (count == 0)
                {
                    p = x;
                    break;
                }
            }
            x -= 2;
        }
    
        System.out.println(p);
    }


    public static void main(String args[])
    {
        long n = 13195;
        drei(n); 
        
        n  =  600851475143l;
        drei(n);
    }
}
