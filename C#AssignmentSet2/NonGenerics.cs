using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AssignmentConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {  
            SortedList < int, string > sortedlist = new SortedList < int, string > ();  
         
            sortedlist.Add(2, "Monday");  
            sortedlist.Add(6, "Friday");
            sortedlist.Add(3, "Tuesday");  
            sortedlist.Add(7, "Saturday");  
            
            Console.WriteLine("The elements in the SortedList are:");  
            foreach(KeyValuePair < int, string > pair in sortedlist) 
            {  
                Console.WriteLine("{0} => {1}", pair.Key, pair.Value);  
            }  

            sortedlist.Add(4, "Wednesday");
            sortedlist.Add(1, "Sunday");   
            sortedlist.Add(5, "Thusday");

            Console.WriteLine("\nThe elements in the SortedList after adding some items are:");  
            foreach(KeyValuePair < int, string > pair in sortedlist) 
            {  
                Console.WriteLine("{0} => {1}", pair.Key, pair.Value);  
            }
        }
    }
}
