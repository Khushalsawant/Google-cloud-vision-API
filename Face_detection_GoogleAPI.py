# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:28:22 2019

@author: KS5046082
"""
'''
from google.cloud import vision
print(dir(vision))
import os
print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
'''


from google.cloud import vision
from google.cloud.vision import enums
from google.cloud.vision import types

print(dir(enums))

uri_base = 'gs://cloud-vision-codelab'
pics = ['face_surprise.jpg', 'face_no_surprise.png']

client = vision.ImageAnnotatorClient()
image = types.Image()

for pic in pics:
    image.source.image_uri = '{}/{}'.format(uri_base, pic)
    response = client.face_detection(image=image)

    print('=' * 79)
    print('File: {}'.format(pic))
    for face in response.face_annotations:
        print("Confidence = ",face.detection_confidence)
        print("content = ",face)
        likelihood = enums.Likelihood(face.surprise_likelihood)
        vertices = (['({},{})'.format(v.x, v.y)
                     for v in face.bounding_poly.vertices])
        print('Face surprised: {}'.format(likelihood.name))
        print('Face bounds: {}'.format(','.join(vertices)))



# GOOGLE_APPLICATION_CREDENTIALS
# set the path of your API key file as env var.
'''
from google.cloud import vision
from google.cloud.vision import types

image_uri = 'gs://cloud-vision-codelab/otter_crossing.jpg'

client = vision.ImageAnnotatorClient()
image = types.Image()
image.source.image_uri = image_uri

response = client.text_detection(image=image)

for text in response.text_annotations:
    print('=' * 79)
    print('"{}"'.format(text.description))

    vertices = (['({},{})'.format(v.x, v.y)
                 for v in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))
'''