def make_album(artist : str , title : str) -> str:
    album : dict = {"Title:" : title, "Artist" : artist}
    print(album)
    return make_album

def make_album2(artist : str , title : str, nsong : int = None) -> str:
    album : dict = {"Title:" : title, "Artist" : artist, "Track number: " : nsong}
    print(album)
    return make_album2