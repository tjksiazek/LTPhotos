import json
import urllib.request

##Loading json response of photos
def get_photos(url):
    response = urllib.request.urlopen(url)
    photo_albums = json.loads(response.read())
    return photo_albums

##Grabbing all albums based off albumID and finding max album number
def get_albums(photo_albums):
    total_albums = 0

    for album in photo_albums:
        album_id = album.get('albumId')
        if album_id > total_albums:
            total_albums = album_id

    return str(total_albums)

##Returns albumID followed by title for each photo
def get_photo_content(photos):
    for photo in photos:
        id = photo.get('id')
        title = photo.get('title')
        print(str(id) + "--" + title)

albums_url = "https://jsonplaceholder.typicode.com/photos"    ##URL for all albums
all_photos = get_photos(albums_url)   ##Gets photos from URL in get photos
albums = get_albums(all_photos) ##sets number of total albums in collections
url_album_list = 'https://jsonplaceholder.typicode.com/photos?albumId='  ##direct url to albums by ID

print("LT Photo Albums")
print("Which album do you want to view?")
print("There is " + albums + "albums")

work = True     ##Setting var for while loop for exiting app

while work:

    try:
        selection = input("Enter album choice or enter 2020 to exit: ")  ##Receives user input for album selection
        user_photos = get_photos((url_album_list) + str(selection))

        if 0 < int(selection) <= int(albums):       ##makes sure album is within possible selection range
            print("Album " + (selection))
            get_photo_content(user_photos)      ##pulls ID and title for all photos in user selection album list

        elif int(selection) == 2020:        ##gives a way to quit and set var to exit while
            print("Thanks for using LT Photos")
            work = False

        else:       ##error handling for not number in range
            print(str(selection) + " is not a valid album number")
            print("Select an album number between 1 and " + albums)

    except (SyntaxError, ValueError):
        print("You have not entered a valid album or quit")
