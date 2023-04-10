DDL_QUERY =  '''
CREATE TABLE dim_product
(
    id_product INT NOT NULL,
    name VARCHAR(200) NOT NULL,
    CONSTRAINT PK_PRODUCT PRIMARY KEY (id_product),
    CONSTRAINT UNICO_PRODUCT UNIQUE (name)
);

CREATE TABLE dim_genero
(
    id_genero INT NOT NULL,
    genre VARCHAR(15) NOT NULL,
    CONSTRAINT PK_GENERO PRIMARY KEY (id_genero),
    CONSTRAINT UNICO_GENERO UNIQUE (genre)
);

CREATE TABLE dim_plataforma
(
    id_plataforma INT NOT NULL,
    platform VARCHAR(10) NOT NULL,
    CONSTRAINT PK_PLATFORM PRIMARY KEY (id_plataforma),
    CONSTRAINT UNICO_PLATFORM UNIQUE (platform)
);

CREATE TABLE dim_publisher
(
    id_publisher INT NOT NULL,
    publisher VARCHAR(50) NOT NULL,
    CONSTRAINT PK_PUBLISHER PRIMARY KEY (id_publisher),
    CONSTRAINT UNICO_PUBLISHER UNIQUE (publisher)
);

CREATE TABLE dim_year
(
    year FLOAT NOT NULL,
    id_category INT NOT NULL,
    category_year VARCHAR(10) NOT NULL,
    CONSTRAINT PK_YEAR PRIMARY KEY (year)    
);

CREATE TABLE fact_sales
(
    id_sales INT NOT NULL,
    id_product INT NOT NULL,
    id_plataforma INT NOT NULL,
    year FLOAT NOT NULL,
    id_genero INT NOT NULL,
    id_publisher INT NOT NULL,
    na_sales FLOAT,
    eu_sales FLOAT,
    jp_sales FLOAT,
    other_sales FLOAT,
    global_sales FLOAT,
    rank INT NOT NULL,
    CONSTRAINT PK_SALES PRIMARY KEY (id_sales),
    CONSTRAINT FK_PRODUCT FOREIGN KEY (id_product) REFERENCES dim_product (id_product),
    CONSTRAINT FK_PLATAFORMA FOREIGN KEY (id_plataforma) REFERENCES dim_plataforma (id_plataforma),
    CONSTRAINT FK_YEAR FOREIGN KEY (year) REFERENCES dim_year (year),
    CONSTRAINT FK_GENERO FOREIGN KEY (id_genero) REFERENCES dim_genero (id_genero),
    CONSTRAINT FK_PUBLISHER FOREIGN KEY (id_publisher) REFERENCES dim_publisher (id_publisher)
)

'''