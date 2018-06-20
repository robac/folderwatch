SET NAMES utf8;

CREATE DATABASE `tftpbackup`;

USE `tftpbackup`;

CREATE TABLE `backup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `src_filename` varchar(255) COLLATE utf8_czech_ci NOT NULL,
  `dst_filename` varchar(255) COLLATE utf8_czech_ci NOT NULL,
  `src_directory` varchar(4096) COLLATE utf8_czech_ci NOT NULL,
  `dst_directory` varchar(4096) COLLATE utf8_czech_ci NOT NULL,
  `size` int(11) NOT NULL,
  `moved` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `src_filename` (`src_filename`),
  KEY `moved` (`moved`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

CREATE USER 'tftpbackup'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON tftpbackup.backup TO 'tftpbackup'@'localhost';

