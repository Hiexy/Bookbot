booksDir = "books/"

def main():
    frankensteinContent = readFile("frankenstein")
    frankensteinWordCount = countWords(frankensteinContent)
    print(frankensteinWordCount)

def readFile(book: str) -> str:
    bookFile = f"{book}.txt"
    with open(f"{booksDir}{bookFile}") as f:
        bookContent = f.read()
    return bookContent

def countWords(bookContent: str) -> int:
    words = bookContent.split()
    return len(words)

main()
