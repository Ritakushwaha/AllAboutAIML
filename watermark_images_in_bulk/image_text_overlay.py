import cv2 
import os 

# add text to center of the image
def add_text_to_center(image, text):
    #get dimension of the image
    height, width, _ = image.shape # height of the image, width of the image and number of channels in the image at different indices

    #calculate center coordinates
    center_x = width // 2
    center_y = height // 2

    #choose font scale and thickness for the text
    font_scale = 2
    thickness = 2

    #get the size of the text
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]

    #calculate the coordinates to put the text at the center
    text_x = center_x - (text_size[0] // 2)
    text_y = center_y - (text_size[1] // 2)

    #add the text to image
    cv2.putText(image, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), thickness)

    return image


if __name__ == "__main__":

    #input and output folder paths
    input_folder = './mini_programs/input_images'
    output_folder = './mini_programs/output_images'

    #create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):

            #read image
            input_image_path = os.path.join(input_folder, filename)
            image = cv2.imread(input_image_path)
            text = '@enliven_arts'

            #add text to the center of the image
            image_with_text = add_text_to_center(image,text)

            #save the image with text in the output_images folder
            output_images_path = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}_ea.jpg')
            cv2.imwrite(output_images_path, image_with_text)

            print(f"Image saved successfully to: {output_images_path}")