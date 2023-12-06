drop table dbo.users;
create table dbo.users (
 id int identity primary key,
 name varchar(50) not null,
 surname varchar(50) not null,
 username varchar(20) not null,
 password varchar(30) not null,
 is_staff bit not null constraint df_users_is_staff default 0,
 deleted bit constraint df_deleted default 0
);

drop table dbo.cars;
create table dbo.cars (
	id int primary key not null,
	model varchar(50) not null,
	year int not null constraint ck_cars_year check(year >= 1980 and year <= year(getdate())),
	price int not null,
	state varchar(20) not null,
	engine_capacity int not null,
	fuel_type varchar(20) not null,
	gear_type varchar(20) not null,
	traction_type varchar(20) not null,
	horse_power int not null,
	deleted bit constraint df_cars_deleted default 0
);