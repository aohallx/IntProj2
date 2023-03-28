# With all cited information derived from tunebat.com, bigtimemusicians.com and
# lloydworldofaudio.wordpress.com/2016/06/17/genre-analysis-shoegaze
# ...................................................................
# Aidan O'Halloran, 2.4.2023
# This is a custom album designer.


welcome = input("   Welcome! Press enter to continue ")
print(welcome)

genre = input("Pick a music genre! ")
print("Ah. ", genre,
      end=".""\nShoegaze is " + "very, " * 2 + "new genre. It is "
                                               "one of my favorite genres.")
print(
    "\nDid you know: In the early 2000s, guitarists that played "
    "music of this "
    "'gazey' sounding genre would have many effects coming "
    "from thier guitar.")
print(
    "\nThey would often be seen as looking down to change "
    "effects on thier pedals.")
print("\nThus, the genre called 'Shoegaze' had originated.")
# ^^^^ I had multiplied and added these operators to emphasize a
# genre's importance

# Next line of code asks user to enter # of songs in album
song_amount = int(input("****This is a custom album builder. "
                        "Enter the amount of songs in your album: "))
print(song_amount)

# Next code will be based off an average statistic from bigtimemusicians.com .
# Given their average rock song is 4:15 in length, let's apply this.
# 4:15 in seconds is 255s. Duration in mins multiplies
# by avg seconds in a song, divides by 60s.
print("\nEstimated album duration in seconds: ",
      song_amount * 255)
duration = song_amount * 255 / 60
print("Estimated album duration in minutes: ", duration,
      "minutes long", sep=" ")
continue1 = input("\n- Press enter on your keyboard to continue.")

# Next line of code adds a filler song, which basically is an extra song.
# 'filler' adds duration + 1 song times 255/60
filler_total_album = song_amount * 255 / 60 + 255 / 60
round_filler = filler_total_album // 1
round_filler_sec = filler_total_album - round_filler ** 1
round_filler_0 = filler_total_album % filler_total_album
print(
    "\nWe are going to add another song as an end filler. "
    "New album duration: ",
    filler_total_album, ", or ", round_filler, "minutes with ",
    round_filler_sec - round_filler_0, "of a minute long.", sep=" ")
print("Wow! This is a pretty short album.")
print("\nLet's estimate more of what this album will sound like. ")
print(continue1)
# Now we are going to calculate the bpm of each song.
print(
    "Lloydworldofaudio.com states, after studying the Shoegaze genre, "
    "''played... set to a slow tempo of 93 Bpm. "
    "Slow tempo was a common thing and a big part of the genre.''")
