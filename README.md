# Japanese Names frequency

## Source

The name list was obtained from "ENAMDICT/JMnedict - Japanese Proper Names Dictionary Files", available [here](http://www.edrdg.org/enamdict/enamdict_doc.html).

The entries that do not start with a kanji were removed to exclude foreign names.
It was done by simply finding the first entry starting with a kanji and removing the previous entries, since the ones starting with hiragana or katakana precede the kanji ones.
The last entry on the file was one consisting of kanji, so there was nothing to remove from the end of the file.
The resulting filename is called [`filtered`](filtered).

That list was split into a male and a female given names, the others were ignored.
There is already a family name Anki deck available on Ankiweb.

To remove all the entries that are not a (fe)male given name the lines containing the regexp were `^.*/([^m]{1-8}).*\n` replaced by nothing.
The entries that can be from more than one category were also removed using `^.*/(.,.+).*\n`.
The list of male (female) given names is called [male](male) and [female](female).
There are 97008 female given names and 19025 male ones.

There are several entries with the same key, i. e. homographs that have different readings.
They were all merged together to have only one keyword to search for each of them.
After that, there are 16484 entries of [male given names](male-merged) and 77171 for [female given names](female-merged).

A simple script was written to scrap the search page from yahoo.co.jp and get the number of hits from each entry.
The proxy rotation came [from here](https://codelike.pro/create-a-crawler-with-rotating-ip-proxy-in-python/), but it doesn't seem to work consistently, maybe it is due the bot protection from yahoo.

The files from enamdictl are not encoded with `utf8`, and it has to be reencoded to work with python.
It can be done in Emacs by opening it, using `M-a revert-buffer-wth-coding-system > japanese-iso-8bit` to display the characters correctly.
Then `M-a set-buffer-file-coding-system utf-8` and save the file.

I've started processing the male names on 20200325.


