import os

from PIL import ImageDraw, ImageFont


def draw(predictions, image):
    draw_image = ImageDraw.Draw(image, "RGBA")

    image_width, image_height = image.size

    font = ImageFont.truetype("adapters/arial.ttf", 12)
    i = 0
    for prediction in predictions:
        box = prediction.box
        draw_image.rectangle(
            [(box.xmin * image_width, box.ymin * image_height),
             (box.xmax * image_width, box.ymax * image_height)],
            outline='red')
        class_name = prediction.class_name
        draw_image.text(
            (box.xmin * image_width, box.ymin * image_height - font.getsize(class_name)[1]),
            class_name, font=font, fill='red')
        i += 1
    try:
        os.mkdir('tmp/debug')
    except OSError as error:
        pass
    image.save("tmp/debug/output.jpg", "JPEG")
