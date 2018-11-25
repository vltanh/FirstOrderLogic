word('cool', 'English', 'adjective', '/cul/', 'mat').
word('freezing', 'English', 'adjective', '/frizing/', 'lanh cong').
word('cold', 'English', 'adjective', '/cou/', 'lanh ngat').
word('hot', 'English', 'adjective', '/hot/', 'nong').
word('chaud', 'French', 'adjective', '/sau/', 'nong nuc').
word('froid', 'French', 'adjective', '/froid/', 'lanh leo').

word('poor', 'English', 'adjective', '/pur/', 'ngheo').
word('poor', 'English', 'noun', '/pur/', 'nguoi ngheo').

word('record', 'English', 'verb', '/ricod/', 'ghi am').
word('record', 'English', 'noun', '/recod/', 'dia nhac').

word('go', 'English', 'verb', '/go/', 'di').
word('went', 'English', 'verb', '/qent/', 'di (V2)').
word('gone', 'English', 'verb', '/gon/', 'di (V3)').

word('*sreu-', 'Proto-Indo-European', 'base', '/.../', 'chay').

word('rhein', 'Greek', 'verb', '/.../', 'chay').
word('rheuma', 'Latin', 'noun', '/.../', 'dong chay').
word('rime', 'Old French', 'noun', '/.../', 'dong chay').
word('ryme', 'Middle English', 'noun', '/.../', 'nhip dieu').
word('rhyme', 'English', 'noun', '/.../', 'nhip dieu').

word('*pleu-', 'Proto-Indo-European', 'base', '/.../', 'chay').
word('*flo-', 'Proto-Germanic', 'base', '/.../', 'chay').
word('flowan', 'Old English', 'verb', '/.../', 'chay').
word('flow', 'English', 'verb', '/.../', 'chay').

word('fluxus', 'Latin', 'noun', '/.../', 'dong chay').
word('flux', 'English', 'noun', '/.../', 'dong chay').

word('nation', 'English', 'noun', '/neison/', 'quoc gia').
word('national', 'English', 'adjective', '/neisonou/', 'thuoc quoc gia').
word('nationality', 'English', 'noun', '/neisonouliti/', 'quoc tich').
word('nationally', 'English', 'adverb', '/neisonouli/', 'mang tinh quoc gia').

synonymous_('lanh ngat', 'lanh cong').
synonymous_('lanh cong', 'lanh leo').
synonymous_('nong', 'nong nuc').

synonymous(X, X).
synonymous(X, Y) :- synonymous_(X, Y), X \= Y.
synonymous(X, Y) :- synonymous_(Y, X), X \= Y.
synonymous(X, Y) :- synonymous_(X, Z), synonymous_(Z, Y), X \= Y.
synonymous(X, Y) :- synonymous_(Z, X), synonymous_(Z, Y), X \= Y.
synonymous(X, Y) :- synonymous_(X, Z), synonymous_(Y, Z), X \= Y.
synonymous(X, Y) :- synonymous_(Z, X), synonymous_(Y, Z), X \= Y.

antonymous_('nong', 'lanh ngat').

antonymous(X, Y) :- antonymous_(X, Y).
antonymous(X, Y) :- antonymous_(Y, X).
antonymous(X, Y) :- synonymous(X, Z), synonymous(Y, T), antonymous_(Z, T), X \= Z, Y \= T.
antonymous(X, Y) :- synonymous(X, Z), synonymous(Y, T), antonymous_(T, Z), X \= Z, Y \= T.

pronounce(Word, Pronunciation) :- word(Word, _, _, Pronunciation, _).
mean(Word, Definition) :- word(Word, _, _, _, Definition).
type(Word, PartOfSpeech) :- word(Word, _, PartOfSpeech, _, _).
in_language(Word, Language) :- word(Word, Language, _, _, _).

synonym(Word1, Word2) :- mean(Word1, X), mean(Word2, Y), synonymous(X, Y).
antonym(Word1, Word2) :- mean(Word1, X), mean(Word2, Y), antonymous(X, Y).

homophone(Word1, Word2) :- same_language(Word1, Word2), pronounce(Word1, X), pronounce(Word2, X), mean(Word1, Y), mean(Word2, Z), Y \= Z.
homograph(Word1, Word2) :- same_language(Word1, Word2), Word1 == Word2.
heteronym(Word1, Word2) :- homograph(Word1, Word2), pronounce(Word1, X), pronounce(Word2, Y), X \= Y.

same_word_different_language(Word1, Word2) :- synonym(Word1, Word2), in_language(Word1, X), in_language(Word2, X).

