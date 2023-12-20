-- araba tablosu için gerekli işlemler
create or alter procedure dbo.get_cars
as begin
	select * from dbo.cars where deleted = 0;
end;
go

create or alter procedure [dbo].[add_car]
	@model varchar(50),
	@year int,
	@price int,
	@state varchar(30),
	@engine_capacity int,
	@fuel_type varchar(20),
	@gear_type varchar(20),
	@traction_type varchar(20),
	@horse_power int,
	@image varchar(100)
as begin
	insert into dbo.cars (model, year, price, state, engine_capacity, fuel_type, gear_type, traction_type, horse_power, img)
		values (@model, @year, @price, @state, @engine_capacity, @fuel_type, @gear_type, @traction_type, @horse_power, @image);
end;
go

create or alter procedure dbo.upd_car
	@id int,
	@model varchar(50),
	@year int,
	@price int,
	@state varchar(30),
	@engine_capacity int,
	@fuel_type varchar(20),
	@gear_type varchar(20),
	@traction_type varchar(20),
	@horse_power int
as begin
	update dbo.cars set
		model = @model,
		year = @year,
		price = @price,
		state = @state,
		engine_capacity = @engine_capacity,
		fuel_type = @fuel_type,
		gear_type = @gear_type,
		traction_type = @traction_type,
		horse_power = @horse_power
	where id = @id;
end;
go

create or alter procedure dbo.delete_car
	@id int
as begin
	update dbo.cars set deleted = 1 where id = @id;
end;
go


-- kullanıcı tablosu için gerekli işlemler
create or alter procedure dbo.get_users
as begin
	select * from dbo.users where deleted = 0;
end;
go

create or alter procedure dbo.add_user
	@name varchar(50),
	@surname varchar(50),
	@username varchar(20),
	@password varchar(30),
	@is_staff bit
as begin
	insert into dbo.users (name, surname, username, password, is_staff)
		values (@name, @surname, @username, @password, @is_staff);
end;
go

create or alter procedure dbo.upd_user
	@id int,
	@name varchar(50),
	@surname varchar(50),
	@username varchar(20),
	@password varchar(30),
	@is_staff bit
as begin
	update dbo.users set
		name = @name,
		surname = @surname,
		username = @username,
		password = @password,
		is_staff = @is_staff
	where id = @id;
end;
go

create or alter procedure dbo.delete_user
	@id int
as begin
	update dbo.users set deleted = 1 where id = @id;
end;
go


-- araba satışı
create or alter procedure dbo.delete_user
	@user_id int,
	@car_id int
as begin
	insert into dbo.car_user(user_id, car_id) values (@user_id, @car_id);
	update dbo.car set is_sold = 1 where id = @car_id;
end;
go


create or alter procedure dbo.proc_car_sale
	 @user_id int,
	 @car_id int
as begin
	insert into dbo.car_sale (user_id, car_id, price) select top 1 @user_id, @car_id, price from dbo.cars where id = @car_id;
end;
go


create or alter procedure dbo.get_services
	@user_id int = 0
as begin
	select (u.name + ' ' + u.surname) as 'user', c.model as 'car_model', s.type as 'types', s.notes as 'notes'
		from dbo.car_sale as cs
			left join dbo.services as s on s.arac_id = cs.car_id
			left join dbo.cars as c on c.id = cs.car_id
			left join dbo.users as u on u.id = cs.user_id
			where (@user_id = 0) or (@user_id != 0 and @user_id = cs.user_id);
end;
go


create or alter procedure dbo.add_service
	@arac_id int,
	@type varchar(50),
	@date date,
	@notes varchar(100)
as begin
	insert into dbo.services (arac_id, type, date, notes) values (@arac_id, @type, @date, @notes);
end;
go


create   procedure dbo.get_sold_cars
	@user_id int = 0
as begin
	select u.id as 'user_id', (u.name + ' ' + u.surname) as 'username', cs.car_id as 'car_id', c.model as 'model', cs.price as 'price', cs.date as 'sold_date'
		from dbo.car_sale as cs
		left join dbo.users as u on u.id = cs.user_id
		left join dbo.cars as c on c.id = cs.car_id
		where (@user_id = 0) or (@user_id = cs.user_id);
end;
GO

