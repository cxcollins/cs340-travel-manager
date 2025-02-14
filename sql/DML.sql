-- Variables in these queries are denoted by %%variable_name%%.
-- User ID Queries
SELECT *
FROM `Users`
WHERE `user_id` = %%user_id%%;

INSERT INTO `Users` (`first_name`, `last_name`, `email`, `phone_number`, `creation_date`)
VALUES (%%first_name%%, %%last_name%%, %%email%%, %%phone_number%%, %%creation_date%%);

UPDATE `Users`
SET 
    `email` = %%email%%,
    `phone_number` = %%phone_number%%
WHERE `user_id` = %%user_id%%;

DELETE FROM `Users`
WHERE `user_id` = %%user_id%%;

-- Travel Plan Queries
SELECT *
FROM `Travel_Plans`
WHERE `user_id` = %%user_id%%;

INSERT INTO `Travel_Plans` (`user_id`, `destination_id`, `start_date`, `end_date`, `budget`, `status`)
VALUES (%%user_id%%, %%destination_id%%, %%start_date%%, %%end_date%%, %%budget%%, %%status%%);

UPDATE `Travel_Plans`
SET 
    `start_date` = %%start_date%%,
    `end_date` = %%end_date%%,
    `budget` = %%budget%%,
    `status` = %%status%%
WHERE `plan_id` = %%plan_id%%;

DELETE FROM `Travel_Plans`
WHERE `plan_id` = %%plan_id%%;

-- Destination Queries
SELECT *
FROM `Destinations`
WHERE `destination_id` = %%destination_id%%;

INSERT INTO `Destinations` (`country`, `state`, `city`)
VALUES (%%country%%, %%state%%, %%city%%);

UPDATE `Destinations`
SET 
    `country` = %%country%%,
    `state` = %%state%%,
    `city` = %%city%%
WHERE `destination_id` = %%destination_id%%;

DELETE FROM `Destinations`
WHERE `destination_id` = %%destination_id%%;

-- Activity Queries
SELECT *
FROM `Activities`
WHERE `activity_id` = %%activity_id%%;

INSERT INTO `Activities` (`name`, `type`)
VALUES (%%name%%, %%type%%);

UPDATE `Activities`
SET 
    `name` = %%name%%,
    `type` = %%type%%
WHERE `activity_id` = %%activity_id%%;

DELETE FROM `Activities`
WHERE `activity_id` = %%activity_id%%;

-- Hotel Queries
SELECT *
FROM `Hotels`
WHERE `destination_id` = %%destination_id%%;

INSERT INTO `Hotels` (`destination_id`, `name`, `cost_per_night`, `rating`)
VALUES (%%destination_id%%, %%name%%, %%cost_per_night%%, %%rating%%);

UPDATE `Hotels`
SET 
    `name` = %%name%%,
    `cost_per_night` = %%cost_per_night%%,
    `rating` = %%rating%%
WHERE `hotel_id` = %%hotel_id%%;

DELETE FROM `Hotels`
WHERE `hotel_id` = %%hotel_id%%;