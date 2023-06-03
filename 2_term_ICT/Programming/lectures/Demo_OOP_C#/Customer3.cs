using System;

/*
Расширить возможности компании, добавив наличие у клиента тарифного плана,
в каждом из которых есть тип звонка («городской» и «мобильный»):
 - Повременный: «городской» (5 руб./мин.) и «мобильный» (1 руб./мин.);
 - После10МинутВ2РазаДешевле: после 10 минут звонка на городской номер каждая вторая минута бесплатно; в остальном как Повременный;
 - ПлатиМеньшеДо5Минут: до 5 минут разговора в 2 раза дешевле тарифа Повременный, после - в 2 раза дороже.
Решение:
    Реализация тарификации по модели «включения/делегации».
    Добавить новый класс CallPlan (Тариф):
      - поле name: наименование тарифа;
      -	метод record_call(): выполняет обработку звонка клиента в зависимости от:
         -- типа звонка: «городской» (5 руб./мин.) и «мобильный» (1 руб./мин.);
         -- количества минут разговора.
    Наследники классаCallPlan (прочие тарифы) будут иметь изменять необходимые атрибуты.
 */
namespace Customer
{
    // Абстрактный класс для всех тарифных планов
    abstract class CallPlan
    {
        public string Name = "Абстрактный тариф";
        public Call CustCall { get; set; }
        public virtual void recordCall(int minutes)
        {
            CustCall.valueCall(minutes);
        }
        public void SetTypeCall(Call typeCall)
        {
            CustCall = typeCall;
        }
    }
    class CallPlanSimple : CallPlan
    {
        public CallPlanSimple()
        {
            Name = "Простой повременный";
        }
        
        public override void recordCall(int minutes)
        {
            base.recordCall(minutes);
        }
    }
    class CallPlanFree2andMinuteAfter10 : CallPlan
    {
        public int BonusMinutes { get; set; }
        public CallPlanFree2andMinuteAfter10()
        {
            Name = "После 10 минут каждая минута в два раза дешевле";
        }

        public override void recordCall(int minutes)
        {
            if (minutes > 10)
            {
                BonusMinutes = (minutes - 10) / 2;
            }
            else
                BonusMinutes = 0;
            
            base.recordCall(minutes-BonusMinutes);
        }
    }
    class CallPlanTwiceCheaperFirst5Minutes : CallPlan
    {
        public int LimitCheap { get; private set; }
        public int CheapMinutes { get; set; }
        public int ExpensiveMinutes { get; set; }
        public CallPlanTwiceCheaperFirst5Minutes(int limitCheap)
        {
            Name = "Плати меньше до...";
            LimitCheap = limitCheap;
        }
        public override void recordCall(int minutes)
        {
            if (minutes > LimitCheap)
            {
                CheapMinutes = LimitCheap;
                ExpensiveMinutes = minutes - LimitCheap;
            }
            else
            {
                CheapMinutes = minutes;
                ExpensiveMinutes = 0;
            }
            
            base.recordCall(CheapMinutes / 2 + ExpensiveMinutes * 2);
        }
    }

    class Call
    {
        public char CallType { get; set; }
        public Customer Cust { get; set; }
        public Call(Customer cust, char tc)
        {
            Cust = cust;
            CallType = tc;
        }

        public void valueCall(int minutes)
        {
            if (CallType == 'Г')
                Cust.Balance -= minutes * 5;
            else
            if (CallType == 'М')
                Cust.Balance -= minutes * 1;
        }

    }
    class Customer
    {
        public string Name { get; set; }
        public double Balance { get; set; }
        public Call CustCall { get; set; }
        public CallPlan CustPlan { get; set; }

        public Customer(string name, double balance = 100, CallPlan callPlan = null)
        {
            Name = name;
            Balance = balance;
            if (callPlan == null)
            {
                CustPlan = new CallPlanSimple();
            }
            else
                CustPlan = callPlan;
        }

        public override string ToString() => $"Клиент: {Name} имеет баланс: {Balance}";
        
        public void RecordPayment(double amountPaid)
        {
            if (amountPaid > 0)
                Balance += amountPaid;
        }

        public void RecordCall(char callType, int minutes)
        {
            CustCall = new Call(this, callType);
            CustPlan.SetTypeCall(CustCall);
            CustPlan.recordCall(minutes);
        }
    }

    class CustomerTest
    {
        static void Main(string[] args)
        {
            Customer Ivan = new Customer("Иван Петров", 500);
            Customer Elena = new Customer("Елена Иванова");
            Ivan.RecordCall('Г', 20);
            Elena.RecordCall('М', 25);

            Console.WriteLine(Ivan);
            Console.WriteLine(Elena);

            CallPlanFree2andMinuteAfter10 cpFree = new CallPlanFree2andMinuteAfter10();
            Customer Petr = new Customer("Петр Иванов", 500, cpFree);
            Petr.RecordCall('Г', 20);
            Console.WriteLine(Petr);

            CallPlanTwiceCheaperFirst5Minutes cpTCFM = new CallPlanTwiceCheaperFirst5Minutes(20);
            Customer Alina = new Customer("Алина Апина", 100, cpTCFM);
            Alina.RecordCall('М', 25);
            Console.WriteLine(Alina);
        }
    }
}
