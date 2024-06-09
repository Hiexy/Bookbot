from typing import Dict, List

booksDir = "books/"

def main():
    frankensteinBookReport = generateReport("frankenstein")
    print(frankensteinBookReport)

def readFile(book: str) -> str:
    bookFile = f"{book}.txt"
    with open(f"{booksDir}{bookFile}") as f:
        bookContent = f.read()
    return bookContent

def countWords(bookContent: str) -> int:
    words = bookContent.split()
    return len(words)

def countChars(bookContent: str) -> List[Dict[str, int]]:
    charCountList = []
    charCount = dict()
    for char in bookContent:
        lowerChar = char.lower()
        if lowerChar not in charCount.keys():
            charCount[lowerChar] = 1
        else:
            charCount[lowerChar] += 1

    for char in charCount:
        charCountFrequency = {"char": char, "frequency": charCount[char]}
        charCountList.append(charCountFrequency)

    charCountList.sort(reverse=True, key=sort_on)
    return charCountList

def sort_on(dict: Dict[str, int]) -> int:
    return dict["frequency"]

def generateReport(book: str) -> str:
    bookContent = readFile(book)
    bookWordCount = countWords(bookContent)
    bookCharCount = countChars(bookContent)

    report = ""
    reportHeader = f"--- Begin report of {booksDir}{book}.txt ---\n"
    report += reportHeader

    reportWordCount = f"{bookWordCount} words found in the document\n"
    report += reportWordCount

    for charCount in bookCharCount:
        char = charCount["char"]
        charFrequency = charCount["frequency"]
        reportCharCount = f"The '{char}' was found {charFrequency} times\n"
        report += reportCharCount

    reportFooter = "--- End report ---"
    report += reportFooter

    return report

main()
