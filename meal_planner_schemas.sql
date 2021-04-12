DROP DATABASE IF EXISTS meal_planner;

CREATE DATABASE meal_planner;

USE  meal_planner;

CREATE TABLE `User`(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(30),
    `password` VARCHAR(30)
);

CREATE TABLE Measurement(
    units VARCHAR(30) PRIMARY KEY,
    `type` VARCHAR(30)
);

CREATE TABLE Recipe(
    recipe_id INT PRIMARY KEY,
    recipe_name VARCHAR(300),
    added_by INT,
    image VARCHAR(100),

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
    calories_per_ml DECIMAL(5,2),
    calories_per_g DECIMAL(5,2)
);

CREATE TABLE Ingredients_In_Recipes(
    food_id INT,
    recipe_id INT,
    units VARCHAR(30),
    quantity DECIMAL(5,2),

    PRIMARY KEY(food_id,recipe_id),
    FOREIGN KEY(food_id) REFERENCES Food_Item(food_id) ON DELETE CASCADE, 
    FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE,
    FOREIGN KEY(units) REFERENCES Measurement(units) ON DELETE SET NULL
     
);

CREATE TABLE Meal_Plan(
    user_id INT,
    recipe_id INT,
    consumption_date DATE,
    serving VARCHAR(30),
    type_of_meal VARCHAR(30),

    PRIMARY KEY(user_id,recipe_id,consumption_date,type_of_meal),
    FOREIGN KEY(user_id) REFERENCES `User`(user_id) ON DELETE CASCADE, 
    FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id) ON DELETE CASCADE
);

CREATE TABLE Kitchen_Stock(
    user_id INT,
    food_id INT,
    quantity DECIMAL(5,2),
    units VARCHAR(30),

    PRIMARY KEY(user_id,food_id),
    FOREIGN KEY(user_id) REFERENCES `User`(user_id), 
    FOREIGN KEY(food_id) REFERENCES Food_Item(food_id),
    FOREIGN KEY(units) REFERENCES Measurement(units)
);

/* Stored procedure for getting the ingredients from a recipe*/
DELIMITER //
CREATE PROCEDURE get_ingredients( in id INT )
begin
    SELECT * FROM ingredients_in_recipes 
    JOIN food_item ON 
        ingredients_in_recipes.food_id=food_item.food_id 
    WHERE ingredients_in_recipes.recipe_id=38;
end //
DELIMITER ;

/* Stored procedure for getting the instructions from a recipe*/
DELIMITER //
CREATE PROCEDURE get_instructions( in id INT )
begin
    SELECT * FROM Instruction WHERE recipe_id=id;
end //
DELIMITER ;