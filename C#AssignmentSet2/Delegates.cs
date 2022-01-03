using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AssignmentConsoleApp1
{
    class rectangle
    {
        public delegate void recArea(double a, double b);
        public delegate void recPerimeter(double a, double b);

        public void area(double x, double y)
        {
            Console.WriteLine("Area is: {0}", (x * y));
        }
  
        public void perimeter(double x, double y)
        {
            Console.WriteLine("Perimeter is: {0} ", 2 * (x + y));
        }

        static void Main(string[] args)
        {  
            rectangle rect = new rectangle();
            recArea area_obj = new recArea(rect.area);
            recPerimeter perimeter_obj = new recPerimeter(rect.perimeter);

            area_obj(6.3, 4.2);
            perimeter_obj(6.3, 4.3); 
            Console.WriteLine();
            area_obj(16.3, 10.3);
            perimeter_obj(16.3, 10.3); 
        }
    }
}
