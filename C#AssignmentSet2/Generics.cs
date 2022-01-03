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
            Stack<int> num = new Stack<int>();
            
            num.Push(10);
            num.Push(20);
            num.Push(30);
            num.Push(40);
            num.Push(50);
            num.Push(60);
            num.Push(70);
            print(num);

            Console.WriteLine("\nTop Item is : {0}",num.Peek());

            Console.WriteLine("\nRemoved Top Item of Stack : " + num.Pop());  
            Console.WriteLine("\nNow Stack's Items are : ");
            print(num);
        }
        public static void print(Stack<int> numbers)
        {
            foreach(int n in numbers)
            {
                Console.Write(n + " | ");
            }
        }
    }
}
