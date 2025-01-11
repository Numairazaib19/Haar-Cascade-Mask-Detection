# Haar Cascade Mask Detection for Faces

This project uses Haar Cascade Classifiers to detect faces wearing masks. It involves collecting and processing both positive and negative images, training a classifier, and validating it using various datasets. This README will guide you through the steps to run the project.

## Overview

This project consists of multiple steps:
1. **Collecting Images**: Gathering positive and negative images.
2. **Describing Images**: Using the `Objectmarker` utility to define object locations in positive images.
3. **Creating a Vector Training Set**: Generating the vector file to be used in the training process.
4. **Training the Classifier**: Training the Haar Cascade classifier with the images.
5. **Generating the XML Classifier**: Converting the trained data into an XML file.
6. **Testing**: Running the XML classifier on images and videos to validate its performance.

## Prerequisites

To run this project, you will need to:
- Python 3.x installed on your system.
- OpenCV library for running Haar Cascade operations.

## Setup and Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Numairazaib19/Haar-Cascade-Mask-Detection.git
   cd Haar-Cascade-Mask-Detection
   ```

2. **Data**

   The repository **does not contain the data** due to the large size of the images and the need for data privacy. You will need to **load your own data** before using this project. The steps below will guide you on how to prepare the data:
   
   - **Positive Images**: Faces with masks saved as `.bmp`.
   - **Negative Images**: Backgrounds without faces or masks saved as `.jpg`.

   Make sure to follow the below steps for gathering data:
   - **Extract frames from videos** and save them in `.bmp` format.
   - **Use internet datasets** or other sources to collect additional positive images.
   - **For negative images**, use general background images that do not contain faces or masks.

3. **Preparing the Data**

   - **Create a list of negative images**:
     Run the `create_list.bat` to create a list of negative images, which will be saved in the `infonegative.txt` file.

   - **Mark objects in positive images**:
     Use `objectmarker.exe` to define the object locations (masks) in the positive images. A file named `positive/info.txt` will be generated once completed.

4. **Creating the Vector Training Set**

   - Edit `creation.bat` to set the number of positive images and adjust image size parameters (`-w` and `-h`).
   - Run `samples_creation.bat` to generate the vector file.

5. **Training the Classifier**

   - Edit `haartraining.bat`:
     - Set the `-vec` parameter to the path of your generated vector file.
     - Set the number of positive (`-npos`) and negative (`-nneg`) images.
     - Adjust `-nstages` for the number of stages.
     - Set the `-mem` parameter based on your available RAM (e.g., 512 or 1024).
     - Set the width (`-w`) and height (`-h`) to match those used in `samples_creation.bat`.
   - Delete any files inside the `cascade` folder.
   - Run `haartraining.bat` to start the training process.

6. **Generating the XML File**

   - Edit `convert.bat`:
     - Set the width and height to match the values used in the training process.
     - Change the name of the output XML file.
   - Run `convert.bat` to generate the final XML file for your trained classifier.

7. **Running the Classifier**

   - Test the XML file on images and videos using Python to validate the performance of the classifier.
   - Run the provided Python scripts to test and validate your trained classifier.

## Conclusion

This project demonstrates how to create a Haar Cascade classifier for mask detection, covering data collection, training, and testing phases. It is a useful example for anyone looking to build object detection classifiers using Haar Cascades in Python.
