using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication4
{
    class ArrayQueue<T>
    {
        private T[] q; // holds the array of items
        private int fp; // holds the index of the front of the line (inclusive)
        private int e; // holds the index of the end of the line (inclusive)
        private int n; // holds the length of the line
        private int size; // holds the maximum length of the buffer

        // default ArrayQueue objects have a max buffer length of 3
        public ArrayQueue()
        {
            size = 3;
            fp = 0;
            e = 0;
            n = 0;
            q = new T[size];
        }

        public ArrayQueue(int buf_len)
        {
            size = buf_len;
            fp = 0;
            e = 0;
            n = 0;
            q = new T[buf_len];
        }


        public void add(T val)
        {
            if (n == 0) // The queue is empty.
            {
                q[fp] = val;
                n += 1;
                return; // insert the element and return
            }
            if (n == size) // The queue is full and needs to be resized
            {
                resize();
            }

            e = (e + 1) % size; // update end pointer
            q[e] = val; // assign value at the end
            n++; // increase number of elements in the list

            return;

        }

        private void resize()
        {
            T[] b = new T[n * 2];
            int k;
            for (k = 0; k < n; k++)
            {
                b[k] = q[(fp + k) % size];
            }

            fp = 0;
            e = n - 1;
            q = b;
            size = n * 2;

            return;
        }

        public void print()
        {
            int k = fp;
            for (k = fp; k < n; k++)
            {
                Console.Write(q[k] + "  ");
            }
            Console.WriteLine();

        }
    }
}
