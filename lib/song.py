class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment song count and add to tracking
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count"""
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        """Update the genres list with unique genres"""
        # This method will be called from __init__, but we'll handle duplicates in the property
        pass

    @classmethod
    def add_to_artists(cls):
        """Update the artists list with unique artists"""
        # This method will be called from __init__, but we'll handle duplicates in the property
        pass

    @classmethod
    def add_to_genre_count(cls, genre=None):
        """Update the genre count histogram"""
        # This will be handled by the property, but we need to initialize it
        pass

    @classmethod
    def add_to_artist_count(cls, artist=None):
        """Update the artist count histogram"""
        # This will be handled by the property, but we need to initialize it
        pass

    # Using properties to handle the derived attributes
    @property
    def genres(self):
        """Return unique genres from all songs"""
        return list(set(self.__class__.genres))
    
    @property
    def artists(self):
        """Return unique artists from all songs"""
        return list(set(self.__class__.artists))
    
    @property
    def genre_count(self):
        """Return count of songs by genre"""
        count_dict = {}
        for genre in self.__class__.genres:
            count_dict[genre] = count_dict.get(genre, 0) + 1
        return count_dict
    
    @property
    def artist_count(self):
        """Return count of songs by artist"""
        count_dict = {}
        for artist in self.__class__.artists:
            count_dict[artist] = count_dict.get(artist, 0) + 1
        return count_dict