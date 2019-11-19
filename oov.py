import re
import collections
import matplotlib.pyplot as plt
from numpy import array


greek = open('corpora/corpus.el', "r", encoding='utf-8').read()
german = open('corpora/corpus.de', "r", encoding='utf-8').read()
bulgarian= open('corpora/corpus.bg', "r", encoding='utf-8').read()
finnish = open('corpora/corpus.fi', "r", encoding='utf-8').read()
french= open('corpora/corpus.fr', "r", encoding='utf-8').read()
maltese = open('corpora/corpus.mt', "r", encoding='utf-8').read()

# want to get all Unicode non alphabets(punctuations) to remove all symbols whichd are neither
# alphabets nor whitespaces
def getNonAlph():
    count0 = 0
    count = 1
    regExbhp = ""
    for x in range(1, pow(2, 16)):

        if ((chr(x).isalpha()) | (chr(x).isspace())):
            continue
        else:
            if (count == 1):
                regExbhp += "[\\u%04x|" % ord(chr(x))
            elif (count == 16768):
                regExbhp += "\\u%04x]" % ord(chr(x))
            else:
                regExbhp += "\\u%04x|" % ord(chr(x))
            count0 = count0 + 1
        count = count + 1
    return regExbhp

nonAlphabets = getNonAlph()  # contains a regular expression obtained for getNonAlph()

""" processing(corpus) function takes a corpus as input and do the following:
 Regex pattern to remove non-alphabets except whitespaces
 Remove non-alphabets using regex pattern
 remove whitespace, punct and lowercase all the charecters"""
def processing(x):
    patt = re.compile(nonAlphabets, re.MULTILINE)  #
    x = patt.sub('', x)  #
    x = x.lower().strip().split() #
    return x


greek = processing(greek)
german = processing(german)
maltese = processing(maltese)
french = processing(french)
finnish = processing(finnish)
bulgarian = processing(bulgarian)


"""[a] Partition each corpus into a training corpus (80% of the word tokens) and a test corpus
(20% of the word tokens)."""
corpus = [bulgarian, greek, german, french, maltese, finnish]

"""partition(x) function takes as input a list that contains all the languages and return two lists: train and 
test that contain the languages partitioned 80%, 20%"""
def partition(x):

    train = [] #train corpus of bulgarian, greek, german, french, maltese, finnish in order
    test = [] #test corpus of bulgarian, greek, german, french, maltese, finnish in order
    for i in x:
        n = len(i)
        train_set = i[:int((n * 0.8))]
        test_set = i[int((n * 0.8)):]
        train.append(train_set)
        test.append(test_set)

    return  train, test
train_data, test_data = partition(corpus)


"""(b) Construct a vocabulary for each language by taking the most frequent 15k word types in
the training corpus. The vocabulary set should be ranked by frequency from the most
frequent to the least frequent."""


"""create the test data for different langauges"""
el_test = test_data[0]
bg_test = test_data[1]
de_test = test_data[2]
fr_test = test_data[3]
mt_test = test_data[4]
fi_test = test_data[5]

el_train = train_data[0]
bg_train = train_data[1]
de_train = train_data[2]
fr_train = train_data[3]
mt_train = train_data[4]
fi_train = train_data[5]
"""(c) Compute OOV rate (percentage) on the test corpus as the vocabulary grows by 1k words."""
def vocabulary(x, c):
    cnt = collections.Counter()
    for word in x:
        cnt.update([word])
    voc = cnt.most_common(c)
    return  voc

def ovv_rate(voc, test):
    unseen = [x for x in test if x  not in voc]
    rate = len(unseen)/len(voc)
    return rate

"""before increasing the vocabulary value by 1k words"""
# print("Ovv rate for greek: ", ovv_rate(el_voc, el_test))
# print("Ovv rate for bulgarian: ", ovv_rate(bg_voc, bg_test))
# print("Ovv rate for german: ", ovv_rate(de_voc, de_test))
# print("Ovv rate for french: ", ovv_rate(fr_voc, fr_test))
# print("Ovv rate for malteese: ", ovv_rate(mt_voc, mt_test))
# print("Ovv rate for finnish: ", ovv_rate(fi_voc, fi_test))


# """after increasing the vocabulary by 1000 words"""
# print("Ovv rate for greek: ", ovv_rate(el_voc, el_test))
# print("Ovv rate for bulgarian: ", ovv_rate(bg_voc, bg_test))
# print("Ovv rate for german: ", ovv_rate(de_voc, de_test))
# print("Ovv rate for french: ", ovv_rate(fr_voc, fr_test))
# print("Ovv rate for malteese: ", ovv_rate(mt_voc, mt_test))
# print("Ovv rate for finnish: ", ovv_rate(fi_voc, fi_test))

# ovv = array([x for x in range(int(ovv_rate(el_voc, el_test)))])
# ovv2 = array([x for x in range(int(ovv_rate(bg_voc, bg_test)))])
ovvdict =  { i : 5 for i in range(1,15000) }
for i in ovvdict.keys():
    ovvdict[i] = ovv_rate(vocabulary(el_train, i), el_test)
plt.loglog(ovvdict.keys(), ovvdict.values(), 'b', label='greek')
# plt.loglog(vocab, ovv2, 'r', label='bulgarian')
plt.legend(loc='best')
plt.show()
mng = plt.get_current_fig_manager()
mng.window.showMaximized()
mng.window.showMinimized()