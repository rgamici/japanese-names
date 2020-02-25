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
The list of male (female) given names is called [male](male) and [female](female). 


