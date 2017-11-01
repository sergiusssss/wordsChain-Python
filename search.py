import  sys
words = []

sys.setrecursionlimit(6000)

with open("words_four_one(5918).txt") as f:
    for string in f:
        words.append(string.replace("\n", ""))

words = list(set(words))


def search(words_list, chain, word, stop_word):
    new_list = {}

    for ww in word:
        new_list[ww] = []
        try:
            words_list.remove(ww)
        except:
            pass
        for w in words_list:
            distance_Hamming = 0
            for i in range(len(w)):
                if not ww[i] == w[i] and distance_Hamming <= 1:
                    distance_Hamming += 1
            if distance_Hamming == 1:
                if w == stop_word:
                    new_chain = chain
                    new_chain.append(ww)
                    new_chain.append(w)
                    print("@@@@@")
                    print(ww)
                    print(w)
                    print(stop_word)
                    print(new_chain)
                else:
                    new_list[ww].append(w)

    for key, value in new_list.items():
        new_chain = chain
        new_chain.append(key)
        search(words_list, new_chain, value, stop_word)






# def search(words_list,chain, word, stop_word):
#     chain.append(word)
#     words_list.remove(word)
#     for w in words_list:
#         distance_Hamming = 0
#         for i in range(len(w)):
#             if not word[i] == w[i] and distance_Hamming <= 1:
#                 distance_Hamming += 1
#         if distance_Hamming == 1:
#             new_word = w
#             if new_word == stop_word:
#                 chain.append(new_word)
#                 with open("www.txt", 'a') as f:
#                     str = ""
#                     for word_in_f in chain:
#                         str += word_in_f + "->"
#                     final_str = str[:-2]
#                     f.write(final_str + "\n")
#                     print(chain)
#             else:
#                 search(words_list,chain, new_word, stop_word)
#     return False

search(words, [], ["мура"], "слон")

