from PIL import Image, ImageDraw, ImageFilter

haha = Image.open('zene/data/image/haha.jpg')
blurImage = haha.filter(ImageFilter.BoxBlur(15))
blurImage.save('zene/data/image/simBlurImage.jpg')