public class Demo
{
    public static boolean isPalin(int n)
    {
        /*
         *
        int temp, remainder, nreversed;
        
        temp = n;
        
        //remainder = 0;
        nreversed = 0;

        while (temp > 0);
        {
            remainder = temp % 10;
            nreversed = 10 * nreversed + remainder;
            temp /= 10;
        }

        if (nreversed == n)
            return true;

         *
         * palin-check works in c, don't know why not working here
         * luckily there's an another way to do it 
         * which is also easiter (belo)
         *
         */

        String s = Integer.toString(n);

        int i = 0;
        int j = s.length() - 1;
        
        while (i < j)
        {
            if (s.charAt(i) != s.charAt(j))
                return false;
            i++;
            j--;
        }
        
        return true;
    }

    public static void main(String args[])
    {
        int target, product, x, y;
        target = 0;
        x = 999;

        while (x > 99)
        {
            y = x;

            while (y > 99)
            {
                product = x * y;

                if (isPalin(product) == true && product > target)
                {
                    target = product;
                    break;
                }
                y--;
            }
            x--;
        }

        System.out.println(target);
    }
}

