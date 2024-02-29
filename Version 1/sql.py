import sqlite3

# Connect to sqlite
connection = sqlite3.connect("anime.db")

# create a cursor object to insert record create table, retrieve result
cursor = connection.cursor()

# Create a table
table_info = """
CREATE TABLE ANIME (
    ID INT,
    NAME VARCHAR(250),
    GENRE VARCHAR(250),
    TYPE VARCHAR(25),
    EPISODES VARCHAR(20),
    RATING FLOAT,
    MEMBERS INT
)
"""

cursor.execute(table_info)
# Dummy data for database.
anime_data = [
    (32281, 'Kimi no Na wa.', 'Drama, Romance, School, Supernatural', 'Movie', '1', 9.37, 200630),
    (5114, 'Fullmetal Alchemist: Brotherhood', 'Action, Adventure, Drama, Fantasy, Magic, Military, Shounen', 'TV', '64', 9.26, 793665),
    (9253, 'Steins;Gate', 'Sci-Fi, Thriller', 'TV', '24', 9.17, 673572),
    (32935, 'Haikyuu!!: Karasuno Koukou VS Shiratorizawa Gakuen Koukou', 'Comedy, Drama, School, Shounen, Sports', 'TV', '10', 9.15, 93351),
    (11061, 'Hunter x Hunter (2011)', 'Action, Adventure, Shounen, Super Power', 'TV', '148', 9.13, 425855),
    (30276, 'One Punch Man', 'Action, Comedy, Parody, Sci-Fi, Seinen, Super Power, Supernatural', 'TV', '12', 8.82, 552458),
    (19, 'Monster', 'Drama, Horror, Mystery, Police, Psychological, Seinen, Thriller', 'TV', '74', 8.72, 247562),
    (1535, 'Death Note', 'Mystery, Police, Psychological, Supernatural, Thriller', 'TV', '37', 8.71, 1013917),
    (22319, 'Tokyo Ghoul', 'Action, Drama, Horror, Mystery, Psychological, Seinen, Supernatural', 'TV', '12', 8.07, 618056),
    (21, 'One Piece', 'Action, Adventure, Comedy, Drama, Fantasy, Shounen, Super Power', 'TV', 'Running', 8.58, 504862),
    (31964, 'Boku no Hero Academia', 'Action, Comedy, School, Shounen, Super Power', 'TV', '13', 8.36, 282002),
    (43, 'Ghost in the Shell', 'Action, Mecha, Police, Psychological, Sci-Fi, Seinen', 'Movie', '1', 8.34, 223036),
    (33950, 'Black Clover', 'Action, Comedy, Fantasy, Magic, Shounen', 'TV', '175', 8.6, 2247),
    (32182, 'Mob Psycho 100', 'Action, Comedy, Slice of Life, Supernatural', 'TV', '12', 8.55, 193716),
    (13601, 'Psycho-Pass', 'Action, Police, Psychological, Sci-Fi', 'TV', '22', 8.5, 509109)
]

# Iterate through the list and execute INSERT statements
for data in anime_data:
    cursor.execute("INSERT INTO ANIME VALUES (?, ?, ?, ?, ?, ?, ?)", data)

# Display all the records
print("Records inserted")

# Commit the changes and close the connection
connection.commit()
connection.close()
