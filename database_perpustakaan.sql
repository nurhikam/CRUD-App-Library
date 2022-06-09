CREATE DATABASE perpustakaan;

USE perpustakaan;

CREATE TABLE daftar_buku(
	isbn VARCHAR(13),
    judul VARCHAR(200),
    penulis VARCHAR(200),
    tahun_terbit VARCHAR(4),
    rating_average FLOAT,
    rating_count INTEGER,
    PRIMARY KEY (isbn)
);

