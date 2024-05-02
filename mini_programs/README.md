# Image Text Overlay

## Objective
The objective of this mini project is to create a Python script that adds a specified text to the center of an image and saves the modified image. This can be useful for tasks such as watermarking images with logos or adding annotations.

## Packages Needed
This project requires the following Python packages:
- OpenCV (cv2): For image processing and manipulation.
    ```
    pip3 install opencv-python
    ```
- os: For file and directory operations.

## How to Run the Code
1. Install the required packages using pip3:
```
pip3 install opencv-python
```

2. Clone or download this repository to your local machine.

3. Navigate to the directory containing the Python script (`image_text_overlay.py`).

4. Make sure you have an input image inside `input_images` folder in the same directory as the script. You can replace this image with your own image if desired.

5. Run the Python script using the following command:
```
python3 image_text_overlay.py
```

6. The modified image with the added text will be saved in the `output_images` folder within the same directory. The filename of the output image will be `<image_name>_ea.jpg`.

7. You can view the saved image with the added text in the `output_images` folder.

## Additional Notes
- You can modify the text to be added and the input image filename/path directly in the Python script if needed.
- Ensure that the input image is in a common image format supported by OpenCV (e.g., JPEG, PNG).
- The font scale and thickness of the added text can be adjusted as per your preference in the `add_text_to_center` function.

