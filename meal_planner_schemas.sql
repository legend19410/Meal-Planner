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


CREATE VIEW Total_Cal_Meal as(
    SELECT 
        recipe_id, sum(calories) as tot_calories
    FROM (
        SELECT  
            i.recipe_id as recipe_id, 
            CASE WHEN m.type = 'volume' THEN
                        (f.calories_per_ml * i.quantity *m.base_unit)
                WHEN m.type = 'mass' THEN
                        (f.calories_per_g * i.quantity *m.base_unit)
            END as calories
        FROM 
            ingredients_in_recipes i 
        JOIN food_item f on f.food_id = i.food_id
        JOIN measurement m on m.units = i.units
                
    ) as cal_per_i
    GROUP BY recipe_id    
);


DELIMITER //          
CREATE PROCEDURE getEmployees(IN user_id INT)          
BEGIN          
    select l.person_name, l.city 
    from lives l 
    join works w on l.person_name=w.person_name where w.company_name=companyName;
END //
DELIMITER ;

DELIMITER //
CREATE procedure createRandomMealPlan()
wholeblock:BEGIN
   DECLARE anyVariableName1 INT ;
   Declare anyVariableName3 int;
   DECLARE anyVariableName2 VARCHAR(255);
   SET anyVariableName1 =1 ;
   SET anyVariableName3 =10;
   SET anyVariableName2 = '';
loop_label: FORLOOP
   IF anyVariableName1 > anyVariableName3 THEN
      LEAVE loop_label;
   END IF;
   SET anyVariableName2 = CONCAT(anyVariableName2 ,anyVariableName1 ,',');
   SET anyVariableName1 = anyVariableName1 + 1;
   ITERATE loop_label;
   END FORLOOP;
SELECT anyVariableName2;
END//
DELIMITER ;