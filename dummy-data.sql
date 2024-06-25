--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-06-25 08:51:28

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 4856 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16399)
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    "EmployeeID" integer NOT NULL,
    "EmployeeLastName" character varying(50) NOT NULL,
    "EmployeeFirstName" character varying(50) NOT NULL,
    "EmployeeMiddleName" character varying(50) NOT NULL,
    "StartedRoleOn" timestamp with time zone NOT NULL,
    "EndedRoleOn" timestamp with time zone,
    "EmployeeStatus" character varying(50)
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16416)
-- Name: skill; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.skill (
    "SkillID" integer NOT NULL,
    "AddedBy" integer NOT NULL,
    "SkillName" character varying(100) NOT NULL,
    "SkillType" character varying(50) NOT NULL,
    "CreatedOn" timestamp with time zone NOT NULL,
    "DeletedOn" timestamp with time zone,
    "SkillStatus" character varying(50) NOT NULL,
    CONSTRAINT skill_type_choices CHECK ((("SkillType")::text = ANY ((ARRAY['Functional'::character varying, 'Enabling'::character varying])::text[])))
);


ALTER TABLE public.skill OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16427)
-- Name: skill_level; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.skill_level (
    "SkillLevelID" integer NOT NULL,
    "SkillID" integer NOT NULL,
    "AddedBy" integer NOT NULL,
    "SkillLevelValue" integer NOT NULL,
    "SkillLevelDescription" character varying(500) NOT NULL,
    "CreatedOn" timestamp with time zone NOT NULL,
    "EditedOn" timestamp with time zone NOT NULL,
    "DeletedOn" timestamp with time zone,
    "SkillLevelStatus" character varying NOT NULL
);


ALTER TABLE public.skill_level OWNER TO postgres;

--
-- TOC entry 4848 (class 0 OID 16399)
-- Dependencies: 215
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (1, 'Smith', 'John', 'Michael', '2021-01-10 16:00:00+08', '2023-05-21 01:00:00+08', 'Inactive');
INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (2, 'Johnson', 'Emily', 'Sarah', '2019-03-15 17:00:00+08', NULL, 'Active');
INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (3, 'Williams', 'David', 'Robert', '2020-07-22 18:00:00+08', NULL, 'Active');
INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (4, 'Jones', 'Jessica', 'Anne', '2018-11-30 16:30:00+08', '2022-03-01 00:30:00+08', 'Inactive');
INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (5, 'Brown', 'Michael', 'James', '2017-04-25 17:00:00+08', NULL, 'Active');
INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (6, 'Davis', 'Jennifer', 'Marie', '2022-06-10 18:00:00+08', NULL, 'Active');
INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (7, 'Miller', 'William', 'Joseph', '2015-12-01 16:00:00+08', '2022-01-01 01:00:00+08', 'Inactive');
INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (8, 'Wilson', 'Amanda', 'Lee', '2019-08-12 17:00:00+08', NULL, 'Active');
INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (9, 'Moore', 'Christopher', 'John', '2023-01-05 16:30:00+08', NULL, 'Active');
INSERT INTO public.employee ("EmployeeID", "EmployeeLastName", "EmployeeFirstName", "EmployeeMiddleName", "StartedRoleOn", "EndedRoleOn", "EmployeeStatus") VALUES (10, 'Taylor', 'Elizabeth', 'Grace', '2021-10-20 17:30:00+08', NULL, 'Active');


