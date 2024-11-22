-------------Recently Asked SQL Interview Questions:--

select * from emp

--1.if you know the highest sal by usiong this cmd we can filter
A.  select * from emp where sal=5000

--2.if you want first 5 recors from table,by usiong this cmd we can filter
A.select top 5 sal from emp

--3.write a query to display highest paid salary from table
 A.select * from emp
where sal=(select max(sal) from emp)


--4.write a query to diplay the emp details and 2nd highest salary 
A.select ename,job,sal from emp
where sal=(select max(sal) from emp
where sal<(select max(sal) from emp))

--5.To find duplicates ,we can follow this cmmd
A.select sal,count(*) from emp
group by sal
having count(*)>1