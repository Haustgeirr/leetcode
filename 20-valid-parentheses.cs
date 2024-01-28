public class ValidParentheses
{
    public bool Test()
    {
        Debug.Log("hi");
    }

    public bool IsValid(string s)
    {
        // check if s is empty
        // check if s.len is odd
        // check if s[i] is valid

        // create new array half size of s
        // every new open increment open and set a[open]
        // every close check last open and see if valid
        // decrement open
        // remove last open from a[open]

        if (s.Length % 2 != 0) return false;

        char[] open = new char[s.Length];
        int qty = 0;

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{')
            {
                open[qty] = s[i];
                qty++;
            }
            else if (s[i] == ')' || s[i] == ']' || s[i] == '}')
            {
                // if the last one opened is the same as what we have here
                if (open[qty - 1] == s[i])
                {
                    open[qty - 1] = (char)0;
                    qty--;
                }
                else
                {
                    // return false;
                }
            }
        }

        if (qty == 0)
            return true;

        return false;
    }
}