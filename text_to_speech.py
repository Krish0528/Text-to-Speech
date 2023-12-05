# Import the gTTS module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
from playsound import playsound

import PyPDF2

input_pdf = input("Enter the pdf file name with .pdf extension: ")

file = open(input_pdf, 'rb')
pdf_reader = PyPDF2.PdfReader(file)
num_pages = len(pdf_reader.pages)

for num in range(0, num_pages):
    page = pdf_reader.pages[num]
    data = page.extract_text()

    # It is a text value that we want to convert to audio
    text_val = data

    # Here are converting in English Language
    language = 'en'
    # Passing the text and language to the engine,
    # here we have assign slow=False. Which denotes
    # the module that the transformed audio should
    # have a high speed
    obj = gTTS(text=text_val, lang=language, slow=False)

    # Here we are saving the transformed audio in a mp3 file named
    obj.save(f"page{num}.mp3")

    print('Audio content written to file "output.mp3"')

    # Play the exam.mp3 file
    playsound(f"page{num}.mp3")
