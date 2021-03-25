DROP DATABASE IF EXISTS meal_planner;

CREATE DATABASE meal_planner;

USE  meal_planner;
CREATE TABLE `User`(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(30),
    `password` VARCHAR(30),
    address VARCHAR(80)
);

CREATE TABLE Measurement(
    units VARCHAR(30) PRIMARY KEY
);

CREATE TABLE Recipe(
    recipe_id INT PRIMARY KEY AUTO_INCREMENT,
    recipe_name VARCHAR(300),
    added_by INT,

    FOREIGN KEY(added_by) REFERENCES `User`(user_id) ON DELETE SET NULL
);

CREATE TABLE Instruction(
    recipe_id INT,
    step INT,
    description VARCHAR(200),

    PRIMARY KEY (recipe_id, step),
    FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE
);

CREATE TABLE Food_Item(
    food_id INT PRIMARY KEY AUTO_INCREMENT,
    food_name VARCHAR(150),
    calories_per_unit DECIMAL(5,2)
);

CREATE TABLE Ingredients_In_Recipes(
    food_id INT,
    recipe_id INT,
    units VARCHAR(30),
    quantity DECIMAL(5,2),
    total_calories DECIMAL(5,2),

    PRIMARY KEY(food_id,recipe_id),
    FOREIGN KEY(food_id) REFERENCES Food_Item(food_id) ON DELETE CASCADE, 
    FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE,
    FOREIGN KEY(units) REFERENCES Measurement(units) ON DELETE SET NULL
     
);

CREATE TABLE Meal(
    meal_id INT PRIMARY KEY,
    meal_name VARCHAR(30),
    consumption_date DATE,
    serving VARCHAR(30),
    colories DECIMAL(5,2),
    type_of_meal VARCHAR(30)
);



CREATE TABLE Users_Meals(
    meal_id INT,
    user_id INT,

    PRIMARY KEY(meal_id,user_id),
    FOREIGN KEY(meal_id) REFERENCES Meal(meal_id), 
    FOREIGN KEY(user_id) REFERENCES `User`(user_id)
);

CREATE TABLE Recipes_In_Meals(
    meal_id INT,
    recipe_id INT,

    PRIMARY KEY(meal_id,recipe_id),
    FOREIGN KEY(meal_id) REFERENCES Meal(meal_id), 
    FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE Kitchen_Stock(
    user_id INT,
    food_id INT,
    quantity DECIMAL(5,2),

    PRIMARY KEY(user_id,food_id),
    FOREIGN KEY(user_id) REFERENCES `User`(user_id), 
    FOREIGN KEY(food_id) REFERENCES Food_Item(food_id)
);