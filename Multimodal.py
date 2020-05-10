#language 1: Spanish
pos_1 = "positive_words_es.txt"
neg_1 = "negative_words_es.txt"
trans_pos_1 = "trans_positive_words_es.txt"
trans_neg_1 = "trans_negative_words_es.txt"

#language 2: German
pos_2 = "positive_words_de.txt"
neg_2 = "negative_words_de.txt"
trans_pos_2 = "trans_positive_words_de.txt"
trans_neg_2 = "trans_negative_words_de.txt"

#create language 1 word array
trans_pos_1_file = open(trans_pos_1, "r", encoding='utf-8-sig')
pos_1_words = set()
for line in trans_pos_1_file:
    word = line.lower()[:-1]
    pos_1_words.add(word)
trans_pos_1_file.close()

trans_neg_1_file = open(trans_neg_1, "r", encoding='utf-8-sig')
neg_1_words = set()
for line in trans_neg_1_file:
    word = line.lower()[:-1]
    neg_1_words.add(word)
trans_neg_1_file.close()


#create language 2 word array
trans_pos_2_file = open(trans_pos_2, "r", encoding='utf-8-sig')
pos_2_words = set()
for line in trans_pos_2_file:
    word = line.lower()[:-1]
    pos_2_words.add(word)
trans_pos_2_file.close()

trans_neg_2_file = open(trans_neg_2, "r", encoding='utf-8-sig')
neg_2_words = set()
for line in trans_neg_2_file:
    word = line.lower()[:-1]
    neg_2_words.add(word)
trans_neg_2_file.close()


#find both positives
both_positives = set()

for word1 in pos_1_words:
    for word2 in pos_2_words:
        if word1 == word2:
            if word1 not in both_positives:
                both_positives.add(word1)

#find both negatives
both_negatives = set()

for word1 in neg_1_words:
    for word2 in neg_2_words:
        if word1 == word2:
            if word1 not in both_negatives:
                both_negatives.add(word1)

#find only positives in language 1
only_pos_in_1 = pos_1_words - both_positives

#find only positives in language 2
only_pos_in_2 = pos_2_words - both_positives

#find only negatives in language 1
only_neg_in_1 = neg_1_words - both_negatives

#find only negatives in language 2
only_neg_in_2 = neg_2_words - both_negatives

print("Words positive in both languages: ")
print(both_positives)
print()

print("Words negative in both languages: ")
print(both_negatives)
print()

print("Words only positive in Spanish: ")
print(only_pos_in_1)
print()

print("Words only positive in German: ")
print(only_pos_in_2)
print()

print("Words only negative in Spanish: ")
print(only_neg_in_1)
print()

print("Words only negative in German: ")
print(only_neg_in_2)
print()