continue2 = input("\n- (Press Enter)")
bpm_total_estimate = 93 * filler_total_album
# ^ 93bpm times the album's minutes = # of beats
print(
    "\nThe total amount of beats on this album will be around",
    int(bpm_total_estimate // 1), "beats long. ")
print("- ... So...")
print(
    "Say you want your songs to have an average of 120 or 140 beats "
    "per minute(bpm).")
bpm_alt_120_not_rounded = (120 * filler_total_album)
bpm_alt_140_not_rounded = (140 * filler_total_album)
bpm_alt_120 = int(bpm_alt_120_not_rounded // 1)
bpm_alt_140 = int(bpm_alt_140_not_rounded // 1)
# ^^^ Rounded the bpm to integer place. Put int in for I can calculate strings
print("\nFor an average of 120 bpm, the album will be",
      bpm_alt_120, "beats long. ")
print("For an average of 140 bpm, the album will be",
      bpm_alt_140, "beats long. ")
continue4 = input("\n- (Press Enter)")
print(continue4)

custom_input_question = input(
    "\nOkay. Theses are given bpms, so how many beats per minute do "
    "you want your songs to be? ")
custom_input_unrounded = int(custom_input_question) * filler_total_album
custom_input = int(custom_input_unrounded // 1)
print(custom_input_question)
print(
    "\nHere we are. Your album with a custom input of", custom_input_question,
    "bpm generates the album an estimated", custom_input, "beats in total. ")

print(continue4)
print("Thus.. with a genre of", genre, "your album is unique")
print(custom_input, "beats per minute is uniquely yours.")
what_instrument = input("What instrument would you play in this genre? ")
print(what_instrument, "is an interesting instrument.")
played_before_or_no = input("Have you played this instrument before? ")
print("\nAh, I see.")
print("Thanks for tuning in!")
print("THE END")
continue_to_int_2 = input("Press enter to continue! ")
print(continue_to_int_2)

# Aidan O'Halloran, 3.20.2023
# Integration Project II (I-continued):
# An already made playlist of songs to be filtered by
# chord progression number, year, artist, key, bpm
# ...................................................................
# With all cited information derived from tunebat.com, bigtimemusicians.com,
# lloydworldofaudio.wordpress.com/2016/06/17/genre-analysis-shoegaze,
#                                        and open.spotify.com/search.
#                        * ( CRT-ALT-L FORMATS CODE ) *
# _________ (This code I ran because it ____)


list_of_all_songs = "Modern Color - Pale" \
                    "\nModern Color - Skipping stones\nMac Miller - Uber\n" \
                    "Kanye West - Flashing Lights" \
                    "\nMobb Deep  - Shook Ones Pt. II" \
                    "\nBedroom    - In My Head\n" \
                    "Surf Curse - Forever Dumb" \
                    "\nKanye West & Jay Z - Primetime"


# what_filter_function_full is the function calling for asking a question
# for what filter the user wants. then goes to main (want to continue)


def what_filter_function_full():
    print("Here is a list of songs I have selected.")
    print(list_of_all_songs)
    filter_by_what = input("What do you want to filter by?\n\n   "
                           "Filter by:\n Year - "
                           "'year'\n Music Genre - 'genre'\n\nEnter here: ")
    while filter_by_what != "year" and filter_by_what != "genre":
        print("Sorry, this is not a filter.\n")
        what_filter_function_full()
        break
    if filter_by_what == "year":
        main(filter_by_what)
    if filter_by_what == "genre":
        main(filter_by_what)


# Song Functions: (Calling for song infos bwlow):


def shook_ones():
    shook_ones_artist = "Mobb Deep"
    shook_ones_bpm = 94
    print("Here is all the information about this song. It is written by",
          shook_ones_artist, "and is", shook_ones_bpm, "bpm.\n")
    main3()


def uber():
    uber_artist = "Mac Miller"
    uber_bpm = 170
    print("Here is all the information about this song. It is written by",
          uber_artist, "and is", uber_bpm, "bpm.\n")
    main3()


def flashing_lights():
    flashing_lights_artist = "Kanye West"
    flashing_lights_bpm = 90
    print("Here is all the information about this song. It is written by",
          flashing_lights_artist, "and is", flashing_lights_bpm, "bpm.\n")
    main3()


def in_my_head():
    in_my_head_artist = "Bedroom"
    in_my_head_bpm = 151
    print("Here is all the information about this song. It is written by",
          in_my_head_artist, "and is", in_my_head_bpm, "bpm.\n")
    main3()


def forever_dumb():
    forever_dumb_artist = "Surf Curse"
    forever_dumb_bpm = 171
    print("Here is all the information about this song. It is written by",
          forever_dumb_artist, "and is", forever_dumb_bpm, "bpm.\n")
    main3()


def primetime():
    primetime_artist = "Jay Z and Kanye West"
    primetime_bpm = 85
    print("Here is all the information about this song. It is written by",
          primetime_artist, "and is", primetime_bpm, "bpm.\n")
    main3()


def pale():
    pale_artist = "Modern Color"
    pale_bpm = 77
    print("Here is all the information about this song. It is written by",
          pale_artist, "and is", pale_bpm, "bpm.\n")
    main3()


def skipping_stones():
    skipping_stones_artist = "Modern Color"
    skipping_stones_bpm = 138
    print("Here is all the information about this song. It is written by",
          skipping_stones_artist, "and is", skipping_stones_bpm, "bpm.\n")
    main3()


# function below asks what year, then if its in range the original question
# for what to filter by follows with its function

def main(filter_by_what):
    while filter_by_what == "year":
        asked_year = int(input("What year was your favorite? "
                               " \n*Note: The latest year possible"
                               " is 2023 and first is 0000* : "))
        if asked_year in range(0, 2023):
            filter_by_year(asked_year)
        if asked_year not in range(0, 2023):
            print("Sorry, this is not after year 0 and before 2023.")
            main(filter_by_what)
        break
    if filter_by_what == "genre":
        asked_genre = input("What genre would you like to filter by?"
                            " \nGenres: \nShoegaze, Rap, Hip Hop "
                            "and Indie\nGenre : ")
        filter_by_genre(asked_genre)


# if year inputted, move to function below (year info):


def filter_by_year(asked_year):
    print("\n", asked_year, ", a magnificent year...")
    year_up_or_down = input("Do you want this list from most recent to "
                            "oldest? (yes or no) : ")
    while True:
        if year_up_or_down == "yes":
            print("\n2020: Modern Color - Pale"
                  "\n2017: Bedroom - In My Head"
                  "\n2016: Modern Color - Skipping Stones"
                  "\n2015: Surf Curse - Forever Dumb"
                  "\n2014: Mac Miller - Uber"
                  "\n2011: Jay Z and Kanye West - Primetime"
                  "\n1995: Mobb Deep - Shook Ones Pt. II")
            ready_to_main4()
            break
        if year_up_or_down == "no":
            print(
                "\n1995: Mobb Deep - Shook Ones Pt. II"
                "\n2011: Jay Z and Kanye West - Primetime"
                "\n2014: Mac Miller - Uber"
                "\n2015: Surf Curse - Forever Dumb"
                "\n2016: Modern Color - Skipping Stones"
                "\n2017: Bedroom - In My Head"
                "\n2020: Modern Color - Pale")
            ready_to_main4()
        else:
            print("Not an answer. Enter another.. ")
            filter_by_year(asked_year)
        break


# if genre inputted, move to next definition about genres:

def filter_by_genre(asked_genre):
    while asked_genre != "Shoegaze" and asked_genre != "Indie" \
            and asked_genre != "Rap" and asked_genre != "Hip Hop":
        asked_genre = input("Sorry, this is not a genre listed.\nWhat genre? ")
    while asked_genre == "Shoegaze":
        shoegaze_genre_function()
        break
    while asked_genre == "Indie":
        indie_genre_function()
        break
    while asked_genre == "Rap":
        rap_genre_function()
        break
    while asked_genre == "Hip Hop":
        hip_hop_genre_function()
        break
    return


# down functions are functions including songs by genre. then goes to
# ready_to_main4() which is another bridge type of function to continue.

def hip_hop_genre_function():
    print("Kanye West - Flashing Lights\nMac Miller - Uber")
    ready_to_main4()


def shoegaze_genre_function():
    print("Modern Color- Pale\nModern Color - Skipping Stones")
    ready_to_main4()


def rap_genre_function():
    print("\nMobb Deep - Shook Ones Pt. II\nKanye West & Jay Z: Primetime\n")
    ready_to_main4()


def indie_genre_function():
    print("\nBedroom - In My Head\nSurf Curse - Forever Dumb\n")
    ready_to_main4()


# first question asked below


def first():
    want_to_start = input("\nDo you want to start? (yes or no): ")
    while want_to_start != "yes" and want_to_start != "no":
        print("Sorry, that is not an appropriate answer. \n ")
        want_to_start = input("\nDo you want to start? (yes or no): ")
    while want_to_start == "yes":
        song_info_question = input("What song would you like to know about?\n"
                                   "modern color - pale"
                                   "\nmodern color - skipping stones\nmac "
                                   "miller - uber\n"
                                   "kanye west - flashing lights"
                                   "\nmobb Deep  - shook ones pt. II"
                                   "\nbedroom    - in my head\n"
                                   "surf curse - Forever Dumb"
                                   "\nkanye west & jay z - primetime"
                                   "\n: ")
        while song_info_question != "pale" and \
                song_info_question != "skipping stones" \
                and song_info_question != "uber" \
                and song_info_question != "flashing lights" \
                and song_info_question != "shook ones pt ii" \
                and song_info_question != "in my head" \
                and song_info_question != "forever dumb" \
                and song_info_question != "primetime" \
                and want_to_start == "yes":
            song_info_question = input(
                "Sorry, that is not a song listed.\n"
                "\nWhat song would you like to know about?\n"
                "modern color - pale"
                "\nmodern color - skipping stones\nmac "
                "miller - uber\n"
                "kanye west - flashing lights"
                "\nmobb Deep  - shook ones pt. II"
                "\nbedroom    - in my head\n"
                "surf curse - Forever Dumb"
                "\nkanye west & jay z - primetime"
                "\n: ")
        if song_info_question == "pale" and want_to_start != "no":
            pale()
        elif song_info_question == "skipping stones" and want_to_start != \
                "no":
            skipping_stones()
        elif song_info_question == "primetime" and want_to_start != \
                "no":
            primetime()
        elif song_info_question == "forever dumb" and want_to_start != \
                "no":
            forever_dumb()
        elif song_info_question == "in my head" and want_to_start != \
                "no":
            in_my_head()
        elif song_info_question == "shook ones pt ii" and want_to_start != \
                "no":
            shook_ones()
        elif song_info_question == "flashing lights" and want_to_start != \
                "no":
            flashing_lights()
        elif song_info_question == "uber" and want_to_start != \
                "no":
            uber()
        else:
            print("What a song!\n")
        return
    while want_to_start == "no":
        print("Okay then. \n")
        what_filter_function_full()
        break


# bridge function below, then what_filter_function_full asks for
# the user to filter by a genre or year


def main3():
    want_to_continue = input("\nDo you want to continue? (yes or no): ")
    while want_to_continue != "yes" and want_to_continue != "no":
        print("Sorry, that is not an appropriate answer. \n ")
        want_to_continue = input("\nDo you want to continue? (yes or no): ")
    while want_to_continue == "yes":
        what_filter_function_full()
        break
    if want_to_continue == "no":
        print("\nHere is the other segment! \n")
        what_filter_function_full()
    return


def ready_to_main4():
    ready_for_4 = input("Are you ready for the final segment? (yes or no) ? ")
    if ready_for_4 == "yes":
        main4()
    if ready_for_4 != "yes":
        print("We are going to go anyway.\n")
        main4()


# last set of questions below. all combinations of inputs eventually leads to
# def main4(), first(), and ready_to_main4() .


def main4():
    year = 1996
    while year in range(1996, 2013):
        print("If you are born in ", year, ":", sep="")
        year += 1
    print("\nYou are a part of 'Gen Z!\n")

    random_num = 1
    while random_num in range(1, 5):
        star = "*"
        star *= 24
        print(star)
        break

    year = 1995
    while year in range(1980, 1996):
        print("If you are born in ", year, ":", sep="")
        year -= 1
    print("\nYou are a Millennial!\n")

    random_num = 50
    while random_num in range(1, 2001):
        random_num /= 2
        print("*" * 24)
        break

    age = int(input("How old are you now? "))
    if age in range(1, 120):
        print("Wow.", age, "years old.")
        if 1 < age < 26:
            ''' ( in 2023) '''
            print("Gen Z. You were alive for 7/8 of these songs.")
        if 26 < age < 43:
            print("Millennial. Yoy were only alive for Mobb Deep - "
                  "Shook Ones Pt. II !")
        if age < 0 or age > 130:
            print("Sorry, out of range.")
    print("Thanks for tuning in.\n")


first()
