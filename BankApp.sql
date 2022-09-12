create database Bankdb;
use Bankdb;
create table customer_info ( FullName varchar(255),
                           DOB varchar(255),
						   BankNo bigint,
                           EmailId Varchar(255),
                           Password1 varchar(255),
                           Balance float(20,2)); 
select * from customer_info;
