def make_album(artist, album):
    full_album = f"Artist {artist.title()} dropped the album {album.title()} for your listening pleasure."
    return full_album

while True:
    artist_name = input("\nEnter the artist's name: ")
    print("\n(Enter 'q' to quit at any time)")

    album_title = input("\nEnter an album title: ")

    if artist_name or album_title == 'q':
        break

    final = make_album(artist_name, album_title)
    print(final)
        