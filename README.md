# Japanese Names frequency

## Source

The name list was obtained from "ENAMDICT/JMnedict - Japanese Proper Names Dictionary Files", available [here](http://www.edrdg.org/enamdict/enamdict_doc.html).

The entries that do not start with a kanji were removed to exclude foreign names.
It was done by simply finding the first entry starting with a kanji and removing the previous entries.
Since the ones starting with hiragana or katakana precede the kanji ones, they were also removed by the same operation.
The last entry on the file was one consisting of kanji, so there was nothing to remove from the end of the file.
The resulting filename is called [`filtered`](filtered).

That list was split into a male and a female given names, the others, surnames, places, etc., were ignored.
There is already a family name Anki deck available on Ankiweb, and because of that I will not scrap them.

To remove all the entries that are not a (fe)male given name the lines containing the regexp were `^.*/([^m]{1-8}).*\n` replaced by nothing.
The entries that can be from more than one category were also removed using `^.*/(.,.+).*\n`.
The list of male (female) given names is called [male](male) and [female](female).
There are 97008 female given names and 19025 male ones.

There are several entries with the same key, i. e. homographs that have different readings.
They were all merged together to have only one keyword to search for each of them, because there is no way to automatically discern which read correspond the results.
After that, there are 16484 entries of [male given names](male-merged) and 77171 for [female given names](female-merged).

A [simple script](search.py) was written to scrap the search page from yahoo.co.jp and get an approximate number of hits from each entry.
It is not perfect, but it may give an idea of which names are the most common.
There are also some names that are also common words, like 一年 and 一人, that have to be filtered later, because the number of hits may come mostly from the common words.
The results are the files with a suffix `-count`.

The proxy rotation came [from here](https://codelike.pro/create-a-crawler-with-rotating-ip-proxy-in-python/), but it doesn't seem to work consistently, maybe it is due the bot protection from yahoo.

The files from enamdict are not encoded with `utf8`, and they have to be reencoded to work with python.
It can be done in Emacs by opening it, using `M-a revert-buffer-wth-coding-system > japanese-iso-8bit` to display the characters correctly.
Then `M-a set-buffer-file-coding-system utf-8` and save the file.

Another script was written to tag the names who are also present as an entry in edict2, i.e., words that are also used as names.
Those words were tagged, because it is probable that most of the results in a web search come from the word and not from the name.
The processed list, including the count results, are named with the prefix `-finished`.


## Anki Deck

After finish processing the entries, the list of names was transformed into a Anki deck.
The fields include both the kana and romaji readings, and the count results are also included to sort the names by it.

All the entries are included, but a shortlist can be provided by request on github.

I tried to order the due cards by the result counts decreasing, but I'm not sure if the scheduling will be preserved.
If not, it is necessary to modify the sort field in "Manage Note Types" to order them by count.

The decks with the male names was posted on ankiweb, and it can be found [here](https://ankiweb.net/shared/info/1905821603).


