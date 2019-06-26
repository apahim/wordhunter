Word Hunter
===========

This is a Word Hunter application.

Install
-------

To install, use:

```
$ pip install .
```

Run
---

To run, execute:

```
$ wordhunter --wordlist selftests/data/words.txt --dimension 4
Matrix 4x4:
  ['a', 'g', 'm', 'i']
  ['m', 'e', 'f', 'h']
  ['u', 'i', 'n', 'k']
  ['w', 'z', 's', 'i']
Wordlist number of words: 62799
The hunter has found 13 words:
['mi', 'if', 'ks', 'is', 'em', 'me', 'ma', 'in', 'mu', 'hi', 'ink', 'am', 'um']
```

Where:
 - The `--wordlist` is a file containing one valid word per line.
 - The `--dimension` is the size of the matrix side. E.g. a dimension `4`
 will generate a 4x4 matrix.

For additional information, run `wordhunter --help`

Test
----

You can run the selftests with:

```
$ python selftests/run.py
```

Performance
-----------

The Word Hunter was optimized for performance. To do that, some
design decisions were made:

- The wordlist file is retrieved line by line, avoiding excessive
  memory consumption.
- The wordlist file content is parsed into a Python dictionary for
  fast lookup.
- The hunter helpers are matching the words in both normal and
  reversed order to avoid extra loop for the reversed words.
- The wordlist lookup uses `try`/`except` and key access instead
  of a loop like `for word in wordlist`, so the lookup time is
  O(1) in the average case.

All together, the entire execution for a default 15x15 matrix was kept
under half second:

```bash
$ time wordhunter --wordlist selftests/data/words.txt --dimension 15
Matrix 15x15:
  ['w', 'b', 'c', 'j', 'x', 'q', 'z', 'e', 'j', 'a', 'x', 'k', 'f', 'e', 'l']
  ['a', 'q', 'e', 'f', 'k', 'y', 'c', 'z', 'o', 'f', 'f', 'e', 'v', 'b', 'c']
  ['g', 'w', 'v', 't', 'j', 'g', 'l', 't', 't', 'm', 'p', 'x', 't', 's', 'i']
  ['y', 'n', 'r', 'x', 'b', 'm', 'p', 'e', 'w', 'h', 'b', 'r', 'p', 'h', 'f']
  ['d', 'e', 'd', 'k', 'w', 'a', 'y', 'b', 'u', 'w', 's', 'f', 'w', 'o', 'm']
  ['u', 'b', 's', 'm', 'p', 's', 'l', 'r', 'k', 'b', 'v', 'p', 'a', 'g', 'k']
  ['i', 'x', 'n', 'v', 'g', 'o', 'f', 'w', 'z', 'e', 'q', 'c', 't', 'p', 'i']
  ['m', 'j', 'j', 'u', 'f', 'k', 'w', 'k', 'o', 'r', 't', 'm', 'w', 'p', 'o']
  ['l', 'i', 'z', 'c', 'l', 'g', 'y', 'j', 'c', 'x', 'r', 'g', 'u', 'n', 'w']
  ['c', 'j', 'x', 'h', 't', 'g', 'n', 'z', 'c', 'p', 'k', 'n', 'i', 'm', 's']
  ['x', 'g', 'y', 'n', 'u', 'w', 'g', 'v', 'i', 'a', 'x', 'z', 'm', 'd', 'l']
  ['e', 'v', 'u', 'i', 'q', 'j', 'z', 'h', 'u', 'p', 'a', 's', 'b', 'j', 'a']
  ['s', 'd', 'i', 'w', 'v', 'i', 'o', 'w', 'z', 'w', 'd', 't', 'r', 'w', 'r']
  ['p', 'o', 'z', 'r', 'j', 'g', 'b', 'g', 'n', 'o', 'u', 'f', 'd', 's', 'k']
  ['x', 'c', 'o', 'u', 'n', 'u', 'o', 'u', 'k', 'm', 'x', 'p', 'p', 'm', 't']
Wordlist number of words: 62799
The hunter has found 96 words:
['up', 'ax', 'sap', 'la', 'wag', 'act', 'gap', 'as', 'ad', 'via', 'ho', 'if', 'fa', 'lark', 'ink', 'doc', 'be', 'owl', 'my', 'hi', 'ye', 'hip'
, 'mink', 'zip', 'pun', 'pas', 'yaw', 'yet', 'ls', 'ay', 'ark', 'jig', 'ts', 'sex', 'um', 're', 'rs', 'am', 'we', 'apt', 'mas', 'ox', 'lo', 'f
og', 'ks', 'pa', 'to', 'is', 'cod', 'ids', 'gs', 'mow', 'id', 'way', 'no', 'ms', 'ex', 'or', 'mu', 'mum', 'on', 'mix', 'pap', 'sh', 'off', 'by
', 'so', 'jog', 'dig', 'do', 'gun', 'oh', 'win', 'pi', 'es', 'kc', 'ma', 'dun', 'pew', 'cs', 'ow', 'go', 'hog', 'lab', 'uh', 'yes', 'bet', 'of
', 'at', 'in', 'vs', 'nu', 'fly', 'jot', 'mi', 'ohs']

real    0m0.451s
user    0m0.000s
sys     0m0.030s

```
