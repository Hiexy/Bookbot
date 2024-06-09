from typing import Dict

booksDir = "books/"

def main():
    frankensteinContent = readFile("frankenstein")
    frankensteinWordCount = countWords(frankensteinContent)
    frankensteinCharCount = countChars(frankensteinContent)
    print(frankensteinCharCount)

def readFile(book: str) -> str:
    bookFile = f"{book}.txt"
    with open(f"{booksDir}{bookFile}") as f:
        bookContent = f.read()
    return bookContent

def countWords(bookContent: str) -> int:
    words = bookContent.split()
    return len(words)

def countChars(bookContent: str) -> Dict[str, int]:
    charCount = dict()
    for char in bookContent:
        lowerChar = char.lower()
        if lowerChar not in charCount.keys():
            charCount[lowerChar] = 1
        else:
            charCount[lowerChar] += 1
    return charCount

main()
