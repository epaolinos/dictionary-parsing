import io

dict_f = io.open("efremova.txt", mode="r", encoding="utf-8")
file_str = dict_f.read()
dict_f.close()

dict_list = file_str.split("\n\n")
new_f = io.open("word_list.txt", mode="w", encoding="utf-8")
for x in dict_list:
    word = x.split("\n")[0]
    if word.isalpha() and 3 < len(word) < 13:
        new_f.write(word + "\n")
