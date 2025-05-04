--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: families; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.families (
    f_id integer NOT NULL,
    f_value character varying(30)
);


ALTER TABLE public.families OWNER TO postgres;

--
-- Name: family_f_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.family_f_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.family_f_id_seq OWNER TO postgres;

--
-- Name: family_f_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.family_f_id_seq OWNED BY public.families.f_id;


--
-- Name: main; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.main (
    uniq_id integer NOT NULL,
    fam integer,
    name_ integer,
    otc integer,
    street integer,
    bldn character varying(10),
    bldn_h character varying(10),
    appr integer,
    tel character varying(20)
);


ALTER TABLE public.main OWNER TO postgres;

--
-- Name: main_uniq_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.main_uniq_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.main_uniq_id_seq OWNER TO postgres;

--
-- Name: main_uniq_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.main_uniq_id_seq OWNED BY public.main.uniq_id;


--
-- Name: names_; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.names_ (
    name_id integer NOT NULL,
    name_val character varying(20)
);


ALTER TABLE public.names_ OWNER TO postgres;

--
-- Name: names_name_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.names_name_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.names_name_id_seq OWNER TO postgres;

--
-- Name: names_name_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.names_name_id_seq OWNED BY public.names_.name_id;


--
-- Name: otchestvo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.otchestvo (
    otc_id integer NOT NULL,
    otc_val character varying(30)
);


ALTER TABLE public.otchestvo OWNER TO postgres;

--
-- Name: otchestvo_otc_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.otchestvo_otc_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.otchestvo_otc_id_seq OWNER TO postgres;

--
-- Name: otchestvo_otc_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.otchestvo_otc_id_seq OWNED BY public.otchestvo.otc_id;


--
-- Name: streets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.streets (
    id_street integer NOT NULL,
    street_val character varying(30)
);


ALTER TABLE public.streets OWNER TO postgres;

--
-- Name: streets_id_street_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.streets_id_street_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.streets_id_street_seq OWNER TO postgres;

--
-- Name: streets_id_street_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.streets_id_street_seq OWNED BY public.streets.id_street;


--
-- Name: families f_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.families ALTER COLUMN f_id SET DEFAULT nextval('public.family_f_id_seq'::regclass);


--
-- Name: main uniq_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main ALTER COLUMN uniq_id SET DEFAULT nextval('public.main_uniq_id_seq'::regclass);


--
-- Name: names_ name_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.names_ ALTER COLUMN name_id SET DEFAULT nextval('public.names_name_id_seq'::regclass);


--
-- Name: otchestvo otc_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.otchestvo ALTER COLUMN otc_id SET DEFAULT nextval('public.otchestvo_otc_id_seq'::regclass);


--
-- Name: streets id_street; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.streets ALTER COLUMN id_street SET DEFAULT nextval('public.streets_id_street_seq'::regclass);


--
-- Name: families family_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.families
    ADD CONSTRAINT family_pkey PRIMARY KEY (f_id);


--
-- Name: main main_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main
    ADD CONSTRAINT main_pkey PRIMARY KEY (uniq_id);


--
-- Name: names_ names_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.names_
    ADD CONSTRAINT names_pkey PRIMARY KEY (name_id);


--
-- Name: otchestvo otchestvo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.otchestvo
    ADD CONSTRAINT otchestvo_pkey PRIMARY KEY (otc_id);


--
-- Name: streets streets_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.streets
    ADD CONSTRAINT streets_pkey PRIMARY KEY (id_street);


--
-- Name: main fk_fam; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main
    ADD CONSTRAINT fk_fam FOREIGN KEY (fam) REFERENCES public.families(f_id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: main fk_names_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main
    ADD CONSTRAINT fk_names_ FOREIGN KEY (name_) REFERENCES public.names_(name_id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;


--
-- Name: main fk_otchestvo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main
    ADD CONSTRAINT fk_otchestvo FOREIGN KEY (otc) REFERENCES public.otchestvo(otc_id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: main fk_streets; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main
    ADD CONSTRAINT fk_streets FOREIGN KEY (street) REFERENCES public.streets(id_street) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- PostgreSQL database dump complete
--

