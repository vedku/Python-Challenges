#it don't work yet
import random

artist_list = ["deadmau5", "John Coltrane", "Tigran Hamasyan", "Nas", "Johnny Cash"]


s_deadmau5 = ["Sofi Needs A Ladder", "A City in Florida", "Animals Rights", "Cthulhu Sleeps", "Some Chords", "I Said(Michael Woods Remix)", "Bad Selection", "Right This Second", "Raise Your Weapon", "One Trick Pony"]
s_John_Coltrane = ["Giant Steps", "Cousin Mary", "Countdown", "Spiral", "Syeeda's Flute Song", "Naima", "Mr P.C.", "Giant Steps (alternate version 1)", "Naima (alternate version 1)", "Cousing Mary (alternate take)"]
s_Tigran_Hamasyan = ["Levitation 21", "Our Film", "Ara Resurrected", "At a Post-Historic Seashore", "Space of Your Existence", "The Dream Voyager", "Old Maps", "Vortex", "37 Newlyweds", "New Maps"]
s_Nas = ["The Genesis", "N.Y. State of Mind", "Life's a bitch", "The World Is Yours", "Halftime", "Memory Lane (Sittin' in da Park)", "One Love", "One Time 4 Your Mind", "Represent", "It Ain't Hard To Tell"]
s_Johnny_Cash = ["The Preacher Said, 'Jesus Said'", "Orphan of the Road", "You've Got a New Light Shining in Your Eyes", "If Not For Love", "Man In Black", "Singin' In Viet Nam Talkin' Blues", "Ned Kelly", "Look for Me", "Dear Mrs.", "I talk to Jesus Every Day"]

all_songs = [s_deadmau5 + s_John_Coltrane + s_Tigran_Hamasyan + s_Nas + s_Johnny_Cash]

for i in range(5):
    artist_chosen = random.choice(artist_list)
    if artist_chosen == (artist_list[0]):
        song_choice = random.choice(s_deadmau5)
        print("Now Playing:", song_choice, "\nby:", artist_chosen)
