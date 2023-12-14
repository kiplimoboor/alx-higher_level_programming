-- creates database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE states
  (
     id   INT UNIQUE NOT NULL auto_increment,
     name VARCHAR(256),
     PRIMARY KEY(id)
  ); 