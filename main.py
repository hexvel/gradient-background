from PIL import Image

from test import GradientBackgroundLayer

if __name__ == "__main__":
    background_image = Image.new("RGB", (800, 600), (255, 255, 255))
    layer = GradientBackgroundLayer()
    gradient_image = layer.pipe(
        background_image, from_color=(255, 0, 0), to_color="blue", direction="rt-lb"
    )
    gradient_image.show()
