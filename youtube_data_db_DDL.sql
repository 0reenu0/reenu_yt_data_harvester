CREATE SCHEMA `youtube_data` DEFAULT CHARACTER SET utf8mb4 ;


CREATE TABLE `youtube_data`.`channel_data` (
  `channel_id` VARCHAR(255) NOT NULL,
  `channel_name` VARCHAR(255) NULL,
  `channel_type` VARCHAR(255) NULL,
  `channel_views` INT NULL,
  `channel_description` TEXT NULL,
  `channel_status` VARCHAR(255) NULL,
  PRIMARY KEY (`channel_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COMMENT = 'This table will used to store channel data eg. name, type, descripyion,status';

CREATE TABLE `youtube_data`.`playlist_data` (
  `channel_id` VARCHAR(255) NOT NULL,
  `playlist_id` VARCHAR(255) NOT NULL,
  `playlist_name` VARCHAR(255) NULL,
  PRIMARY KEY (`channel_id`,`playlist_id`),
  FOREIGN KEY (`channel_id`) REFERENCES  `youtube_data`.`channel_data`(`channel_id`)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COMMENT = 'This table will used to store playlist data of channels eg. id, name';

ALTER TABLE `youtube_data`.`playlist_data` 
ADD INDEX `pl_idx` (`playlist_id` ASC) VISIBLE,
ADD INDEX `ch_pl_idx` (`channel_id` ASC, `playlist_id` ASC) VISIBLE;

CREATE TABLE `youtube_data`.`video_data` (
  `playlist_id` VARCHAR(255) NOT NULL,
  `video_id` VARCHAR(255) NOT NULL,
  `video_title` VARCHAR(255) NULL,
  `video_description` TEXT NULL,
  `video_published_date` DATETIME NULL,
  `video_view_count` INT NULL,
  `video_like_count` INT NULL,
  `video_dislike_count` INT NULL,
  `video_favorite_count` INT NULL,
  `video_comment_count` INT NULL,
  `video_duration` INT NULL,
  `video_thumbnail` VARCHAR(255) NULL,
  `caption_status` VARCHAR(255) NULL,
  PRIMARY KEY (`playlist_id`,`video_id`),
  FOREIGN KEY (`playlist_id`) REFERENCES  `youtube_data`.`playlist_data`(`playlist_id`)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COMMENT = 'This table will used to store video data for each playlist of channels 
eg.  video id, title, description, pub_date,views,likes,dislikes,favorites,commentscount,duartion,
thumbnail and caption status';

ALTER TABLE `youtube_data`.`video_data` 
ADD INDEX `vid_idx` (`video_id` ASC) VISIBLE;


CREATE TABLE `youtube_data`.`comments` (
  `video_id` VARCHAR(255) NOT NULL,
  `comment_id` VARCHAR(255) NOT NULL,
  `comment_text` TEXT NULL,
  `comment_author` VARCHAR(255) NULL,
  `comment_published_date` DATETIME NULL,
  PRIMARY KEY (`video_id` , `comment_id`),
  FOREIGN KEY (`video_id`) REFERENCES  `youtube_data`.`video_data`(`video_id`)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COMMENT = 'This table will used to store comments data of each video eg. id, text, author name, pub date';



ALTER TABLE `youtube_data`.`channel_data` 
ADD COLUMN `channel_subscriber_count` INT NULL AFTER `channel_type`,
ADD COLUMN `channel_video_count` INT NULL AFTER `channel_view_count`,
CHANGE COLUMN `channel_views` `channel_view_count` INT NULL DEFAULT NULL ;

/*Date conversion error */
ALTER TABLE `youtube_data`.`video_data` 
CHANGE COLUMN `video_published_date` `video_published_date` VARCHAR(255) NULL DEFAULT NULL ;

/* Duration is sent in PT13H56M30S format*/
ALTER TABLE `youtube_data`.`video_data` 
CHANGE COLUMN `video_duration` `video_duration` VARCHAR(255) NULL DEFAULT NULL ;

/*Date conversion error */

ALTER TABLE `youtube_data`.`comments` 
CHANGE COLUMN `comment_published_date` `comment_published_date` VARCHAR(255) NULL DEFAULT NULL ;
