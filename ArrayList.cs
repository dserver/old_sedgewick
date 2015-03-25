using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication4
{
	class ArrayList<T>
	{
		private T[] memoryarray; // holds the actual array
		private int max_size = 5; // holds the actual size of memoryarray
		private int front_pointer; // holds the index of the first item in the array
		private int actual_size; // holds the number of elements in the memory array
		public ArrayList()
		{
			memoryarray = new T[max_size];
			front_pointer = 0;
			actual_size = 0;
		}
		
		public ArrayList(int newsize)
		{
			memoryarray = new T[newsize];
			front_pointer = 0;
			actual_size = 0;
		}
		
		public void add(T new_element, int position){
			if (actual_size == 0){
				memoryarray[front_pointer] = new_element;
				return;
			}
			
			if (actual_size == max_size){
				resize();
			}
			
			// shift elements j...i to j+1...i+1
			int j = (front_pointer + (actual_size - 1)) % max_size;
			for (; j >= (front_pointer + i) % max_size; j = (j-1) % max_size){
				memoryarray[(j + 1) % max_size] = memoryarray[j];
			}
			
			// insert at i
			memoryarray[(front_pointer + i) % max_size] = new_element;
			
			return;
		}
		
		public void add_fast(T new_element, int position){
			if (actual_size >= max_size)
				resize();
			
			if (i < actual_size/2) { 
				int y;
				for (y = front_pointer; y <= (front_pointer + position) % max_size; y = (y+1) % max_size){
					
				}
			}
		}
	
	}

}