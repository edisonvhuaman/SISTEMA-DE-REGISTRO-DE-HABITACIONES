-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3334
-- Tiempo de generación: 15-08-2022 a las 00:14:57
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `al3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alquiler`
--

CREATE TABLE `alquiler` (
  `ID_AL` char(4) DEFAULT NULL,
  `ID_CLIENTE` char(4) DEFAULT NULL,
  `F_PAGO` date DEFAULT NULL,
  `F_PAGADO` date DEFAULT NULL,
  `MONTO` decimal(11,2) DEFAULT NULL,
  `DEUDA` decimal(11,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `alquiler`
--

INSERT INTO `alquiler` (`ID_AL`, `ID_CLIENTE`, `F_PAGO`, `F_PAGADO`, `MONTO`, `DEUDA`) VALUES
('A001', 'C002', '2022-08-13', '2022-09-13', '150.00', '0.00'),
('A002', 'C001', '2022-08-11', '2022-09-11', '170.00', '0.00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `ID_CLIENTE` char(4) NOT NULL,
  `ID_HAB` char(4) NOT NULL,
  `NOMBRE` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`ID_CLIENTE`, `ID_HAB`, `NOMBRE`) VALUES
('C001', 'H002', 'FLOR'),
('C002', 'H003', 'LUIS'),
('C003', 'H005', 'DORIS'),
('C004', 'H001', 'EDISON');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hab`
--

CREATE TABLE `hab` (
  `ID_HAB` char(4) NOT NULL,
  `PRECIO` decimal(11,2) DEFAULT NULL,
  `DESCRIPCION` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `hab`
--

INSERT INTO `hab` (`ID_HAB`, `PRECIO`, `DESCRIPCION`) VALUES
('H001', '150.00', NULL),
('H002', '150.00', ''),
('H003', '178.00', ''),
('H004', '170.00', NULL),
('H005', '170.00', 'Esta al lado de la ventana en la calle');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alquiler`
--
ALTER TABLE `alquiler`
  ADD KEY `ID_CLIENTE` (`ID_CLIENTE`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`ID_CLIENTE`),
  ADD KEY `ID_HAB` (`ID_HAB`);

--
-- Indices de la tabla `hab`
--
ALTER TABLE `hab`
  ADD PRIMARY KEY (`ID_HAB`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alquiler`
--
ALTER TABLE `alquiler`
  ADD CONSTRAINT `alquiler_ibfk_1` FOREIGN KEY (`ID_CLIENTE`) REFERENCES `clientes` (`ID_CLIENTE`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`ID_HAB`) REFERENCES `hab` (`ID_HAB`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
