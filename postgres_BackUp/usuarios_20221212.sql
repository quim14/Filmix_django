PGDMP                         z            filmix_django    15.0    15.0                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                        0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            !           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            "           1262    16438    filmix_django    DATABASE     ?   CREATE DATABASE filmix_django WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE filmix_django;
                postgres    false            ?            1259    16481 	   auth_user    TABLE     ?  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    postgres    false            ?            1259    16480    auth_user_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    225            #           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    224            ?           2604    16484    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    225    225                      0    16481 	   auth_user 
   TABLE DATA           ?   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    225   ?       $           0    0    auth_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_user_id_seq', 10, true);
          public          postgres    false    224            ?           2606    16486    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    225            ?           2606    16578     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    225            ?           1259    16579     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    225               ?  x?}?[o?L?k?)z?]S??@ҤX??????l???R9(??_??7??].`.??????}:[/@???F"???Ǧ?(?|ҋ?&?Q????,Ѥބ?Qj??z?P??a&?u?Uu$vI????!z?20Dd?`.?
?/~"nj?	g??????pgǉ঻?߷ ??D?`?Ãx??]???b?????roW?r??ygt?e?????Yۅ??-??v?s?q???N|?"?_?/܏Qs<7MC??ӫ0??b??RE?0/6v?fzd?[??He?93{?|?|????4????6??R??č?Rx"OsUʕ???5?e??B???>?&??)xy???RRU?(PIƐ\??}f???T??	???`?62??yX??AaZ'???~?gc2?c??A?weL????ί???s????5??oHY? ?D??)?G};???????)?G?????%k??ms??&???:-???P+?{k??'??^???參E?@,Ș*?T???8K?io???CƸi? (?!???}?_??G?T???͠???t???ܰ?>k??ۮ??*?d???2ڟ?V??8k?؍>B? М- 	???????kB
hJ?$I???󮳊LV?Qқ??ЕX贏?'??j????-???k?w?+?nz????tW??]?Ɖ???@H%|?+@???}?_?????u+?L-?T??????[?`???jt?'+y???Z???=??ç?;???{?V?yс??`???ԷxF?6?6?? Y ?)?????v??^?D?b?W??????nz?h?.???tfUt?1?g?j???>???Nxt???0?<5??????&0?p??(+?
P?_?iD?'?????F??????[7}l*??K??_??????=-??     