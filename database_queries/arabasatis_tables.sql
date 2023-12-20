use arabasatis;

drop table if exists log.cars;
drop table if exists log.users;
drop table if exists log.car_user;
drop table if exists dbo.car_sale;
drop table if exists dbo.services;
drop table if exists dbo.users;
drop table if exists dbo.cars;

create table dbo.users (  -- kullanici tablosu
 id int identity primary key,
 name varchar(50) not null,
 surname varchar(50) not null,
 username varchar(20) not null,
 password varchar(30) not null,
 is_staff bit not null constraint df_users_is_staff default 0,
 deleted bit constraint df_users_deleted default 0
);


create table dbo.cars (  -- arac tablosu
	id int identity primary key not null,
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
	deleted bit constraint df_cars_deleted default 0,
	img varchar(100) default ''
);

create table dbo.car_sale (  -- satilan araclarin logu
	id int identity primary key not null,
	user_id int constraint fk_log_car_sale_users foreign key references dbo.users(id) on delete cascade on update cascade,
	car_id int constraint fk_log_car_sale_cars foreign key references dbo.cars(id) on delete cascade on update cascade,
	price int not null,
	date date constraint df_log_car_sale_date default cast(getdate() as date)
);


create table dbo.services (  -- servis tablosu
	id int identity primary key not null,
	arac_id int foreign key references dbo.cars(id) on delete cascade on update cascade not null,
	type varchar(50) not null,
	notes varchar(200) not null,
	date date constraint df_log_service_date default cast(getdate() as date)
			constraint ck_services_date check (date >= getdate())
);


-- log tablolari
-- create schema log  -- boş bir sorgu dosyasında bir kere çalıştırılmalı

create table log.car_user (  -- aracin satis logu
	id int identity primary key not null,
	user_id int constraint fk_car_user_users foreign key references dbo.users(id) on delete cascade on update cascade,
	car_id int constraint fk_car_user_cars foreign key references dbo.cars(id) on delete cascade on update cascade,
	price int not null,
	data datetime not null constraint df_log_car_user_data default getdate()
);

create table log.cars (  -- arac loglari
	id int identity primary key not null,
	car_id int constraint fk_log_cars_cars foreign key references dbo.cars(id) on delete cascade on update cascade,
	process varchar(4) constraint ck_log_cars_process check(process in ('ADD', 'DEL', 'UPD')),
	data datetime not null constraint df_log_cars_data default getdate()
);

create table log.users(  -- kullanici loglari
	id int identity primary key not null,
	user_id int constraint fk_log_users_users foreign key references dbo.users(id) on delete cascade on update cascade,
	process varchar(4) constraint ck_log_users_process check(process in ('ADD', 'DEL', 'UPD')),
	data datetime not null constraint df_log_users_data default getdate()
);


-- kullanıcı ve hesapları ekleme
INSERT INTO dbo.users (name, surname, username, password, is_staff) SELECT 'admin', 'admin', 'admin', 'admin123', 1 WHERE NOT EXISTS (SELECT 1 FROM dbo.users WHERE username = 'admin');
INSERT INTO dbo.users (name, surname, username, password, is_staff) SELECT 'Mehmet Mete', 'Nak', 'burekboi', 'mete123', 0 WHERE NOT EXISTS (SELECT 1 FROM dbo.users WHERE username = 'burekboi');

