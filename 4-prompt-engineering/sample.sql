-- create tables
CREATE TABLE company.departments (
    department_id INT IDENTITY (1, 1) PRIMARY KEY,
    department_name VARCHAR (255) NOT NULL
);

CREATE TABLE company.roles (
    role_id INT IDENTITY (1, 1) PRIMARY KEY,
    role_name VARCHAR (255) NOT NULL
);

CREATE TABLE company.employees (
    employee_id INT IDENTITY (1, 1) PRIMARY KEY,
    first_name VARCHAR (255) NOT NULL,
    last_name VARCHAR (255) NOT NULL,
    phone VARCHAR (25),
    email VARCHAR (255) NOT NULL,
    city VARCHAR (50),
    state VARCHAR (25),
    zip_code VARCHAR (5),
    department_id INT NOT NULL,
    role_id INT NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL (10, 2) NOT NULL,
    FOREIGN KEY (department_id) REFERENCES company.departments(department_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (role_id) REFERENCES company.roles(role_id) ON DELETE CASCADE ON UPDATE CASCADE
);
