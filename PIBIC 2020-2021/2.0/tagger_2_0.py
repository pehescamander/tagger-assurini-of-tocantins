text = open('TEST-SET.txt', 'r', encoding='utf-8')
text = text.read()
text_lower = text.lower()

import nltk
import re

text_clean = re.sub('[.;,-:!?—()]','',text_lower)
with open('TEST-SET-clean.txt', 'w', encoding='utf-8') as f:
  f.writelines(text_clean)

set_list = list(set(text_clean.split()))
set_list.sort()

patterns = [
            (r'asuriní', 'n'),
            (r'a’é', 'dem'),
            (r'.*eokwé', 'dem|-eokwé'),
            (r'.*wyngé', 'dem|-wyngé'),
            (r'.*mén', 'n|-mén'),
            (r'.*moroyró', 'n|-moroyró'),
            (r'.*akoma’é', 'n|-akoma’é'),
            (r'.*akwaháwihi', 'n|-akwaháwihi'),
            (r'.*amýn', 'n|-amýn'),
            (r'.*aosé', 'n|-aosé'),
            (r'.*apýj', 'n|-apýj'),
            (r'.*asýk', 'n|-asýk'),
            (r'.*asýng', 'n|-asýng'),
            (r'hé', 'n'),
            (r'ipirá', 'n'),
            (r'kamará', 'n'),
            (r'osepé', 'n'),
            (r'poraké', 'n'),
            (r'.*kosó', 'n|-kosó'),
            (r'.*sahýa', 'n|-sahýa'),
            (r'saotía', 'n'),
            (r'.*eomí', 'pron.dem|-eomí'),
            (r'.*eopé', 'pron.dem|-eopé'),
            (r'pé', 'pron.dem'),
            (r'né', 'pron.dep'),
            (r'.*sené', 'pron.dep|-sené'),
            (r'isé', 'pron.ind'),
            (r'.*oré', 'pron.ind/pron.dep|-oré'),
            (r'.*ené', 'pron.indep|-ené'),
            (r'.*pehé', 'pron.indep|-pehé'),
            (r'.*a’a', 'n|-a’a'),
            (r'.*’óng', 'n.des|-’óng'),
            (r'^wet', 'pref.corr|wet-'),
]

nom_tagger = nltk.RegexpTagger(patterns)
tags = nom_tagger.tag(set_list)
tags = dict(tags)
print(tags)

for key, value in tags.copy().items():
    if value is None:
        del tags[key]
print(tags)

tags = list(tags)
nom_tagger = nltk.RegexpTagger(patterns)
tags = nom_tagger.tag(tags)
print(tags)

lines = '\n'.join(str(v) for v in tags)
clean_lines = re.sub('[,()\']','',lines)
clean_lines = clean_lines.replace(' ','\t')

with open('output_tags.txt', 'w', encoding='utf-8') as f:
  f.writelines(clean_lines)

import pandas as pd

glossary = 'output_tags.txt'

with open('TEST-SET-clean.txt', 'r', encoding='utf-8') as f:
    infile = f.readlines()

df = pd.read_csv(glossary, sep='\t', header=None, index_col=0)
glossary = df.to_dict()[1]

outlines = []

for line in infile:
    list_of_words = line.lower().split()

    new_line = ''

    for word in list_of_words:

        if word in glossary:
            new_line += word + '\\' + glossary[word] + ' '
        else:
            new_line += word + ' '

    outlines.append(new_line.strip() + '\n')

with open('TEST-SET-tagged.txt', 'w', encoding='utf-8') as f:
    f.writelines(outlines)

read = open('TEST-SET-tagged.txt', 'r', encoding='utf-8')
print(read.read())
