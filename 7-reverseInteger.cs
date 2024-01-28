public class Solution
{
    public int Reverse(int x)
    {
        int r = 0;
        // int neg = (x < 0) ? -1 : 1;
        // x *= neg;

        while (x > 0)
        {
            int lastInt = x % 10;
            x /= 10;
            // try
            // {
            //     checked
            //     {
            //         r = r * 10 + lastInt;
            //     }
            // }
            // catch
            // {
            //     return 0;
            // }
            if (r > int.MaxValue / 10 || r == int.MaxValue / 10 && lastInt > 7) return 0;
            if (r < int.MinValue / 10 || r == int.MinValue / 10 && lastInt < -8) return 0;
        }

        // return (neg == -1) ? r * -1 : r;
        return r;
    }
}