--
-- TOC entry 4849 (class 0 OID 16416)
-- Dependencies: 216
-- Data for Name: skill; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (1, 1, 'Project Management', 'Functional', '2021-05-15 18:00:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (2, 2, 'Python Programming', 'Functional', '2020-06-20 17:30:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (3, 3, 'Data Analysis', 'Functional', '2019-07-25 19:00:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (4, 4, 'Public Speaking', 'Enabling', '2018-08-10 16:45:00+08', NULL, 'Inactive');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (5, 5, 'Team Leadership', 'Enabling', '2017-09-15 20:30:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (6, 6, 'Software Development', 'Functional', '2022-01-05 22:00:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (7, 7, 'Conflict Resolution', 'Enabling', '2023-02-10 23:15:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (8, 8, 'Agile Methodologies', 'Functional', '2021-03-20 21:45:00+08', NULL, 'Inactive');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (9, 9, 'Creative Thinking', 'Enabling', '2020-04-26 00:30:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (10, 10, 'Customer Service', 'Functional', '2019-05-31 01:00:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (11, 1, 'Data Visualization', 'Functional', '2022-03-15 17:00:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (12, 3, 'Communication', 'Enabling', '2021-03-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (14, 3, 'Problem Solving', 'Enabling', '2022-02-20 17:30:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (15, 7, 'Business Needs Analysis', 'Functional', '2022-03-25 19:00:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (16, 1, 'Data Analytics', 'Functional', '2022-04-10 16:45:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (17, 6, 'Data Engineering', 'Functional', '2022-05-15 20:30:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (18, 4, 'Data Ethics', 'Functional', '2022-06-05 22:00:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (19, 9, 'Data Strategy', 'Functional', '2022-07-10 23:15:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (20, 2, 'Data Visualisation', 'Functional', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (21, 5, 'Design Thinking Practice', 'Functional', '2022-09-26 00:30:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (22, 8, 'Intelligent Reasoning', 'Functional', '2022-10-31 01:00:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (23, 10, 'Problem Management', 'Functional', '2022-11-15 17:00:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (24, 1, 'Stakeholder Management', 'Functional', '2023-01-25 19:45:00+08', NULL, 'Active');
INSERT INTO public.skill ("SkillID", "AddedBy", "SkillName", "SkillType", "CreatedOn", "DeletedOn", "SkillStatus") VALUES (25, 6, 'Strategy Planning', 'Functional', '2023-02-20 20:15:00+08', NULL, 'Active');


--
-- TOC entry 4850 (class 0 OID 16427)
-- Dependencies: 217
-- Data for Name: skill_level; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (0, 11, 4, 3, 'Select appropriate visualisation techniques and develop dashboards to reflect data trends and findings', '2023-02-10 23:15:00+08', '2023-02-10 23:15:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (1, 11, 4, 4, 'Design data displays to present trends and finding, incorporating new and advanced visualisation techniques and analytics capabilities', '2023-02-10 23:15:00+08', '2023-02-10 23:15:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (2, 11, 4, 5, 'Establish an effective data visualisation architecture and design intelligent and adaptable displays employing optimal delivery modes, mechanisms and timings', '2023-02-10 23:15:00+08', '2023-02-10 23:15:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (3, 12, 6, 1, 'Communicate with others to share information, respond to general inquiries and obtain specific information', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (4, 12, 6, 2, 'Tailor communication approaches to audience needs and determine suitable methods to convey and exchange information', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (5, 12, 6, 3, 'Synthesise information and inputs to communicate an overarching storyline to multiple stakeholders', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (6, 14, 8, 1, 'Identify problems and implement guidelines and procedures to solve problems and test solutions', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (7, 14, 8, 2, 'Determine underlying causes of problems and collaborate with other stakeholders to implement and evaluate solutions', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (8, 14, 8, 3, 'Anticipate potential problems to drive a culture of continuous improvement which seeks to turn problems into opportunities across the organisation', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (9, 1, 9, 3, 'Oversee small projects or programmes, managing timelines, resources, risks and stakeholders', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (10, 1, 9, 4, 'Plan and drive medium scale projects or programmes, including allocating resources to different parts, and engaging stakeholders on the project''s progress and outcomes', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (11, 1, 9, 5, 'Lead end-to-end management of large programmes or multiple projects concurrently, coordinating project interdependencies', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');
INSERT INTO public.skill_level ("SkillLevelID", "SkillID", "AddedBy", "SkillLevelValue", "SkillLevelDescription", "CreatedOn", "EditedOn", "DeletedOn", "SkillLevelStatus") VALUES (12, 1, 9, 6, 'Direct the management and authorise ownership of multiple large, complex programmes and projects, ensuring alignment with strategic business priorities', '2022-08-20 21:45:00+08', '2022-08-20 21:45:00+08', NULL, 'Active');


--
-- TOC entry 4699 (class 2606 OID 16421)
-- Name: skill SkillID; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skill
    ADD CONSTRAINT "SkillID" PRIMARY KEY ("SkillID");


--
-- TOC entry 4697 (class 2606 OID 16403)
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY ("EmployeeID");


--
-- TOC entry 4701 (class 2606 OID 16433)
-- Name: skill_level skill_level_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skill_level
    ADD CONSTRAINT skill_level_pkey PRIMARY KEY ("SkillLevelID");


--
-- TOC entry 4702 (class 2606 OID 16422)
-- Name: skill AddedBy; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skill
    ADD CONSTRAINT "AddedBy" FOREIGN KEY ("AddedBy") REFERENCES public.employee("EmployeeID");


--
-- TOC entry 4703 (class 2606 OID 16439)
-- Name: skill_level employee_reference; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skill_level
    ADD CONSTRAINT employee_reference FOREIGN KEY ("AddedBy") REFERENCES public.employee("EmployeeID");


--
-- TOC entry 4704 (class 2606 OID 16434)
-- Name: skill_level skill_reference; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skill_level
    ADD CONSTRAINT skill_reference FOREIGN KEY ("SkillID") REFERENCES public.skill("SkillID");


-- Completed on 2024-06-25 08:51:28

--
-- PostgreSQL database dump complete
--

