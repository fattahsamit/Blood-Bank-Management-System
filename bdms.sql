-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 22, 2021 at 06:48 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bdms`
--

-- --------------------------------------------------------

--
-- Table structure for table `donors`
--

CREATE TABLE `donors` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `blood_group` varchar(100) NOT NULL,
  `number` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `ailment` varchar(100) NOT NULL,
  `last_donation` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `donors`
--

INSERT INTO `donors` (`id`, `name`, `gender`, `blood_group`, `number`, `email`, `dob`, `ailment`, `last_donation`, `address`) VALUES
(12876, 'Fattah Samit', 'Male', 'O+', '01254325347', 'samit876@gmail.com', '14/04/1998', 'None', '19/11/2020', 'Mohammadpur, Dhaka'),
(12900, 'Kawsar Ahmed', 'Male', 'A-', '01734545666', 'kawsar@yahoo.com', '22/03/1997', 'None', '22/03/2021', 'Mirpur-10, Dhaka'),
(13442, 'Jannatul Ferdous', 'Female', 'B-', '01446536356', 'jjfrdous34@gmail.com', '14/02/1999', 'None', '04/09/2018', 'Shukrabad, Dhaka'),
(13555, 'Shamima Akhter', 'Female', 'AB-', '1554656363', 'shamima1@yahoo.com', '04/01/1996', 'Diabetes', '22/06/2019', 'Kodomtoli, Sylhet'),
(14524, 'Jonas Kabir', 'Male', 'B+', '01843252525', 'jondon@gmail.com', '22/04/1989', 'None', '20/02/2021', 'Shamoli, Dhaka'),
(14525, 'Masuda Khan', 'Female', 'B+', '01845535323', 'masu@gmail.com', '29/05/1994', 'None', '05/11/2020', 'Shamoli, Dhaka'),
(14828, 'Fahim Faisal', 'Male', 'A+', '01782767631', 'ffaisal@gmail.com', '01/11/1993', 'None', '15/08/2018', 'Mohammadpur, Dhaka'),
(15521, 'Khalid Nur', 'Male', 'A-', '01623588571', 'khalidnur@gmail.com', '04/02/1990', 'None', '10/03/2021', 'Mohakhali, Dhaka'),
(15609, 'Sadman Sakib ', 'Male', 'O+', '01552678020', 'ssakib@gmail.com', '25/05/1992', 'None', '10/08/2020', 'Mohammadpur, Dhaka'),
(15619, 'Sanzida Islam', 'Female', 'AB+', '01553546373', 'sanzida12@gmail.com', '11/12/1995', 'None', '27/02/2018', 'Uttara, Dhaka'),
(16219, 'Mehedi Hosain', 'Male', 'A-', '01962238321', 'mehedi99@gmail.com', '12/09/1999', 'None', '17/01/2021', 'Mirpur-1, Dhaka'),
(16275, 'Mahzabin Anika', 'Female', 'B-', '01774345853', 'Anika007@gmail.com', '28/01/1999', 'None', '18/03/2018', 'Gulshan, Dhaka'),
(16424, 'Ayub Baccu', 'Female', 'A-', '01914535417', 'ayub44@gmail.com', '22/11/1988', 'None', '02/07/2019', 'Mirpur-1, Dhaka'),
(17313, 'Zerin Haque', 'Female', 'AB+', '01525446412', 'zerinhq@gmail.com', '22/11/1995', 'None', '13/03/2018', 'Mirpur-1, Dhaka'),
(17327, 'Sadia Islam', 'Female', 'O+', '01835546359', 'sadia_420@gmail.com', '24/04/1996', 'None', '13/02/2019', 'Dhanmondi-7A, Dhaka'),
(17424, 'Shahrukh Khan', 'Male', 'O+', '01714436416', 'kingkhan@gmail.com', '13/12/1986', 'None', '22/05/2018', 'Gulshan, Dhaka'),
(17523, 'Elias Kanchon', 'Male', 'A+', '01515786512', 'elias21@gmail.com', '05/10/1991', 'Diebetes', '12/11/2018', 'Dhanmondi-7A, Dhaka'),
(17721, 'Shafin Ahmed', 'Male', 'O+', '01323788529', 'shafirockz@gmail.com', '27/03/2001', 'None', '13/02/2021', 'Kodomtoli, Sylhet'),
(17761, 'Muzahid Ahmed', 'Male', 'B-', '01563986771', 'muzahid1@gmail.com', '20/11/1997', 'Diebetes', '02/06/2020', 'Shukrabad, Dhaka'),
(18223, 'Maliha Hosen', 'Female', 'O+', '01915536313', 'maliha@gmail.com', '10/10/1999', 'None', '17/09/2017', 'Mohammadpur, Dhaka'),
(18332, 'Chowdhury Hoq', 'Male', 'O-', '01742784622', 'ch1990@gmail.com', '21/02/1990', 'None', '16/07/2020', 'Uttara, Dhaka'),
(18517, 'Nafis Ahmed', 'Male', 'B-', '01713786620', 'nafis99@gmail.com', '22/12/1999', 'Dust Allergy', '12/05/2019', 'Dhanmondi-7A, Dhaka'),
(18812, 'Purnima Islam', 'Female', 'B+', '01364546381', 'purnim10@gmail.com', '10/12/1989', 'Diabetes', '12/01/2018', 'Gulshan, Dhaka'),
(19223, 'Jamil Ahmed', 'Male', 'AB-', '01862788621', 'jamil21@gmail.com', '01/01/2001', 'None', '17/03/2021', 'Uttara, Dhaka'),
(19228, 'Nurul Huda', 'Male', 'O-', '01862788621', 'nur222@gmail.com', '26/09/2000', 'None', '17/07/2019', 'Mohammadpur, Dhaka'),
(19717, 'Tanzina Maisha', 'Female', 'A-', '01994546452', 'tanzina22@gmail.com', '22/11/1998', 'Dust Allergy', '18/02/2017', 'Dhanmondi-7A, Dhaka');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `donors`
--
ALTER TABLE `donors`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
