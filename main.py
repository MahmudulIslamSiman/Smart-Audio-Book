import pyttsx3
import PyPDF2
book = open('DSA.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
Proton = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    Proton.say(text)
    Proton.runAndWait()