CREATE TABLE Persons (
  PersonID int PRIMARY KEY,
  LastName varchar(255) NOT NULL,
  FirstName varchar(255),
  Addrss varchar(255),
  City varchar(255)
);

INSERT INTO Persons (PersonID, LastName, FirstName, Address, City)
VALUES (1, 'Doe', 'John', '123 Main St', 'New York');

SELECT* FROM latihan-Sheet1.csv;

SELECT City FROM Persons;