same_language(Word1, Word2) :- in_language(Word1, X), in_language(Word2, X).
same_part_of_speech(Word1, Word2) :- type(Word1, X), type(Word2, X).

is_word(X) :- word(X, _, _, _, _).
is_language(X) :- word(_, X, _, _, _).
is_part_of_speech(X) :- word(_, _, X, _, _).
is_pronunciation(X) :- word(_, _, _, X, _).
is_definition(X) :- word(_, _, _, _, X).

is_verb(Word) :- is_word(Word), type(Word, 'verb').
is_adjective(Word) :- is_word(Word), type(Word, 'adjective').
is_noun(Word) :- is_word(Word), type(Word, 'noun').

is_english(Word) :- is_word(Word), in_language(Word, 'English').
is_greek(Word) :- is_word(Word), in_language(Word, 'Greek').
is_latin(Word) :- is_word(Word), in_language(Word, 'Latin').

translate(Word1, Language1, Word2, Language2) :- in_language(Word1, Language1), in_language(Word2, Language2), synonym(Word1, Word2).

tense('go', 'go', 'infinitive').
tense('go', 'went', 'past simple').
tense('go', 'gone', 'past participle').

is_tense(X) :- tense(_, _, X).

same_word_different_tense(Word, Word).
same_word_different_tense(Word1, Word2) :- tense(Word1, Word2, _), Word1 \= Word2.
same_word_different_tense(Word1, Word2) :- tense(Word2, Word1, _), Word1 \= Word2.

% 

relative_('nationally', 'national').
relative_('national', 'nation').
relative_('national', 'nationality').

relative(X, X).
relative(X, Y) :- relative_(X, Y), X \= Y.
relative(X, Y) :- relative_(Y, X), X \= Y.
relative(X, Y) :- relative_(X, Z), relative_(Z, Y), X \= Y.
relative(X, Y) :- relative_(Z, X), relative_(Z, Y), X \= Y.
relative(X, Y) :- relative_(X, Z), relative_(Y, Z), X \= Y.
relative(X, Y) :- relative_(Z, X), relative_(Y, Z), X \= Y.

verb_relative(Word, VerbWord) :- is_verb(VerbWord), relative(Word, VerbWord).
noun_relative(Word, NounWord) :- is_noun(NounWord), relative(Word, NounWord).
adj_relative(Word, AdjWord) :- is_adjective(AdjWord), relative(Word, AdjWord).

% 37 predicates

direct_derive('rhein', '*sreu-').
direct_derive('rheuma', 'rhein').
direct_derive('rime', 'rheuma').
direct_derive('ryme', 'rime').
direct_derive('rhyme', 'ryme').

direct_derive('*pleu-', '*sreu-').
direct_derive('*flo-', '*pleu-').
direct_derive('flowan', '*flo-').
direct_derive('flow', 'flowan').

direct_derive('fluxus', '*pleu-').
direct_derive('flux', 'fluxus').

is_base(Word) :- word(Word, _, 'base', _, _).

indirect_derive(Word, WordFrom) :- direct_derive(Word, WordFrom).
indirect_derive(Word, WordFrom) :- direct_derive(Word, X), indirect_derive(X, WordFrom).

base(Word, BaseWord) :- indirect_derive(Word, BaseWord), is_base(BaseWord).

closest_base(Word, BaseWord) :- is_base(BaseWord), direct_derive(Word, BaseWord).
closest_base(Word, BaseWord) :- direct_derive(Word, X), closest_base(X, BaseWord), not(is_base(X)).

same_base(Word1, Word2) :- base(Word1, X), base(Word2, X), Word1 \= Word2.

common_ancestor(Word1, Word2, WordAncestor) :- indirect_derive(Word1, WordAncestor), indirect_derive(Word2, WordAncestor).

lowest_common_ancestor(Word1, Word2, WordAncestor) :- direct_originate(WordAncestor, X), direct_originate(WordAncestor, Y), indirect_derive(Word1, X), indirect_derive(Word2, Y), X \= Y.

language_oriented_derive(Word, WordFrom, Language) :- indirect_derive(Word, WordFrom), in_language(WordFrom, Language).

greek_derive(Word, WordFrom) :- indirect_derive(Word, WordFrom), is_greek(WordFrom).
latin_derive(Word, WordFrom) :- indirect_derive(Word, WordFrom), is_latin(WordFrom).

direct_originate(Origin, Word) :- direct_derive(Word, Origin).
indirect_originate(Origin, Word) :- indirect_derive(Word, Origin).