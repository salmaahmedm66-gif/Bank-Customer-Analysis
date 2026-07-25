-- Total number of customers
select count (*) as [Total_customers] 
from Bank 

-- Average balance
select ROUND(AVG(Balance),3)  [Avg_balance]
from Bank;

-- Top 10 customers by balance
select top 10 CustomerId,Surname,Geography,Balance
from Bank
order by Balance desc

-- Number of customers in each country
select Geography, count(*) As num_customers
from Bank
Group by Geography
order by num_customers 

 -- Average Age
select AVG (Age) [Avg_age]
from Bank

-- Active vs Inactive Customers
select IsActiveMember, count(*) as [Total customers]
from Bank
group by IsActiveMember

-- Customers who exited
select  Exited ,count(*) as [Total customers]
from Bank
group by Exited

-- Average Balance by Country
select Geography,ROUND(AVG(Balance),2)  AS Avg_Balance
from Bank
Group by Geography
order by Avg_Balance

-- Average Credit Score by Gender
select Gender, AVG(CreditScore) [Avg_CreditScore]
from Bank
group by Gender
