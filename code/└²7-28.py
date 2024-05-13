import os
import os.path
import pptx   # pip install python-pptx

total = 0
def pptCount(path):
    global total
    for subPath in os.listdir(path):
        subPath = os.path.join(path, subPath)
        if os.path.isdir(subPath):
            pptCount(subPath)
        elif subPath.endswith('.pptx'):
            print(subPath)
            try:
                presentation = pptx.Presentation(subPath)
                total += len(presentation.slides)
            except:
                pass
            
pptCount(r'D:\教学课件')
print(total)
