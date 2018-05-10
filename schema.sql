-- Copyright 2009 FriendFeed
--
-- Licensed under the Apache License, Version 2.0 (the "License"); you may
-- not use this file except in compliance with the License. You may obtain
-- a copy of the License at
--
--     http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
-- WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
-- License for the specific language governing permissions and limitations
-- under the License.

-- To create the database:
--   CREATE DATABASE blog;
--   GRANT ALL PRIVILEGES ON blog.* TO 'blog'@'localhost' IDENTIFIED BY 'blog';
--
-- To reload the tables:
--   mysql --user=blog --password=blog --database=blog < schema.sql

SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

/*
MySQL Data Transfer
Source Host: 47.104.68.55
Source Database: release
Target Host: 47.104.68.55
Target Database: release
Date: 2018/5/10 18:48:09
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for album
-- ----------------------------
DROP TABLE IF EXISTS `album`;
CREATE TABLE `album` (
  `album_id` int(16) NOT NULL AUTO_INCREMENT,
  `album_name` varchar(20) NOT NULL,
  `album_description` varchar(50) DEFAULT NULL,
  `cover_id` int(16) DEFAULT NULL,
  `user_id` int(16) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `edit_date` datetime DEFAULT NULL,
  PRIMARY KEY (`album_id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_id` int(16) DEFAULT NULL,
  `user_id` int(16) DEFAULT NULL,
  `comment_body` varchar(255) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `feed_id` int(16) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for dianzan
-- ----------------------------
DROP TABLE IF EXISTS `dianzan`;
CREATE TABLE `dianzan` (
  `dianzan_id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_id` int(16) DEFAULT NULL,
  `user_id` int(16) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `feed_id` int(16) DEFAULT NULL,
  PRIMARY KEY (`dianzan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=303 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for feed
-- ----------------------------
DROP TABLE IF EXISTS `feed`;
CREATE TABLE `feed` (
  `feed_id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_id` int(16) DEFAULT NULL,
  `user_id` int(16) DEFAULT NULL,
  `reason` varchar(500) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`feed_id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for photo
-- ----------------------------
DROP TABLE IF EXISTS `photo`;
CREATE TABLE `photo` (
  `photo_id` int(11) NOT NULL AUTO_INCREMENT,
  `album_id` int(16) DEFAULT NULL,
  `user_id` int(16) DEFAULT NULL,
  `photo_name` varchar(50) DEFAULT NULL,
  `photo_description` varchar(255) DEFAULT NULL,
  `update_date` varchar(50) DEFAULT NULL,
  `file_name` varchar(150) DEFAULT NULL,
  `is_public` char(2) DEFAULT NULL,
  PRIMARY KEY (`photo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=240 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `name` varchar(100) CHARACTER SET utf8 NOT NULL,
  `hashed_password` varchar(1000) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `nickname` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `user_description` varchar(1000) CHARACTER SET utf8 COLLATE utf8_german2_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;
