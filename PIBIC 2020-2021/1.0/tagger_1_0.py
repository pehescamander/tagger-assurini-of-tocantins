import pandas as pd

tags = 'tags-assurini-to.txt'

with open('TEST-SET.txt', 'r', encoding='utf-8') as f:
    infile = f.readlines()

df = pd.read_csv(tags, sep='\t', header=None, index_col=0)
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