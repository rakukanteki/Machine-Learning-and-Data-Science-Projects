## Collecting Images:
1. Manually download images.
2. Use python and web scraping.
3. Fatkun Chrome Tool. [ Chrome Extension ]
4. Buy data from third party vendor.

## Scraping:
-> Instead of doing things manually we can automate that manual task by SELENIUM and RPO
   ( Robotic Process Automation ).

# Data(Image) Cleaning:
- Detect the face of the person.
- Detect the face that has both eyes. If both eyes aren't found, then you can just discard it.
- For face detection and detecting the eyes, we will use OpenCV.
- For specific detection, use a technique called HAAR cascade.
- May need to do manual verification for images that have multiple persons in them.

# Summary:
- Raw Images --> Crop faces with two eyes using haar cascade --> Manual Data Cleaning -->
  Wavelet transformed images --> Train model --> Hyper tune the model --> Save the model.
  
