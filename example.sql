-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 18, 2020 at 09:05 AM
-- Server version: 5.5.20
-- PHP Version: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `example`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE IF NOT EXISTS `bill` (
  `dated` varchar(50) NOT NULL,
  `customer` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `item` varchar(50) NOT NULL,
  `rate` varchar(50) NOT NULL,
  `quantity` varchar(2) NOT NULL,
  `cost` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`dated`, `customer`, `phone`, `item`, `rate`, `quantity`, `cost`) VALUES
('2019-11-13 11:10:37.997874', 'asmita', '7654221', 'momos', '15', '3', '45'),
('2019-11-13 11:16:54.355327', 'ankita', '636375', 'burger', '20', '2', '40'),
('2019-11-13 11:17:42.745960', 'vani', '98643256', 'chat', '20', '2', '40'),
('2019-11-13 11:18:11.088744', 'savita', '6535477', 'eggroll', '20', '4', '80'),
('2019-11-13 11:18:41.146309', 'roma', '3446788', 'burger', '20', '2', '40'),
('2019-11-13 11:19:16.130589', 'adi', '764329', 'springroll', '15', '3', '45'),
('2019-11-13 11:19:45.068100', 'mahi', '9876326', 'panipuri', '10', '3', '30'),
('2019-11-13 11:20:21.778403', 'pinki', '45678', 'chawmin ', '20', '3', '60');

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE IF NOT EXISTS `item` (
  `name` varchar(50) NOT NULL,
  `rate` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`name`, `rate`, `type`) VALUES
('burger', '20', 'snacks'),
('momos', '15', 'snacks'),
('chat', '20', 'snacks'),
('chawmin ', '20', 'snacks'),
('panipuri', '30', 'snacks'),
('eggroll', '20', 'snacks'),
('springroll', '15', 'snacks');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `Userid` varchar(15) NOT NULL,
  `password` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`Userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Userid`, `password`) 
VALUES('abc', '123');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
