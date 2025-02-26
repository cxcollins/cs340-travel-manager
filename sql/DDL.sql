-- Disable commits and foreign key checks to avoid issues during table creation and data insertion
SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- Create Users table to store user information
CREATE OR REPLACE TABLE `Users` (
    `user_id` INT NOT NULL UNIQUE AUTO_INCREMENT, -- Unique user ID
    `first_name` VARCHAR(255) NOT NULL, -- User's first name
    `last_name` VARCHAR(255) NOT NULL, -- User's last name
    `email` VARCHAR(255) NOT NULL, -- User's email address
    `phone_number` VARCHAR(15) NOT NULL, -- User's phone number
    `creation_date` DATE NOT NULL, -- Date when the user was created
    PRIMARY KEY (`user_id`) -- Primary key constraint
);

-- Create Travel_Plans table to store travel plans for users
CREATE OR REPLACE TABLE `Travel_Plans` (
    `plan_id` INT NOT NULL UNIQUE AUTO_INCREMENT, -- Unique plan ID
    `user_id` INT NOT NULL, -- ID of the user who created the plan
    `destination_id` INT, -- ID of the destination
    `start_date` DATE, -- Start date of the travel plan
    `end_date` DATE, -- End date of the travel plan
    `budget` DECIMAL(10, 2) NOT NULL DEFAULT 99999.99, -- Budget for the travel plan
    `status` ENUM('PENDING', 'BOOKED', 'COMPLETED') NOT NULL DEFAULT 'PENDING', -- Status of the travel plan
    PRIMARY KEY (`plan_id`), -- Primary key constraint
    FOREIGN KEY (`user_id`) REFERENCES `Users`(`user_id`) ON DELETE CASCADE, -- Foreign key constraint referencing Users table
    FOREIGN KEY (`destination_id`) REFERENCES `Destinations`(`destination_id`) ON DELETE SET NULL -- Foreign key constraint referencing Destinations table
);

-- Create Destinations table to store destination information
CREATE OR REPLACE TABLE `Destinations` (
    `destination_id` INT NOT NULL UNIQUE AUTO_INCREMENT, -- Unique destination ID
    `country` VARCHAR(255) NOT NULL, -- Country of the destination
    `state` VARCHAR(255), -- State of the destination (optional)
    `city` VARCHAR(255) NOT NULL, -- City of the destination
    PRIMARY KEY (`destination_id`) -- Primary key constraint
);

-- Create Destinations_Activities table to store activities available at destinations
CREATE OR REPLACE TABLE `Destinations_Activities` (
    `destination_activity_id` INT NOT NULL UNIQUE AUTO_INCREMENT, -- Unique destination activity ID
    `destination_id` INT NOT NULL, -- ID of the destination
    `activity_id` INT NOT NULL, -- ID of the activity
    FOREIGN KEY (`destination_id`) REFERENCES `Destinations`(`destination_id`) ON DELETE CASCADE, -- Foreign key constraint referencing Destinations table
    FOREIGN KEY (`activity_id`) REFERENCES `Activities`(`activity_id`) ON DELETE CASCADE -- Foreign key constraint referencing Activities table
);

-- Create Activities table to store activity information
CREATE OR REPLACE TABLE `Activities` (
    `activity_id` INT NOT NULL UNIQUE AUTO_INCREMENT, -- Unique activity ID
    `name` VARCHAR(255) NOT NULL, -- Name of the activity
    `type` VARCHAR(255) NOT NULL, -- Type of the activity
    PRIMARY KEY (`activity_id`) -- Primary key constraint
);

-- Create Hotels table to store hotel information
CREATE OR REPLACE TABLE `Hotels` (
    `hotel_id` INT NOT NULL AUTO_INCREMENT, -- Unique hotel ID
    `destination_id` INT NOT NULL, -- ID of the destination where the hotel is located
    `name` VARCHAR(255) NOT NULL, -- Name of the hotel
    `cost_per_night` DECIMAL(10, 2) NOT NULL, -- Cost per night to stay at the hotel
    `rating` DECIMAL(2, 1) NOT NULL DEFAULT 0.0, -- Rating of the hotel
    PRIMARY KEY (`hotel_id`), -- Primary key constraint
    FOREIGN KEY (`destination_id`) REFERENCES `Destinations`(`destination_id`) ON DELETE CASCADE -- Foreign key constraint referencing Destinations table
);

-- Insert sample data into Users table
INSERT INTO `Users` (`first_name`, `last_name`, `email`, `phone_number`, `creation_date`) 
VALUES ('LeBron', 'James', 'lebronjames@gmail.com', '503-214-1244', '2025-01-04'),
    ('Damian', 'Lillard', 'damianlillard@gmail.com', '503-932-4392', '2025-01-25'),
    ('Kevin', 'Durant', 'kevindurant@gmail.com', '503-738-2181', '2025-02-06');

-- Insert sample data into Travel_Plans table
INSERT INTO `Travel_Plans` (`user_id`, `destination_id`, `start_date`, `end_date`, `budget`, `status`)
VALUES (2, 1, '2025-01-07', '2025-01-09', 2000.00, 'COMPLETED'),
    (1, 2, '2025-07-20', '2025-08-20', 1500.00, 'BOOKED'),
    (3, 2, '2025-09-01', '2025-09-03', 2500.00, 'PENDING');

-- Insert sample data into Destinations table
INSERT INTO `Destinations` (`country`, `state`, `city`)
VALUES ('Japan', NULL, 'Tokyo'),
       ('United States', 'Hawaii', 'Honolulu'),
       ('France', NULL, 'Paris');

-- Insert sample data into Destinations_Activities table
INSERT INTO `Destinations_Activities` (`destination_id`, `activity_id`)
VALUES (1, 2),
       (2, 1),
       (3, 2);

-- Insert sample data into Activities table
INSERT INTO `Activities` (`name`, `type`)
VALUES ('Snorkeling or Diving', 'Outdoor'),
       ('City Landmark Tour', 'Sightseeing'),
       ('Museum Exploration', 'Cultural');
       
-- Insert sample data into Hotels table
INSERT INTO `Hotels` (`destination_id`, `name`, `cost_per_night`, `rating`)
VALUES (3, 'Luxury Seine View Hotel', 400.00, 5.0),
       (2, 'Waikiki Beach Resort', 350.00, 4.8),
       (1, 'Ginza Luxury Towers', 380.00, 4.9);

-- Test queries to verify data
SELECT * FROM `Users`;
SELECT * FROM `Travel_Plans`;
SELECT * FROM `Destinations`;
SELECT * FROM `Destinations_Activities`;
SELECT * FROM `Activities`;
SELECT * FROM `Hotels`;

-- Re-enable commits and foreign key checks
SET FOREIGN_KEY_CHECKS=1;
COMMIT;