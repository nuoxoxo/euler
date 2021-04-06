public class Demo
{
    public static boolean isPalin(int n)
    {
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

