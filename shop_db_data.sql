--
-- PostgreSQL database dump
--

\restrict XVUS3eR1mvXklHvUNh4ctStFS2kbEcU8svAfzvSF7YSKYNRJamyatbFbZhQgO6O

-- Dumped from database version 18.1
-- Dumped by pg_dump version 18.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customers (id, name, surname, mail, created_at) FROM stdin;
1	Charlie	\N	narod@mail.ru	2026-02-09 18:03:01+02
2	Konstantin	Mighty	lazyguy@mail.ru	2026-02-09 18:06:54+02
3	Bobby	Duhless	lasagnaIsCool@gmail.com	2026-02-09 18:06:54+02
4	Samantha	Black	samantha@gmail.com	2026-02-09 18:06:54+02
5	Nigel	Carpenter	misterx@gmail.com	2026-02-09 18:06:54+02
6	Walter	White	blackorwhite@gmail.com	2026-02-09 18:06:54+02
7	Volodimir	Grey	usausausa@gmail.com	2026-02-09 18:06:54+02
8	Stephen	Brown	makarena@gmail.com	2026-02-09 18:06:54+02
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (id, customer_id, created_at, address, is_paid) FROM stdin;
2	3	2026-02-09 18:43:39+02	St. Mortimer street 199	f
3	8	2026-02-09 18:44:10+02	Intercection of 1st and 8, 999	t
4	1	2026-02-09 21:20:19+02	Main street, 2	f
5	5	2026-02-09 21:20:19+02	Second main street, 44	f
6	1	2026-02-10 10:55:00+02	Times square	t
7	1	2026-02-10 10:55:00+02	Isaakievskaya ploschad'	f
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (id, name, price, amount) FROM stdin;
1	Banana kg	1.79	100
2	Coca-cola bottle	0.89	1000
3	Chicken thighs kg	3.59	127
4	Wardrobe	359.99	55
5	Chair	89.99	33
6	Table	143.99	18
7	Bread	0.89	188
8	Red dress	22.95	44
9	newest mePhone	2001.59	0
10	Milk l	1.80	145
11	Cocoa milk	2.69	45
12	Chips	3.60	445
13	Watermelon	4.94	115
\.


--
-- Data for Name: order_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.order_items (id, order_id, product_id, product_amount, product_price) FROM stdin;
1	3	1	23	2.00
2	3	5	1	100.00
3	3	12	2	4.00
4	3	7	1	1.00
10	5	2	2	1.00
11	5	6	1	160.00
12	5	13	1	5.00
13	5	11	2	3.00
14	5	9	1	2224.00
15	2	4	1	399.99
16	2	8	2	25.50
17	2	2	6	0.99
18	2	5	3	99.99
19	2	10	2	2.00
\.


--
-- Name: customers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customers_id_seq', 8, true);


--
-- Name: order_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_items_id_seq', 21, true);


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_seq', 8, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 13, true);


--
-- PostgreSQL database dump complete
--

\unrestrict XVUS3eR1mvXklHvUNh4ctStFS2kbEcU8svAfzvSF7YSKYNRJamyatbFbZhQgO6O

