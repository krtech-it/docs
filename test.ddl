CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work
(
    id uuid PRIMARY KEY,
    title text NOT NULL,
    description text,
    creation_date date,
    rating float,
    type text NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS person
(
    id uuid PRIMARY KEY,
    full_name text NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS person_film_work
(
    id uuid PRIMARY KEY,
    person_id uuid NOT NULL,
    film_work_id uuid NOT NULL,
    role text NOT NULL,
    created timestamp with time zone
);

CREATE TABLE IF NOT EXISTS genre
(
    id uuid PRIMARY KEY,
    name text UNIQUE NOT NULL,
    description text,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS genre_film_work
(
    id uuid PRIMARY KEY,
    genre_id uuid NOT NULL,
    film_work_id uuid NOT NULL,
    created timestamp with time zone
);

CREATE UNIQUE INDEX film_work_genre_idx ON genre_film_work(film_work_id, genre_id);

CREATE INDEX film_work_person_idx ON person_film_work(film_work_id, person_id);

CREATE INDEX film_work_creation_date_idx ON film_work(creation_date);



