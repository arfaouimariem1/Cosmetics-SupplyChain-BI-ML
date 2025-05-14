## Installation

### Installer les dépendances

```shell

# Create venv
python -m venv venv
#Access Venv
& ./venv/Scripts/Activate.ps1  
# install dependencies
pip3 install -r requirements.txt
```

### Postgresql

* create database named `supplychain`
* create table users
```sql
  CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      email VARCHAR(255) UNIQUE NOT NULL,
      password VARCHAR(255) NOT NULL,
      role VARCHAR(255) NOT NULL,
      fullname VARCHAR(255) NOT NULL
  );
```
* insert users
```sql
  INSERT INTO users (email, password, role, fullname)
  VALUES ('usereamil@gmail.com', 'pasword', 'admin', 'user name');
```
