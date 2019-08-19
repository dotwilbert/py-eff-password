# py-eff-password

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
