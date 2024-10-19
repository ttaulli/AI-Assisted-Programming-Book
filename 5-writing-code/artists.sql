-- SQL file: music_inventory.sql

-- Create the 'artists' table
CREATE TABLE artists (
    artist_id INT PRIMARY KEY AUTO_INCREMENT,
    artist_name VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    country VARCHAR(100)
);

-- Create the 'albums' table
CREATE TABLE albums (
    album_id INT PRIMARY KEY AUTO_INCREMENT,
    album_title VARCHAR(255) NOT NULL,
    release_date DATE,
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE
);

-- Insert sample data into 'artists'
INSERT INTO artists (artist_name, genre, country)
VALUES
('The Beatles', 'Rock', 'UK'),
('Miles Davis', 'Jazz', 'USA'),
('Adele', 'Pop', 'UK');

-- Insert sample data into 'albums'
INSERT INTO albums (album_title, release_date, artist_id)
VALUES
('Abbey Road', '1969-09-26', 1),
('Kind of Blue', '1959-08-17', 2),
('21', '2011-01-24', 3);
