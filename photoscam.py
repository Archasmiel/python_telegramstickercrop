import glob

from PIL import Image


def crop_multisticker(image: Image, size_x: int, size_y: int) -> Image:
    center_x, center_y = image.size[0] / 2, image.size[1] / 2
    left_x,   left_y = int(center_x - size_x / 2), int(center_y - size_y / 2)
    right_x,  right_y = int(center_x + size_x / 2), int(center_y + size_y / 2)
    image = image.crop((left_x, left_y, right_x, right_y))
    count = 0
    for n in range(5):
        for m in range(5):
            temp = image.crop((m*512, n*512, (m+1)*512, (n+1)*512))
            temp.save(rf'multi\{count}.png')
            count += 1
    return image


def crop_sticker(image: Image, size: int) -> Image:
    center_x, center_y = image.size[0]/2, image.size[1]/2
    left_x,   left_y = int(center_x - size/2), int(center_y - size/2)
    right_x,  right_y = int(center_x + size/2), int(center_y + size/2)
    return image.crop((left_x, left_y, right_x, right_y))


def resize_image(image: Image, size: int, multi_resize: bool) -> Image:
    if not multi_resize:
        image = image.resize((size, int(size / image.size[0] * image.size[1])))
        return image

    if image.size[0] >= image.size[1]:
        image = image.resize((int(size / image.size[1] * image.size[0]), size))
    if image.size[0] <= image.size[1]:
        image = image.resize((size, int(size / image.size[0] * image.size[1])))

    return image


extensions = ['*.png', '*.jpg']
path1 = rf'I:\PC files\Системные папки\Workspace\скамбот'
path2 = rf'photos'

files = []
counter = 0
for i in extensions:
    for j in glob.glob(rf'{path1}\{i}'):
        img = Image.open(j)
        img = resize_image(img, 512*5, True)
        img = crop_multisticker(img, 512*5, 512*5)
        # img = crop_sticker(img, 512)
        print(img.size)
        # img.save(rf'{path2}\{counter}.png')
        # counter += 1


