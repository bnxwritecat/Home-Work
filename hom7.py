import "sqlite3sqlite3"

db = sqlite3lite3.connectconnect("students.db")

b = db.cursor()

b.execute(""" CREATE TABLE IF NOT EXISTS stud(
Name text,
Surname text,
Hobby text,
Mark integer,
Date_of_Birth integer
)
""");
b.execute("INSERT INTO stud  VALUES('Islam', 'Toksonbaev', 'CS:GO', 10, 2004)")
b.execute("INSERT INTO stud  VALUES('Alexander', 'Stasuyk', 'Auto', 8, 1985)")
b.execute("INSERT INTO stud  VALUES('Marat', 'Saparbaev', 'GYM', 6, 2005)")
b.execute("INSERT INTO stud  VALUES('Adilet', 'Zhanibekov', 'Sell cars', 11, 2001)")
b.execute("INSERT INTO stud  VALUES('Dior', 'Ergashev', 'Football', 8, 2006)")
b.execute("INSERT INTO stud  VALUES('Alina', 'Salieva', 'Free Fire', 127, 2006)")
b.execute("INSERT INTO stud  VALUES('Asyl', 'Turdaliev', 'No hobby', 10, 2006)")
b.execute("INSERT INTO stud  VALUES('Maiza', 'Bataeva', 'Cats', 10, 2005)")
b.execute("INSERT INTO stud  VALUES('Muhammed', 'Avazbekov', 'Ponty', 1, 2006)")
b.execute("INSERT INTO stud  VALUES('Ayar', 'Palanchaev', 'headache', 6, 200)")
b.execute("SELECT rowid, surname FROM stud WHERE LENGTH(surname) >= 10 ")
print(b.fetchall())
b.execute("UPDATE stud SET name = 'genius' WHERE mark >= 10")
b.execute("SELECT rowid, *   FROM stud WHERE name = 'genius'")
print(b.fetchall())
b.execute("DELETE FROM stud WHERE rowid % 2 == 0")
db.commit()
db.close()