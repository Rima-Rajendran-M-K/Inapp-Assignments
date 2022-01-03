using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AssignmentConsoleApp1
{
    class Program
    {
        static void Main()
        {
            var Student = new student("Rithun", 12, 18, 82, 85, 73, 92, 100);
            Console.WriteLine("Details of the student");
            Student.studentdetails(Student);
            Console.WriteLine("\nOverall grade and percentage of the student");
            Student.total(Student);
            Console.WriteLine("\nGrade in each subject");
            Student.subjectgrade(Student);
        }
    }
}
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
        public void studentdetails(student Student)
        {
            Console.WriteLine("Name                 : " + Student.name);
            Console.WriteLine("Class                : " + Student.standard);
            Console.WriteLine("Roll No              : " + Student.rollno);
            Console.WriteLine("Marks in Physics     : " + Student.sub1);
            Console.WriteLine("Marks in Chemistry   : " + Student.sub2);
            Console.WriteLine("Marks in Mathematics : " + Student.sub3);
            Console.WriteLine("Marks in English     : " + Student.sub4);
            Console.WriteLine("Marks in Hindi       : " + Student.sub5);
        }
        public void total(student Student)
        {
            sum = Student.sub1 + Student.sub2 + Student.sub3 + Student.sub4 + Student.sub5;
            average = sum / 5;
            Console.WriteLine("Total percentage : " + average);
            Console.Write("Overall grade : ");
            grade(Student.average);
        }
        public void grade(double num)
        {
            if (num > 90)
            {
                Console.WriteLine("A");
            }
            else if (num > 80)
            {
                Console.WriteLine("B");
            }
            else if (num > 70)
            {
                Console.WriteLine("C");
            }
            else if (num > 50)
            {
                Console.WriteLine("D");
            }
            else
            {
                Console.WriteLine("FAIL");
            }
        }
        public void subjectgrade(student Student)
        {
            Console.Write("Grade in Physics     : ");
            grade(Student.sub1);
            Console.Write("Grade in Chemistry   : ");
            grade(Student.sub2);
            Console.Write("Grade in Mathematics : ");
            grade(Student.sub3);
            Console.Write("Grade in English     : ");
            grade(Student.sub4);
            Console.Write("Grade in Hindi       : ");
            grade(Student.sub5);
        }
    }
}
