using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Customer
{
    class Call
    {
        public char CallType { get; set; }
        public int Minutes { get; set; }
        public Customer Cust { get; set; }
        public Call(Customer cust, char tc, int minutes)
        {
            Cust = cust;
            CallType = tc;
            Minutes = minutes;
        }

        public void valueCall()
        {
            if (CallType == 'Г')
                Cust.Balance -= Minutes * 5;
            else
            if (CallType == 'М')
                Cust.Balance -= Minutes * 1;
        }

    }
    class Customer
    {
        public string Name { get; set; }
        public double Balance { get; set; }
        public Call CustCall { get; set; }

        public Customer(string name, double balance = 100)
        {
            Name = name;
            Balance = balance;
        }

        public override string ToString() => $"Клиент: {Name} имеет баланс: {Balance}";
        
        public void RecordPayment(double amountPaid)
        {
            if (amountPaid > 0)
                Balance += amountPaid;
        }

        public void RecordCall(char callType, int minutes)
        {
            CustCall = new Call(this, callType, minutes);
            CustCall.valueCall();
            //if (callType == 'Г')
            //    Balance -= minutes * 5;
            //else
            //    if (callType == 'М')
            //        Balance -= minutes * 1;
        }
    }

    class CustomerTest
    {
        static void Main(string[] args)
        {
            Customer Ivan = new Customer("Иван Петров", 500);
            Customer Elena = new Customer("Елена Иванова");
            Ivan.RecordCall('Г', 12);
            Elena.RecordCall('М', 25);

            Console.WriteLine(Ivan);
            Console.WriteLine(Elena);

        }
    }
}
