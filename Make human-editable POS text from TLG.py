
# coding: utf-8

# In[1]:

from cltk.tag.pos.pos_tagger import POSTag
from cltk.tokenize.sentence.tokenize_sentences import TokenizeSentence
import os
import re


# In[2]:

def extract_tlg_work(file_path, regex_match):
    abs_path = os.path.expanduser(file_path)
    with open(abs_path) as f:
        r = f.read()
    d = re.compile(regex_match)
    m = d.findall(r)
    for x in m:
        work_str = x[1]
    return work_str


# In[3]:

anabasis_path = '~/cltk_data/compiled/tlg/TLG0032.txt'
anabasis_regex = r'(@1 \{1ΚΥΡΟΥ ΑΝΑΒΑΣΕΩΣ Α\}1 @)(.*)( @1 \{1ΚΥΡΟΥ ΠΑΙΔΕΙΑΣ Α\}1 @)'
anabasis_raw = extract_tlg_work(anabasis_path, anabasis_regex)


# In[4]:

def cleanup_tlg_txt(tlg_str):
    # fix beta code transliteration problems
    tlg_str = re.sub(r'ι\+', 'ϊ', tlg_str)
    tlg_str = re.sub(r'ί\+', 'ΐ', tlg_str)
    tlg_str = re.sub(r'\\.', '.', tlg_str)
    # fix tlg markup
    tlg_str = re.sub(r'@1 \{1.+?\}1 @', '', tlg_str) #  rm book titles
    tlg_str = re.sub(r'\[.+?\]', '', tlg_str) #  rm words in square brackets
    tlg_str = re.sub(r'[0-9]', '', tlg_str)
    tlg_str = re.sub(r'@|%|\x00', '', tlg_str)
    tlg_str = re.sub('—', ' — ', tlg_str)
    return tlg_str


# In[5]:

anabasis_clean = cleanup_tlg_txt(anabasis_raw)


# In[6]:

def tokenize_sentences(in_str):
    """tokenize into list of sentences"""
    t = TokenizeSentence()
    out_list = t.sentence_tokenizer(in_str, 'greek')
    return out_list


# In[7]:

anabasis_sentences = tokenize_sentences(anabasis_clean)


# In[8]:

def append_to_file(file_name, pos_str):
    user_data = os.path.expanduser('~/cltk_data/user_data/')
    if not os.path.isdir(user_data):
        os.makedirs(user_data)
    file_name = str('pos_editable_') + str(file_name) + str('.md')
    file_path = os.path.join(user_data, file_name)
    with open(file_path, 'a') as f:
        f.write(pos_str)


# In[9]:

def editable_pos_text(untagged_sentences):
    """POS tag each sentence and print text."""
    p = POSTag()
    counter = 0
    for sentence in untagged_sentences:
        counter += 1
        tagged_words = p.tnt_tagger(sentence, 'greek') #  ~ 6 sec. per sent
        tags_newlines = ''
        unknowns = [] #  mk list of untagged words
        for tagged_word in tagged_words:
            line = str(tagged_word) + '\n'
            tags_newlines = tags_newlines + line
            if tagged_word[1] == 'Unk':
                unknowns.append(tagged_word[0])
        # print str of human-readable sentence
        sent_str_out = """## Sentence %s
### Plaintext
%s
```
### Tagged
%s```
### Unknown words
%s
### Corrected by
['']

""" % (counter, sentence, tags_newlines, unknowns)
        append_to_file('xenophon_anabasis', sent_str_out)


# In[10]:

editable_pos_text(anabasis_sentences)

