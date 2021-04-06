class Main
{
    public static void main(String[] args)
    {
        int a, b, c;
        a = b = c = 1;
        
        int total, limit;
        limit = 4 * (int) Math.pow(10, 6);
        total = 0;

        while (c <= limit)
        {
            if (c % 2 == 0)
            {
                total += c;
            }
            c = a + b;
            a = b;
            b = c;
        }
        System.out.print(total);
    }
}
