using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication4
{

    public class ElemArrayList<T>
    {
        public int n; // size of the ArrayList
        private T[] a;


        public ElemArrayList() {
            this.a = new T[5];
            this.n = 0;

        }

        public T get(int i){
            return this.a[i];
        }


        public void insert(T x, int i)
        {
            if (this.n == this.a.Length - 1) {
                this.resize(); // resize array to twice current size if need be
            }

            int j = i;
            for (j = this.n; j >= i; j--)
            {
                this.a[j + 1] = this.a[j]; // shift all elements from i to n right 1 position
            }
            this.a[i] = x; // put x in position i
            this.n++; // increment the size of the list

            return;
        }

        public T remove(int i){
            T b;
            return b;
        }

        private void resize()
        {
            T[] b = new T[(this.a.Length * 2)];
            int i;
            for (i = 0; i < this.a.Length; i++)
                b[i] = this.a[i];
            this.a = b;
            return;
        }
    }
}
