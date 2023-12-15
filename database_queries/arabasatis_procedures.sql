-- araba tablosu için gerekli işlemler
create or alter procedure dbo.get_cars
as begin
	select * from dbo.cars where deleted = 0;
end;
go

create procedure [dbo].[add_car]
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