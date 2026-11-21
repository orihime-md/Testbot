from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 800, 500


def _font(size):
    try:
        return ImageFont.load_default(size=size)  # Pillow 10.1 and newer
    except TypeError:
        return ImageFont.load_default()


def make_congrats_image():
    """Returns a PNG image (in memory) that says the bot is active."""
    img = Image.new("RGB", (WIDTH, HEIGHT), (20, 24, 45))
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        shade = int(20 + 50 * y / HEIGHT)
        draw.line([(0, y), (WIDTH, y)], fill=(shade, 24, 45 + shade))
    draw.text((WIDTH // 2, 190), "CONGRATS!", font=_font(72), fill=(255, 200, 60), anchor="mm")
    draw.text((WIDTH // 2, 300), "Your bot is active", font=_font(40), fill=(255, 255, 255), anchor="mm")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer
