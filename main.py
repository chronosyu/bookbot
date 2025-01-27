def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    wordcount = word_count(file_contents)
    #print(file_contents)
    count = count_chars(file_contents)
    #print(count)

    sorted_dict= list_and_sort(count)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document")
    print("")

    for i in range(0, len(sorted_dict)):
        if sorted_dict[i]["char"].isalpha():
            print(f"The '{sorted_dict[i]["char"]}' character was found {sorted_dict[i]["count"]} times")
    print("--- End report ---")

def word_count(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char={}
    text = text.lower()
    for t in text:
        if t in char:
            char[t] += 1
        else:
            char[t] = 1
    return char

def list_and_sort(dict):
    dict_l=[]
    for d in dict:
        dict_l.append({"char": d, "count": dict[d]})
    
    dict_l.sort(reverse=True, key=sorting)
    
    return dict_l

def sorting(dict):
    return dict["count"]

main()