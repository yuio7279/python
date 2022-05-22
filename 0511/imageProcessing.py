import numpy as np
import pytesseract
from pytesseract import Output
from PIL import Image
import numpy as np

def cleanFile(filePath, threshold):
    image = Image.open(filePath)
    # 임계점을 설정하고 저장
    image = image.point(lambda x: 0 if x < threshold else 255)
    return image

def getConfidence(image):
    data = pytesseract.image_to_data(image, output_type=Output.DICT)
    text = data['text']
    confidences = []
    numChars = []

    for i in range(len(text)):
        try:
            if int(data['conf'][i]) > -1:
                print('-1 처리')
        except:
            confidences.append(float(data['conf'][i]))
            numChars.append(len(text[i]))

    return np.average(confidences, weights=numChars), sum(numChars)
filePath = './0511/textBad.png'

start = 80
step = 5
end = 200

for threshold in range(start, end, step):
    image = cleanFile(filePath, threshold)
    scores = getConfidence(image)
    output = 'threshold: {}, confidence: {}, numChars{}'
    output = output.format(str(threshold),str(scores[0]),str(scores[1]))
    print(output)