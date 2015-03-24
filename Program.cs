using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
//using System.Threading.Tasks;

/* To help remember bounds checking when splitting a list using n/2 and floor
for x in range(0, 30):
	l = [y for y in range(0, x)]
	print "#############################"
	print l
	print str(len(l)/2) + "    n = " + str(len(l))
	print "0..."+str(len(l)/2 - 1) + "    " + str(len(l)/2) + "..." + str(len(l)-1)
*/


// Use 3.5 on work computer to compile. do:
// set PATH=%PATH%;C:\Windows\Microsoft.NET\Framework\v3.5
// then csc.exe Program.cs; ./Program.exe + whatever classes you need
namespace ConsoleApplication4
{
    class Program
    {
        static void Main(string[] args)
        {
			int seed = 100100;
			Random rnd = new Random(seed);
			
			ArrayQueue<double> arrayq = new ArrayQueue<double>();
			int i;
			for (i=0;i<100;i++){
				arrayq.add(rnd.NextDouble());
			}
        }
		
		static void readFromFile(string filename){
			int counter = 0;
			string line;

			// Read the file and display it line by line.
			System.IO.StreamReader file = 
			   new System.IO.StreamReader(filename);
			while((line = file.ReadLine()) != null)
			{
			   Console.WriteLine (line);
			   counter++;
			}

			file.Close();
		}
		
		static void parseSites(string filename){
			int counter = 0;
			string line;
			// Read the file and display it line by line.
			System.IO.StreamReader file = 
			   new System.IO.StreamReader(filename);
			while((line = file.ReadLine()) != null)
			{
			   line.Split(' ');
			   Console.Write(line[0] + " " + line[1]);
			   Console.WriteLine();
			   counter++;
			}

			file.Close();
			
			
		}
    }
}
