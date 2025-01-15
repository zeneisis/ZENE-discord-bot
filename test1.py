import ebooklib
from ebooklib import epub

book = epub.read_epub('C:\Users\takah\Downloads\Konosuba.epub')

for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
    print(image)