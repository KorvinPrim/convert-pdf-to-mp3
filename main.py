from art import *
from gtts import gTTS
from pathlib import Path
import pdfplumber

def pdf_to_mp3(file_path='In_a _beautiful_ancient_city.pdf', language = 'en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'[+] File name: {Path(file_path).name}')
        print('[+] Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ' '.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text = text, lang=language)
        name_file = Path(file_path).stem
        my_audio.save(f'{name_file}.mp3')
        return f'[+] {name_file}.mp3 saved successfully!\n---Have a good day!---'
    else:
        return "File no exists, check the file path!"

def main():
    tprint('PDF>>>TO>>>MP3', font='buldhead')
    file_path = input('\nEnter path to file: ')
    language = input('Choose language: en or ru: ')
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()