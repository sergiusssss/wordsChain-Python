import sys
import copy
sys.setrecursionlimit(6000)

words = []

with open("ff.txt") as f:
    for string in f:
        words.append(string.replace("\n", ""))

words = list(set(words))


def serach(words_list, in_list, end_word, counter):
    if len(in_list) == 0:
        return
    counter += 1
    print(counter)
    all_words_in_new_list = []
    temp_in_list = []

    for list_in_in_list in in_list:

        for word_in_words_list in words_list:

            distance_Hamming = 0
            for i in range(len(word_in_words_list)):
                if not list_in_in_list[-1][i] == word_in_words_list[i] and distance_Hamming <= 1:
                    distance_Hamming += 1

            if distance_Hamming == 1:
                if (word_in_words_list is end_word) or (word_in_words_list == end_word):
                    print("q")
                    temp_list = copy.copy(list_in_in_list)
                    temp_list.append(word_in_words_list)
                    with open("123.txt", 'a') as f:
                        str = ""
                        for word in temp_list:
                            str += word + " <- "

                        str = str[:-3]
                        str += "\n"
                        try:
                            f.write(str)
                        except:
                            pass
                else:
                    temp_list = copy.copy(list_in_in_list)
                    temp_list.append(word_in_words_list)
                    temp_in_list.append(temp_list)
                    if not word_in_words_list in all_words_in_new_list:
                        all_words_in_new_list.append(word_in_words_list)
    print(temp_in_list)

    for word_in_all_words in all_words_in_new_list:
        try:
            words_list.remove(word_in_all_words)
        except:
            print("=(")

    serach(words_list, temp_in_list, end_word, counter)

if __name__ == "__main__":
    serach(words, [["муха"]], "слон ", 0)