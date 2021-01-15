from app import app, db

#the User model: each user has a username, and a playlist_id foreign key referring
#to the user's Playlist
class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), index = True, unique = True) 
  playlist_id = db.Column(db.Integer,  db.ForeignKey('playlist.id'))
  
  #representation method
  def __repr__(self):
        return "{}".format(self.username)


class Song(db.Model):
  # primary key id
  id = db.Column(db.Integer, primary_key=True)
  # Task 5: add artist and title fields
  artist = db.Column(db.String(50), index=True)
  # title column
  title = db.Column(db.String(50), index=True)
  # Task 6: add column n
  n = db.Column(db.Integer)

  # Task 7: add __repr__ method
  def __repr__(self):
    # Return message
    return "{title} by {artist}".format(title=self.title, artist=self.artist)
    
# Task 8: create the Item model here + add a nice representation method
class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  # Task 9: add foreign key song_id that references Song model primary key id
  song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
  # Task 11: add foreign key playlist_id that references Playlist model primary key id
  playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))

  # add __repr__ method
  def __repr__(self):
    # Return message
    return "Item ID: {id} with Song ID: {song_id}".format(id=self.id, song_id=self.song_id)
    
# Task 10: create the Playlist model here + add a nice representation method
class Playlist(db.Model):
  # primary key id
  id = db.Column(db.Integer, primary_key=True)
  # Task 12: add items using relationship that references Item table
  items = db.relationship('Item', backref='playlist', lazy='dynamic')
