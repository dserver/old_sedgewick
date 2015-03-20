using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ConsoleApplication4
{
    class Program
    {
        static void Main(string[] args)
        {
            ElemArrayList<int> b = new ElemArrayList<int>();
            int x;
            for (x = 0; x <= 9; x++)
            {
                b.insert(x+1,x);
            }

            b.insert(11, 11);

            int y = 1;
        }
    }
}
