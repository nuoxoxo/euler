class Main {
    public static void main(String[] args)
    {
        int somme = 0;
        int i = 3;
        while (i < 1000)
        {
            if ((i % 3 == 0) || (i % 5 == 0))
            {
                somme += i;
            }
            i++;
        }

        System.out.print(somme);
    }
}
