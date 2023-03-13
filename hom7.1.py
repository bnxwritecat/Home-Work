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
b.execute("INSERT INTO stud  VALUES('Adilet', 'Tyraatov', 'pubg', 18, 2005)")
b.execute("INSERT INTO stud  VALUES('Android', 'Shishkib', 'Auto', 24, 1999)")
b.execute("INSERT INTO stud  VALUES('Maratik', 'Sortimovich', 'dym', 18, 2005)")
b.execute("INSERT INTO stud  VALUES('Adil', 'Suliilmanov', 'Sell cars', 24, 2001)")
b.execute("INSERT INTO stud  VALUES('Dior', 'Satinbekov', 'Football', 17, 2006)")
b.execute("INSERT INTO stud  VALUES('Alina', 'Salieva', 'Free Fire', 17, 2006)")
b.execute("INSERT INTO stud  VALUES('Asyl', 'Turdaliev', 'No hobby', 17, 2006)")
b.execute("INSERT INTO stud  VALUES('Marksat', 'Bytyrov', 'Cats', 18, 2005)")
b.execute("INSERT INTO stud  VALUES('Muhammedali', 'Askarov', 'Ponty', 17, 2006)")
b.execute("INSERT INTO stud  VALUES('Ayarabus', 'Palanchaev', 'headache', 623, 200)")
b.execute("SELECT rowid, surname FROM stud WHERE LENGTH(surname) >= 10 ")
print(b.fetchall())
b.execute("UPDATE stud SET name = 'genius' WHERE mark >= 10")
b.execute("SELECT rowid, *   FROM stud WHERE name = 'genius'")
print(b.fetchall())
b.execute("DELETE FROM stud WHERE rowid % 2 == 0")
db.commit()
db.close()