
words = []


with open("litf-win.txt") as f:
    for line in f:
        word = line.split()[0]

        if(len(word)) == 4:
            words.append(word)

with open("pldf-win.txt") as f:
    for line in f:
        word = line.split()[0]

        if (len(word)) == 4:
            words.append(word)

words = list(set(words))

with open("ff.txt", 'a') as f:
    for w in words:
        f.write(w + "\n")

print(len(words))








# import re
#
# with open("lop1v2.txt") as f:
#     words = []
#     for line in f:
#         word = line.split("#")[0]
#         clearText = re.sub(u"[^а-яА-Я0-9.,\s]", "", word)
#         clearText = re.sub(u"[.,\-\s]{3,}", " ", clearText)
#         clearText = clearText.replace(" ", "")
#         big = True
#         for char in clearText:
#             if char.islower():
#                 big = False
#         if len(clearText) == 4:
#             if not big:
#                 words.append(clearText.lower())
#
#     words.sort()
#     print(words)
#     print(len(words))
#     with open("words_four_two(" + str(len(words)) + ").txt", 'w') as f_words:
#         for word_n in words:
#             f_words.write(word_n + "\n")
# #
# # with open("litw-win.txt") as f:
# #     all_file_string = f.read()
# #     all_file_words = all_file_string
# #     for var in range(10):
# #         all_file_words = all_file_words.replace(str(var), "")
# #
# #     all_file_words_list = all_file_words.split()
# #
# #     word_four = []
# #     for word in all_file_words_list:
# #         if len(word) == 4:
# #             word_four.append(word)
# #
# #     print(word_four)
# #     print(len(word_four))
# #
# #     word_four.sort()
# #
# #     with open("words_four_one(" + str(len(word_four)) + ").txt", 'w') as f_words:
# #         for word in word_four:
# #             f_words.write(word + "\n")
