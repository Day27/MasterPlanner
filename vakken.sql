-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 21 jul 2018 om 15:02
-- Serverversie: 10.1.21-MariaDB
-- PHP-versie: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `masterplanner`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `vakken`
--

CREATE TABLE `vakken` (
  `Code` varchar(6) NOT NULL,
  `Naam` varchar(255) NOT NULL,
  `Studiepunten` int(2) NOT NULL,
  `Project` tinyint(1) NOT NULL,
  `Examenvorm` varchar(255) NOT NULL,
  `Semester` int(1) NOT NULL,
  `Groep` varchar(30) NOT NULL,
  `Moeilijkheid` int(1) NOT NULL,
  `Taal` char(2) NOT NULL DEFAULT 'EN'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `vakken`
--

INSERT INTO `vakken` (`Code`, `Naam`, `Studiepunten`, `Project`, `Examenvorm`, `Semester`, `Groep`, `Moeilijkheid`, `Taal`) VALUES
('C07I6A', 'ICT-recht', 4, 0, 'Schriftelijk', 2, 'AVO', 0, 'NL'),
('D0H36A', 'Innovation Management and Strategy', 6, 1, 'Schriftelijk, project, presentatie', 1, 'AVO', 0, 'EN'),
('D0I69A', 'ICT Service Management ', 6, 0, 'Schriftelijk', 2, 'AVO', 0, 'EN'),
('G0B01A', 'Intellectual Property Management', 4, 0, 'Schriftelijk', 2, 'AVO', 0, 'EN'),
('G0B30A', 'Computational Methods for Astrophysical Applications', 6, 1, 'Mondeling, project, report, presentatie', 1, 'COMP2', 0, 'EN'),
('G0B36A', 'Computergrafiek 2', 4, 1, 'Mondeling, werkstuk', 2, 'ANDERE', 0, 'NL'),
('G0O00A', 'Statistische modellen & data-analyse', 6, 1, 'Schriftelijk, take-home', 2, 'DATA1', 0, 'NL'),
('G0P61B', 'Getaltheorie', 6, 0, 'Schriftelijk, take-home', 2, 'CRYPTO2', 0, 'NL'),
('G0Q63B', 'Complexiteitstheorie', 6, 1, 'Mondeling, report, presentatie, medewerking', 2, 'CRYPTO2', 0, 'NL'),
('G0Q66C', 'Fundamenten van Computergrafiek', 3, 0, 'Mondeling', 1, 'ANDERE', 0, 'NL'),
('H00K1A', 'Engineering Economy', 3, 0, 'Schriftelijk, mondeling', 1, 'AVO', 0, 'EN'),
('H01G1A', 'Computergesteund probleemoplossen ', 3, 1, 'Mondeling, schriftelijk', 1, 'COMP1', 0, 'NL'),
('H02A5A', 'Computer Vision', 4, 1, 'Project, presentatie', 2, 'ANDERE', 0, 'EN'),
('H02C1A', 'Machine Learning and Inductive Inference', 4, 0, 'Schriftelijk', 1, 'DATA2', 0, 'EN'),
('H02D1A', 'Genetic Algorithms and Evolutionary Computing', 4, 1, 'Schriftelijk', 1, 'DATA2', 0, 'EN'),
('H02D3A', 'Support Vector Machines: Methods and Applications', 4, 1, 'Mondeling, schriftelijk', 2, 'DATA1', 0, 'EN'),
('H02X6A', 'Bedrijfservaring: Wiskundige ingenieurstechnieken', 3, 0, 'Verslag, presentatie', 1, 'AVO', 0, 'NL'),
('H03D7A', 'Numerieke simulatie van differentiaalvergelijkingen', 6, 0, 'Mondeling, open vragen', 1, 'KERN', 0, 'NL'),
('H03E5A', 'Gevallenstudies: wiskundige ingenieurstechnieken', 3, 1, 'Paper/Werkstuk, Mondeling', 2, 'KERN', 0, 'NL'),
('H03E8A', 'Computergestuurde regeltechniek', 6, 1, 'Mondeling, verdedigen project', 2, 'KERN', 0, 'NL'),
('H03F0B', 'Technisch-wetenschappelijke software', 5, 1, 'Mondeling, Verslag, Take-home', 1, 'KERN', 0, 'NL'),
('H03F2A', 'Meten van fysische grootheden', 3, 1, 'Mondeling, Verslag', 1, 'PROCES1', 0, 'NL'),
('H03F7A', 'Wavelets with Applications in Signal and Image Processing', 6, 1, 'Mondeling', 1, 'COMP1', 0, 'EN'),
('H03F9A', 'Parallel Computing', 4, 0, 'Mondeling', 1, 'COMP1', 0, 'EN'),
('H03G1A', 'Numerical Linear Algebra', 6, 0, 'Mondeling', 1, 'COMP1', 0, 'EN'),
('H03G3B', 'Deterministische en stochastische integratietechnieken', 6, 0, 'Mondeling', 2, 'COMP1', 0, 'NL'),
('H03G5A', 'Advanced Methods in Cryptography', 4, 1, 'Mondeling, presentatie', 2, 'CRYPTO1', 0, 'EN'),
('H03G7A', 'Industriele stage: Wiskundige ingenieurstechnieken', 6, 0, 'Verslag, presentatie', 1, 'ANDERE', 0, 'NL'),
('H03H5A', 'Medical Imaging and Analysis ', 6, 0, 'Schriftelijk', 2, 'ANDERE', 0, 'EN'),
('H03H9A', 'Masterproef', 12, 1, 'Paper/Werkstuk, Presentatie, Medewerking tijdens contactmomenten', 0, 'KERN', 0, 'NL'),
('H03I2A', 'Biomedical Data Processing', 6, 1, 'Mondeling, project', 1, 'ANDERE', 0, 'EN'),
('H03V7B', 'Data Mining and Neural Networks', 4, 1, 'Mondeling, schriftelijk', 1, 'DATA1', 0, 'EN'),
('H04B3A', 'Engels in de bedrijfsomgeving ', 3, 1, 'Mondeling, taken, spreekoefeningen', 0, 'AVO', 0, 'EN'),
('H04B4A', 'Frans in de bedrijfsomgeving', 3, 1, 'Mondeling, verslagen, vaardigheidstoetsen', 0, 'AVO', 0, 'NL'),
('H04D0A', 'Industrial Automation and Control', 6, 0, 'Mondeling', 1, 'PROCES2', 0, 'EN'),
('H04D8A', 'Expressievaardigheid in de technische bedrijfsomgeving', 3, 1, 'Presentatie, take-home, mondeling', 2, 'AVO', 0, 'NL'),
('H04E0A', 'Plichtenleer van de ingenieur', 3, 0, 'Mondeling, kiezen paper of examen', 2, 'AVO', 0, 'NL'),
('H04M8A', 'Interdisciplinair college duurzame ontwikkeling', 3, 0, 'Schriftelijk', 2, 'AVO', 0, 'NL'),
('H04U8A', 'Numerical Techniques in Fluid Dynamics', 3, 1, 'Mondeling, report, presentatie', 1, 'COMP2', 0, 'EN'),
('H04X2A', 'Project Management', 3, 1, 'Presentatie, mondeling', 2, 'AVO', 0, 'EN'),
('H05D9A', 'Cryptografie en netwerkbeveiliging', 3, 1, 'Mondeling, presentatie', 2, 'CRYPTO1', 0, 'NL'),
('H05I5A', 'Programmatuur voor real-time controle', 3, 0, 'Mondeling, Schriftelijk', 2, 'PROCES1', 0, 'NL'),
('H05I9A', 'Stochastische signaal- en systeemanalyse', 3, 0, 'Mondeling', 2, 'ANDERE', 0, 'NL'),
('H05M9A', 'Bio-informatica', 4, 0, 'Mondeling', 1, 'DATA1', 0, 'NL'),
('H05U5A', 'Athens / Summer course', 3, 0, 'Medewerking', 0, 'ANDERE', 0, 'EN'),
('H06J1A', 'Geavanceerde procesregeling in de (bio)chemische industrie', 3, 0, '?', 2, 'PROCES2', 0, 'NL'),
('H07Z5A', 'Computergrafiek: project', 3, 1, 'Ontwerp, verslag, presentatie', 2, 'ANDERE', 0, 'NL'),
('H08K8A', 'Capita Selecta Mathematical Engineering', 3, 1, 'Medewerking, mogelijk project, discussie', 0, 'ANDERE', 0, 'EN'),
('H09J2A', 'Pattern Recognition and Image Interpretation', 6, 0, 'Mondeling', 2, 'ANDERE', 0, 'EN'),
('H09L2A', 'Privacy Technologies ', 3, 1, 'Mondeing, report, presentatie', 1, 'CRYPTO1', 0, 'EN'),
('H09L4A', 'e-Security', 3, 1, 'Mondeling, project', 1, 'CRYPTO2', 0, 'EN'),
('H09P4A', 'Engineering & Entrepreneurship', 6, 1, 'Mondeling, presentatie, project, medewerking', 2, 'AVO', 0, 'EN'),
('H09W6B', 'Complexe functieleer en toepassingen ', 4, 0, 'Mondeling', 1, 'KERN', 0, 'NL'),
('H0E76A', 'Model Predictive Control', 4, 1, 'Schriftelijk', 1, 'PROCES1', 0, 'EN'),
('H0E78A', 'Computeralgebra voor cryptografie', 3, 1, 'Mondeling, Paper/Werkstuk', 2, 'KERN', 0, 'NL'),
('H0S11A', 'Niet-lineaire systemen', 6, 0, 'Mondeling, Schriftelijk', 2, 'KERN', 0, 'NL'),
('H0S14A', 'Systeemidentificatie en modellering', 4, 1, 'Mondeling', 1, 'KERN', 0, 'NL'),
('H0S15A', 'Optimalisatie', 6, 0, 'Schriftelijk', 1, 'KERN', 0, 'NL'),
('H0T39A', 'Entrepreneurship in de praktijk', 3, 1, 'Verslag, presentatie', 2, 'AVO', 0, 'NL'),
('H0T44A', 'Project Wiskundige Ingenieurstechnieken', 3, 1, 'Ontwerp/Product, Presentatie, Procesevaluatie', 2, 'KERN', 0, 'NL'),
('H0T91A', 'Entrepreneurship in practice', 6, 1, 'Ontwerp, verslag, presentatie', 2, 'AVO', 0, 'NL'),
('H9X21A', 'Finite Elements, Part 2', 3, 1, 'Mondeling', 1, 'COMP2', 0, 'EN'),
('I0W36A', 'Transport Phenomena in Bioscience Engineering', 5, 0, 'Schriftelijk', 2, 'COMP2', 0, 'EN'),
('P00H0A', 'Psychologie m.i.v. psychologie van de waarneming', 3, 0, '?', 2, 'AVO', 0, 'NL'),
('S0B88A', 'Genderstudies', 4, 0, 'Schriftelijk', 0, 'AVO', 0, 'NL'),
('S0E06A', 'Interdisciplinary Perspectives on Development and Cultures', 4, 1, 'Schriftelijk, mondeling, paper', 1, 'AVO', 0, 'EN'),
('W0AE0A', 'Lessen voor de 21ste eeuw', 4, 0, 'Schriftelijk', 0, 'AVO', 0, 'NL'),
('W0AH4A', 'Studium generale: mens- en wereldbeelden ', 4, 1, 'Paper, medewerking', 2, 'AVO', 0, 'NL');

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `vakken`
--
ALTER TABLE `vakken`
  ADD PRIMARY KEY (`Code`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
