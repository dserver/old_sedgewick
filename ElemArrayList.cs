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
            int j;
			T r_val = this.a[i]
			for (j=this.n-1; j>= i; j--) {
				this.a[j-1] = this.a[j]
			}
			
			return r_val;
        }

        private void resize()
        {
			if (this.n == this.a.Length -1 ){ # increase array size
				T[] b = new T[(this.a.Length * 2)];
				int i;
				for (i = 0; i < this.a.Length; i++)
					b[i] = this.a[i];
				this.a = b;
				return;
			}
			if (this.a.Length >= this.n * 3) {
				T[] b = new T[this.n * 2];
				int x;
				for (x=0; x < this.n; x++)
					b[x] = this.a[x];
				this.a = b;
				return;
			}
        }
    }
}
