using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AssignmentConsoleApp1
{
    class student
    {
        public string name { get; set; }
        public int standard { get; set; } 
        public int rollno { get; set; }
        public double sub1 { get; set; }
        public double sub2 { get; set; }
        public double sub3 { get; set; }
        public double sub4 { get; set; }
        public double sub5 { get; set; }
        public double sum { get; set; }
        public double average { get; set; }

        public student(string name, int standard, int rollno, double sub1, double sub2, double sub3, double sub4, double sub5)
        {
            this.name = name;
            this.standard = standard;
            this.rollno = rollno;
            this.sub1 = sub1;
            this.sub2 = sub2;
            this.sub3 = sub3;
            this.sub4 = sub4;
            this.sub5 = sub5;
        }
        public void studentdetails()
        {
            Console.WriteLine("Name : "+Student.name);
            Console.WriteLine("Class : "+Student.standard);
            Console.WriteLine("Roll No : "+Student.rollno);
            Console.WriteLine("Marks in Physics     : "+Student.sub1);
            Console.WriteLine("Marks in Chemistry   : "+Student.sub2);
            Console.WriteLine("Marks in Mathematics : "+Student.sub3);
            Console.WriteLine("Marks in English     : "+Student.sub4);
            Console.WriteLine("Marks in Hindi       : "+Student.sub5);       
        }
        public void total()
        {
            sum = Student.sub1 + Student.sub2 + Student.sub3 + Student.sub4 + Student.sub5;
            average = sum / 5;
            Console.WriteLine("Total percentage : "+average);
        }
        public void grade(double num)
        {
            for(int i=0; i < 5; i++)
            {
                if (num > 90)
                {
                    Console.WriteLine(" Grade: " + "A");
                }
                else if(num > 80)
                {
                    Console.WriteLine(" Grade: " + "B");
                } 
                else if (num > 70)
                {
                    Console.WriteLine(" Grade: " + "C");
                }
                else if (num > 50)
                {
                    Console.WriteLine(" Grade: " + "D");
                }
                else
                {
                    Console.WriteLine(" Grade: " + "FAIL");
                }
            }
        }
        public void subjectgrade()
        {
            Console.WriteLine("Grade in Physics     : "+Student.grade(sub1));
            Console.WriteLine("Grade in Chemistry   : "+Student.grade(sub2));
            Console.WriteLine("Grade in Mathematics : "+Student.grade(sub3));
            Console.WriteLine("Grade in English     : "+Student.grade(sub4));
            Console.WriteLine("Grade in Hindi       : "+Student.grade(sub5)); 
        } 

    }
namespace AssignmentConsoleApp1
{
    class Program
    {
        public static void Main(string[] args)
        { 
            var Student = new student("Rithun",12,18,82,85,73,89,100);
            Student.studentdetails();
            Student.total();
            Console.WriteLine("Overall grade : "+Student.grade(average));
            Student.subjectgrade();
        }
    }
}
