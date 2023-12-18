-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pair_12
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pair_12
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pair_12` DEFAULT CHARACTER SET utf8 ;
USE `pair_12` ;

-- -----------------------------------------------------
-- Table `pair_12`.`Ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pair_12`.`Ventas` (
  `ID_Cliente` VARCHAR(100) NOT NULL,
  `ID_Producto` VARCHAR(100) NOT NULL,
  `Fecha_Venta` DATETIME NOT NULL,
  `Cantidad` INT NOT NULL,
  `Total` FLOAT NOT NULL,
  PRIMARY KEY (`ID_Cliente`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
