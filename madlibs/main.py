import madlibs

Madlibs = madlibs.open_madlib_file()
Madlib = madlibs.get_random_madlib(Madlibs)
Madlib = madlibs.change_words(Madlib)
print(Madlib)
