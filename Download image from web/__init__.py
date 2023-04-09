import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://media.licdn.com/dms/image/C5603AQEdFhO7cIS-UQ/profile-displayphoto-shrink_400_400/0/1560820178018?e=1686182400&v=beta&t=lKMJAURuX0sAeNG6a_JE2JxAMxNvY2Jnm9JbSBejXt0")

