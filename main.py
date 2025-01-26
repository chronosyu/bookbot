def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(word_count(file_contents))
    #print(file_contents)

def word_count(text):
    words = text.split()
    return len(words)

main()