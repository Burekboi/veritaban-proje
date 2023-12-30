-- dbo.cars tablosuna yeni veri eklendiğinde log.cars tablosuna process değeri 'INS' olan bir ekleme yapar
create or alter trigger trgCarsInsert on dbo.cars after insert as begin
	insert into log.cars (car_id, process) select id, 'INS' from inserted;
end;
go

-- dbo.cars tablosuna verilere güncelleme yapıldığında log.cars tablosuna;
-- deleted değeri 0 ise process değeri 'UPD' olan bir ekleme yapar
-- deleted değeri 1 ise process değeri 'DEL' olan bir ekleme yapar
create or alter trigger trgCarsUpdated on dbo.cars after update as begin
	if (select deleted from inserted) = 0
		insert into log.cars (car_id, process) select id, 'UPD' from inserted;
	else
		insert into log.cars (car_id, process) select id, 'DEL' from inserted;
end;
go


-- dbo.users tablosuna yeni veri eklendiğinde log.users tablosuna process değeri 'INS' olan bir ekleme yapar
create or alter trigger trgUsersInsert on dbo.users after insert as begin
	insert into log.users (user_id, process) select id, 'INS' from inserted;
end;
go

-- dbo.users tablosuna verilere güncelleme yapıldığında log.users tablosuna;
-- deleted değeri 0 ise process değeri 'UPD' olan bir ekleme yapar
-- deleted değeri 1 ise process değeri 'DEL' olan bir ekleme yapar
create or alter trigger trgUsersUpdated on dbo.users after update as begin
	if (select deleted from inserted) = 0
		insert into log.users (user_id, process) select id, 'UPD' from inserted;
	else
		insert into log.users (user_id, process) select id, 'DEL' from inserted;
end;
go
