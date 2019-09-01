# py-eff-password

The original idea to use dice for password generation came from [Arnold G. Reinhold](http://world.std.com/~reinhold/diceware.html). [Wikipedia](https://en.wikipedia.org/wiki/Diceware) discusses Diceware&trade; and references the year 1995. Reinhold trademarked Diceware&trade;.

## EFF

Generate passwords according to https://www.eff.org/dice. It uses the long word list, that has been optimized for memorability, readability and ease of input, or more general, usability.

The following table is a indication of of the password strength

| # words | bits of entropy |
|:-------:|----------------:|
| 3 | ~38 |
| 4 | ~51 |
| 5 | ~64 |
| 6 | ~77 |

Every additional word adds ~12.9 bits of entropy<sup>1</sup>. 
Choosing 6 words gives the same security as a 15 character password randomly chosen from lowercase letters and digits: 7776<sup>6</sup> = (6<sup>5</sup>)<sup>6</sup> = 6<sup>30</sup> = (6<sup>2</sup>)<sup>15</sup> = 36<sup>15</sup> = (26 + 10)<sup>15</sup> <!-- $7776^6 = (6^5)^6 = 6^{30} = (6^2)^{15} = 36^{15} = (26 + 10)^{15}$ -->. The advantage of 6 words from the list is that they are easier to remember and they are as hard to brute force as the mentioned 15 randomly chosen characters.

<sup>1</sup>https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases

## Usage

```bash
./gen_eff_pwd.py --help
```

```plain
usage: gen_eff_pwd.py [-h] [-n NUMBER_OF_PASSWORDS] [-w NUMBER_OF_WORDS]
                      [-s SEPARATOR] [-p POSTFIX] [-c]

Generate Passwords

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_OF_PASSWORDS, --number_of_passwords NUMBER_OF_PASSWORDS
                        number of passwords to generate (default 1)
  -w NUMBER_OF_WORDS, --number_of_words NUMBER_OF_WORDS
                        number of words per password (default 5)
  -s SEPARATOR, --separator SEPARATOR
                        separator between words
  -p POSTFIX, --postfix POSTFIX
                        characters to append to password. Some websites
                        require special characters and numbers. Examples to
                        use are '5$' or '2#'
  -c, --capitalize      capitalize the words used in the passwords (default
                        false). Some websites require upper- and lowercase.
```

```bash
./gen_eff_pwd.py -n 5 -w 7 -s '^' -p '5#' -c
```

```plain
Armed^Perfected^Quarters^Plaza^Speed^Hardhead^Goal5#
Radiance^Among^Helium^Tighten^Implicate^Scored^Maximize5#
Giggling^Prelude^Fable^Seventeen^Declared^Procreate^Darling5#
Angriness^Unlivable^Shampoo^Celibacy^Matted^Depose^Unscented5#
Foam^Handled^Vaporizer^Contact^Chemo^Trodden^Fetch5#
```

# Development tools

To generate the content of the eff_wordlist dictionary:

```bash
curl -sS "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt" | ./4on1.awk > list.lst
```

You can copy the content, after removing the last comma, in the source code, in case the list is updated. Just get the new url. Or you can use your own word list if it provides better usability.

```bash
./4on1.awk my_better_wordlist.txt > list.lst
```