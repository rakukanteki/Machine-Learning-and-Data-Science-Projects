## Collecting Images:
1. Manually download images.
2. Use python and web scraping.
3. Fatkun Chrome Tool. [ Chrome Extension ]
4. Buy data from third-party vendors.

## Scraping:
-> Instead of doing things manually we can automate that manual task by SELENIUM and RPO
   ( Robotic Process Automation ).

# Data(Image) Cleaning:
- Detect the face of the person.
- Detect the face that has both eyes. If both eyes aren't found, then you can discard it.
- For face detection and detecting the eyes, we will use OpenCV.
- For specific detection, use a technique called HAAR cascade.
- May need to verify images with multiple persons in them manually.

# Summary:
- Raw Images --> Crop faces with two eyes using haar cascade --> Manual Data Cleaning -->
  Wavelet transformed images --> Train model --> Hypertune the model --> Save the model.

## What is Wavelet transform?
- Extracts the features of an image. Wavelet transforms are widely used in pattern recognition    and signal processing.
  
## Concept of frequency of an image:
- An image is nothing more than a bunch of pixels. The value of each pixel for a grayscale        image is 0 - 255. For simplicity, the image is taken in black and white. Here, black       
  represents 0, and white represents 1.
  Hence, if we see the values pixel by pixel we get a periodic value.

