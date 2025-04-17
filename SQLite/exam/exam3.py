import sqlite3

conn=sqlite3.connect('exam3.db')
cursor=conn.cursor()

# make table 
cursor.execute('CREATE TABLE IF NOT EXISTS Cats(Id int, Name text, Age int, Breed text, Favoritefoods text,UniqueHabits text);')
cursor.execute('CREATE TABLE IF NOT EXISTS Dogs(Id int, Name text, Age int, Breed text, Favoritefoods text,UniqueHabits text);')
cursor.execute('CREATE TABLE IF NOT EXISTS Rabits(Id int, Name text, Age int, Breed text, Favoritefoods text,UniqueHabits text);')
cursor.execute('CREATE TABLE IF NOT EXISTS Fish(Id int, Name text, Age int, Breed text, Favoritefoods text,UniqueHabits text);')
cursor.execute('CREATE TABLE IF NOT EXISTS Birds(Id int, Name text, Age int, Breed text, Favoritefoods text,UniqueHabits text);')

# make Function for Insert and Values
def Insert(table, id, Name, Age, Breed, Favoritefoods, UniqueHabits):
    cursor.execute(f'INSERT INTO {table} VALUES(?,?,?,?,?,?)', (id, Name, Age, Breed, Favoritefoods, UniqueHabits))
    conn.commit()

def Update(table, value, where, whereField, whereValue):
    cursor.execute(f'UPDATE {table} SET {where} = ? WHERE {whereField} = ?', (value, whereValue))
    conn.commit()

# start Cats section
# Insert and get values to table (Cats)
Insert('Cats', 1, 'Fluffy', 3, 'Persian','Tuna, chicken','Loves sleeping in the sunlight')
Insert('Cats', 2, 'Tiger', 4, 'Siamese','Lamb meat, fish-flavored Cats food','Enjoys playing with balls')
Insert('Cats', 3, 'Shadow', 5, 'Domestic Short Hair','Dry Cats food','Loves sitting by the window')
# Update
Update('Cats', 'Ali', 'Name', 'Id', '2')
# end Cats section

# start Dogs section
# Insert and get values to table (Dogs)
Insert('Dogs', 1, 'Buddy', 2, 'Golden Retriever', 'Chicken, peanut butter', 'Collects balls around the house, sleeps by the window on sunny days')
Insert('Dogs', 2, 'Max', 3, 'German Shepherd', 'Beef, dry kibble', 'Sleeps on soft pillows, nudges the TV remote with her nose')
Insert('Dogs', 3, 'Bella', 5, 'Shih Tzu', 'Boiled beef, carrots', 'Kisses his owner’s foot before bed, plays with the water hose')
# Update
Update('Cats', 'Ali', 'Name', 'Id', '2')
# end Dogs section

# start Rabits section
# Insert and get values to table (Rabits)
Insert('Rabits', 1, 'Snowy', 2, 'Dutch Lop', 'Carrots, lettuce', 'Loves hopping around the house and always sleeps next to soft toys')
Insert('Rabits', 2, 'Hazel', 3, 'Angora Rabbit', 'Apples, mint leaves', 'Enjoys digging in the dirt and gets very energetic when playing with boxes')
Insert('Rabits', 3, 'Coco', 1, 'Mini Rex', 'Bell peppers, fresh greens', 'Loves grooming herself and always taps her owner’s hand with her paw to seek attention')
# Update
Update('Cats', 'Ali', 'Name', 'Id', '2')
# end Rabits section

# start Fish section
# Insert and get values to table  (Fish)
Insert('Fish', 1, 'Goldie', 1, 'Goldfish', 'Fish flakes, boiled peas', 'Swims in circles whenever someone approaches the tank and likes to hide behind decorative plants')
Insert('Fish', 2, 'Bubbles', 2, 'Betta Fish', 'Bloodworms, daphnia', 'Builds bubble nests at the water’s surface and flares its fins when seeing its reflection')
Insert('Fish', 3, 'Shadow', 3, 'Angelfish', 'Brine shrimp, algae wafers', 'Slowly glides through the water near tank decorations and often "stares" at people through the glass')
# Update
Update('Cats', 'Ali', 'Name', 'Id', '2')
# end Fish section

# start Birds section
# Insert and get values to table  (Birds)
Insert('Birds', 1, 'Sunny', 2, 'Sun Conure', 'Sunflower seeds, tropical fruits, and nuts', 'Loves spinning on perches and mimicking mobile phone ringtones')
Insert('Birds', 2, 'Coco', 5, 'Budgerigar (Parakeet)', 'Lettuce, shredded carrots, and millet', 'Sings along with classical music and bobs its head when excited')
Insert('Birds', 3, 'Kiwi', 1, 'Gouldian Finch', 'Tiny seeds and fresh greens', 'Perches on the tallest branch to observe everything')
# Update
Update('Cats', 'Ali', 'Name', 'Id', '2')
# end Birds section