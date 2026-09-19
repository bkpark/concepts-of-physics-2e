# X10: incorrect chapter reference in Relativistic Momentum

Checked the live OpenStax pages on 2026-09-19. No erratum submitted by this task;
no X10 correction has been applied to the maintained book.

## Evidence

- [College Physics, 28.5](https://openstax.org/books/college-physics/pages/28-5-relativistic-momentum): the paragraph beginning with the importance of momentum names Work, Energy, and Energy Resources as a chapter devoted to momentum. Its link opens [Chapter 7 introduction](https://openstax.org/books/college-physics/pages/7-introduction-to-work-energy-and-energy-resources).
- [College Physics 2e, 28.5](https://openstax.org/books/college-physics-2e/pages/28-5-relativistic-momentum): the same incorrect chapter title remains, but its link opens [7.1 Work: The Scientific Definition](https://openstax.org/books/college-physics-2e/pages/7-1-work-the-scientific-definition).
- [Chapter 8 in the original edition](https://openstax.org/books/college-physics/pages/8-introduction-to-linear-momentum-and-collisions) and [Chapter 8 in 2e](https://openstax.org/books/college-physics-2e/pages/8-introduction-to-linear-momentum-and-collisions) are Linear Momentum and Collisions. Their chapter contents match the surrounding discussion: momentum, impulse, conservation, and collisions.

## Suggested erratum

Location: Section 28.5, Relativistic Momentum, the opening discussion of momentum
conservation, before the relativistic-momentum definition.

Replace the linked title “Work, Energy, and Energy Resources” with “Linear
Momentum and Collisions” and change the hyperlink to the Chapter 8 introduction.
The sentence describes a whole chapter devoted to momentum, so Chapter 8 is the
appropriate scope; simply changing the destination to Section 8.1 would be less
precise. The wrong title/target persists in both editions checked above.

## Local adaptation

The corresponding maintained chapter is Impulse and Momentum (course Chapter 4).
Use that local chapter title and point to its opening retained module `m42155`,
slug `introduction-to-linear-momentum-and-collisions`, until chapter landing pages
are implemented. The erroneous source link is `m42145`; this is an upstream
reference error, not merely a missing section from the adaptation. Preserve
stable IDs and compute any displayed numbering from the chosen profile.
