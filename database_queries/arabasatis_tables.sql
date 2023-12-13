use arabasatis;

drop table log.car_sale;
drop table log.cars;
drop table log.users;
drop table dbo.car_user;
drop table dbo.users;
drop table dbo.cars;

create table dbo.users (
 id int identity primary key,
 name varchar(50) not null,
 surname varchar(50) not null,
 username varchar(20) not null,
 password varchar(30) not null,
 is_staff bit not null constraint df_users_is_staff default 0,
 deleted bit constraint df_users_deleted default 0
);


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
	is_sold bit constraint df_cars_is_sold default 0,
	deleted bit constraint df_cars_deleted default 0
);


create table dbo.car_user (
	id int primary key not null,
	user_id int constraint fk_car_user_users foreign key references dbo.users(id) on delete cascade on update cascade,
	car_id int constraint fk_car_user_cars foreign key references dbo.cars(id) on delete cascade on update cascade,
	price int not null
);


-- log tablolar�

-- create schema log  -- boş bir sorgu dosyasında bir kere çalıştırılmalı

create table log.car_sale (  -- sat�lan ara�lar�n logu
	id int primary key not null,
	user_id int constraint fk_log_car_sale_users foreign key references dbo.users(id) on delete cascade on update cascade,
	car_id int constraint fk_log_car_sale_cars foreign key references dbo.cars(id) on delete cascade on update cascade,
	date date constraint df_log_car_sale_date default cast(getdate() as date)
);

create table log.cars (  -- ara� loglar�
	id int identity primary key not null,
	car_id int constraint fk_log_cars_cars foreign key references dbo.cars(id) on delete cascade on update cascade,
	process varchar(4) constraint ck_log_cars_process check(process in ('ADD', 'DEL', 'UPD')),
	data datetime not null constraint df_log_cars_data default getdate()
);

create table log.users(  -- kullan�c� loglar�
	id int primary key not null,
	user_id int constraint fk_log_users_users foreign key references dbo.users(id) on delete cascade on update cascade,
	process varchar(4) constraint ck_log_users_process check(process in ('ADD', 'DEL', 'UPD')),
	data datetime not null constraint df_log_users_data default getdate()
);