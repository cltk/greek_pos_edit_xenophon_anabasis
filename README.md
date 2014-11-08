# About
The file `pos_editable_xenophon_anabasis.md` is a human–editable POS–tagged text of [Xenohphon's *Anabasis*](https://en.wikipedia.org/wiki/Anabasis_%28Xenophon%29). Any GitHub user can check the quality of a sentence's POS tags, fix or confirm it, and give one's name.

The text was tagged using (the CLTK's TnT tagger](http://docs.cltk.org/en/latest/greek.html#tnt-tagger). The file `Make human-editable POS text from TLG.py` generated `pos_editable_xenophon_anabasis.md`, which was then broken down into files for each book.

Once the *Anabasis* has been tagged, in part or in full, it will be added to (the CLTK's POS tagging training set](https://github.com/cltk/greek_treebank_perseus/blob/master/greek_training_set.pos).

# How to edit
To begin editing, make a free GitHub user account, [fork this repository](https://help.github.com/articles/fork-a-repo/), pick a book, find a sentence which has not been edited, and check and fix the tags. Then, [submit a pull request](https://help.github.com/articles/creating-a-pull-request/).


# POS tags
This text uses the Perseus project's POS tags. ([Read about it here](http://nlp.perseus.tufts.edu/syntax/treebank/greek.html).)

1: 	part of speech

	n	noun
	v	verb
	t	participle
	a	adjective
	d	adverb
	l	article
	g	particle
	c	conjunction
	r	preposition
	p	pronoun
	m	numeral
	i	interjection
	e	exclamation
	u	punctuation

2: 	person

	1	first person
	2	second person
	3	third person

3: 	number

	s	singular
	p	plural
	d	dual

4: 	tense

	p	present
	i	imperfect
	r	perfect
	l	pluperfect
	t	future perfect
	f	future
	a	aorist

5: 	mood

	i	indicative
	s	subjunctive
	o	optative
	n	infinitive
	m	imperative
	p	participle

6: 	voice

	a	active
	p	passive
	m	middle
	e	medio-passive

7:	gender

	m	masculine
	f	feminine
	n	neuter

8: 	case

	n	nominative
	g	genitive
	d	dative
	a	accusative
	v	vocative
	l	locative

9: 	degree

	c	comparative
	s	superlative

---

For example, the postag for the noun "a)/ndra" is "n-s---ma-", 
which corresponds to the following features:

1: n	noun
2: -
3: s	singular
4: -
5: -
6: -
7: m	masculine
8: a	accusative
9: -


# License
The MIT License (see `LICENSE`). The Greek text is public domain, [Marchant's *Xenophontis opera omnia* (Oxford's OCT, 1904)](http://books.google.com/books?id=4rQ4AQAAMAAJ&printsec=frontcover&dq=Xenophontis+opera+omnia+marchant&hl=en&sa=X&ei=i4NdVK28J4X1iQL13IHADg&ved=0CB0Q6AEwAA#v=onepage&q=Xenophontis%20opera%20omnia%20marchant&f=false).