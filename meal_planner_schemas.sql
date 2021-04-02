DROP DATABASE IF EXISTS meal_planner;

CREATE DATABASE meal_planner;

USE  meal_planner;
CREATE TABLE `user`(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(30),
    `password` VARCHAR(30),
    address VARCHAR(80)
);

CREATE TABLE measurement(
    units VARCHAR(30) PRIMARY KEY,
    `type` VARCHAR(30)
);

CREATE TABLE recipe(
    recipe_id INT PRIMARY KEY,
    recipe_name VARCHAR(300),
    added_by INT,

    FOREIGN KEY(added_by) REFERENCES `user`(user_id) ON DELETE SET NULL
);

CREATE TABLE instruction(
    recipe_id INT,
    step INT,
    description VARCHAR(200),

    PRIMARY KEY (recipe_id, step),
    FOREIGN KEY(recipe_id) REFERENCES recipe(recipe_id) ON DELETE CASCADE
);

CREATE TABLE food_item(
    food_id INT PRIMARY KEY AUTO_INCREMENT,
    food_name VARCHAR(150),
    calories_per_ml DECIMAL(5,2),
    calories_per_g DECIMAL(5,2)
);

CREATE TABLE ingredients_in_recipes(
    food_id INT,
    recipe_id INT,
    units VARCHAR(30),
    quantity DECIMAL(5,2),

    PRIMARY KEY(food_id,recipe_id),
    FOREIGN KEY(food_id) REFERENCES food_item(food_id) ON DELETE CASCADE, 
    FOREIGN KEY(recipe_id) REFERENCES recipe(recipe_id) ON DELETE CASCADE,
    FOREIGN KEY(units) REFERENCES measurement(units) ON DELETE SET NULL
     
);

CREATE TABLE meal(
    meal_id INT PRIMARY KEY,
    meal_name VARCHAR(30),
    consumption_date DATE,
    serving VARCHAR(30),
    colories DECIMAL(5,2),
    type_of_meal VARCHAR(30)
);


CREATE TABLE users_meals(
    meal_id INT,
    user_id INT,

    PRIMARY KEY(meal_id,user_id),
    FOREIGN KEY(meal_id) REFERENCES meal(meal_id), 
    FOREIGN KEY(user_id) REFERENCES `user`(user_id)
);


CREATE TABLE kitchen_stock(
    user_id INT,
    food_id INT,
    quantity DECIMAL(5,2),
    units VARCHAR(30),

    PRIMARY KEY(user_id,food_id),
    FOREIGN KEY(user_id) REFERENCES `user`(user_id), 
    FOREIGN KEY(food_id) REFERENCES food_item(food_id),
    FOREIGN KEY(units) REFERENCES measurement(units)
);