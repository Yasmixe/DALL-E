import os
import openai
secret = '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'
openai.api_key = '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'
openai.Model.list()

description = input("enter your discription here please : \n")
number = input("enter your number of images\n")
sizee = input("choose what size suits you the most : 1024x1024, 512x512, 256x256\n")
print("painting in process...\n")
response = openai.Image.create(
    prompt = description,
    n = int(number),
    size = sizee
)

image_url = response['data'][0]['url']

print("Your painting is ready !here's the url, check this out  -->   ",image_url)