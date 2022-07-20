CREATE DATABASE book_store;
USE book_store;

--  Auther table
CREATE TABLE auther(
	A_ID int UNIQUE NOT NULL AUTO_INCREMENT,
    A_FNAME varchar (30) UNIQUE,
    A_LNAME varchar (30) UNIQUE
);
--  Customer table
CREATE TABLE Customers(
	C_ID int UNIQUE NOT NULL AUTO_INCREMENT,
    C_NAME varchar (30) UNIQUE,
    C_ADD varchar (30),
    B_STOCK varchar(30)
);

-- Book table
CREATE TABLE books(
	B_ID int UNIQUE NOT NULL AUTO_INCREMENT,
    B_TITLE varchar (30) UNIQUE,
    B_A_ID int,
    B_PUBLISHER varchar(30),
    B_PUB_DATE date,
    B_SUBJECT varchar(30),
    B_UNIT_PRIZE int,
    PRIMARY KEY (B_ID),
    FOREIGN KEY (B_A_ID) REFERENCES auther(A_ID)
);

-- reservation

CREATE TABLE reservation(
	R_ID int UNIQUE NOT NULL AUTO_INCREMENT,
    R_C_ID int,
    R_C_NAME varchar(30),
    R_B_ID int,
    R_B_TITLE varchar(30),
    R_B_QUANTITY int,
    PRIMARY KEY (R_ID),
    FOREIGN KEY (R_C_ID) REFERENCES customers(C_ID),
    FOREIGN KEY (R_C_NAME) REFERENCES customers(C_NAME),
    FOREIGN KEY (R_B_ID) REFERENCES books(B_ID),
    FOREIGN KEY (R_B_TITLE) REFERENCES books(B_TITLE)
)

ALTER TABLE auther AUTO_INCREMENT = 1;
ALTER TABLE customers AUTO_INCREMENT = 1;
ALTER TABLE books AUTO_INCREMENT = 1;
ALTER TABLE reservation AUTO_INCREMENT = 1;


