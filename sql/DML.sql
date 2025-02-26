-- Variables in these queries are denoted by %%variable_name%%.

-- User ID Queries
-- Select a user by user_id
SELECT *
FROM `Users`
WHERE `user_id` = %%user_id%%;
-- Insert a new user into the Users table
INSERT INTO `Users` (`first_name`, `last_name`, `email`, `phone_number`, `creation_date`)
VALUES (%%first_name%%, %%last_name%%, %%email%%, %%phone_number%%, %%creation_date%%);
-- Update an existing user's information by user_id
UPDATE `Users`
SET 
    `first_name` = %%first_name%%,
    `last_name` = %%last_name%%,
    `email` = %%email%%,
    `phone_number` = %%phone_number%%,
    `creation_date` = %%creation_date%%
WHERE `user_id` = %%user_id%%;
-- Delete a user by user_id
DELETE FROM `Users`
WHERE `user_id` = %%user_id%%;

-- Travel Plan Queries
-- Select a travel plan by plan_id
SELECT *
FROM `Travel_Plans`
WHERE `plan_id` = %%plan_id%%;
-- Insert a new travel plan into the Travel_Plans table
INSERT INTO `Travel_Plans` (`user_id`, `destination_id`, `start_date`, `end_date`, `budget`, `status`)
VALUES (%%user_id%%, %%destination_id%%, %%start_date%%, %%end_date%%, %%budget%%, %%status%%);
-- Update an existing travel plan's information by plan_id
UPDATE `Travel_Plans`
SET 
    `user_id` = %%user_id%%,
    `destination_id` = %%destination_id%%,
    `start_date` = %%start_date%%,
    `end_date` = %%end_date%%,
    `budget` = %%budget%%,
    `status` = %%status%%
WHERE `plan_id` = %%plan_id%%;
-- Set destination_id to NULL for a travel plan if the destination is deleted
UPDATE `Travel_Plans`
SET `destination_id` = NULL
WHERE `destination_id` = %%destination_id%%;
-- Delete a travel plan by plan_id
DELETE FROM `Travel_Plans`
WHERE `plan_id` = %%plan_id%%;

-- Destination Queries
-- Select a destination by destination_id
SELECT *
FROM `Destinations`
WHERE `destination_id` = %%destination_id%%;
-- Insert a new destination into the Destinations table
INSERT INTO `Destinations` (`country`, `state`, `city`)
VALUES (%%country%%, %%state%%, %%city%%);
-- Update an existing destination's information by destination_id
UPDATE `Destinations`
SET 
    `country` = %%country%%,
    `state` = %%state%%,
    `city` = %%city%%
WHERE `destination_id` = %%destination_id%%;
-- Delete a destination by destination_id
DELETE FROM `Destinations`
WHERE `destination_id` = %%destination_id%%;

-- Destination Activity Queries
-- Select activities for a specific destination by destination_id
SELECT da.destination_activity_id, a.name, a.type
FROM `Destinations_Activities` AS da
JOIN `Activities` AS a ON da.activity_id = a.activity_id
WHERE da.destination_id = %%destination_id%%;
-- Insert a new activity for a destination into the Destinations_Activities table
INSERT INTO `Destinations_Activities` (`destination_id`, `activity_id`)
VALUES (%%destination_id%%, %%activity_id%%);
-- Update an existing activity for a destination by destination_activity_id
UPDATE `Destinations_Activities`
SET 
    `destination_id` = %%destination_id%%,
    `activity_id` = %%activity_id%%
WHERE `destination_activity_id` = %%destination_activity_id%%;
-- Delete an activity from a destination by destination_activity_id
DELETE FROM `Destinations_Activities`
WHERE `destination_activity_id` = %%destination_activity_id%%;

-- Activity Queries
-- Select an activity by activity_id
SELECT *
FROM `Activities`
WHERE `activity_id` = %%activity_id%%;
-- Insert a new activity into the Activities table
INSERT INTO `Activities` (`name`, `type`)
VALUES (%%name%%, %%type%%);
-- Update an existing activity's information by activity_id
UPDATE `Activities`
SET 
    `name` = %%name%%,
    `type` = %%type%%
WHERE `activity_id` = %%activity_id%%;
-- Delete an activity by activity_id
DELETE FROM `Activities`
WHERE `activity_id` = %%activity_id%%;

-- Hotel Queries
-- Select hotels by destination_id
SELECT *
FROM `Hotels`
WHERE `destination_id` = %%destination_id%%;
-- Insert a new hotel into the Hotels table
INSERT INTO `Hotels` (`destination_id`, `name`, `cost_per_night`, `rating`)
VALUES (%%destination_id%%, %%name%%, %%cost_per_night%%, %%rating%%);
-- Update an existing hotel's information by hotel_id
UPDATE `Hotels`
SET 
    `destination_id` = %%destination_id%%,
    `name` = %%name%%,
    `cost_per_night` = %%cost_per_night%%,
    `rating` = %%rating%%
WHERE `hotel_id` = %%hotel_id%%;
-- Delete a hotel by hotel_id
DELETE FROM `Hotels`
WHERE `hotel_id` = %%hotel_id%%;