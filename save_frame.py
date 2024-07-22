

def save_images(frame, step, output_folder='videos'):

    """
    Save frames as images
    :param frame: Frame to save (Numpy array)
    :param step: Frame number (Used as the image name)
    :param output_folder: Folder to save the images (default: 'videos')
    """

    os.makedirs(output_folder, exist_ok=True) # Creating the folder if it does not exist
    im = Image.fromarray(frame) # Converting the frame to an image
    im.save(f'{output_folder}/{step}.png') # Saving the image

def save_video(input_folder, output_file, fps=30):

    """ 
    Create a video from a series of images in a folder 
    :param input_folder: Folder containing the images
    :param output_file: Output file name
    :param fps: Frames per second
    """

    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')] # Getting the image files .png only
    image_files.sort(key=lambda x: int(x.split('.')[0]))  # Sort by number

    frame = cv2.imread(os.path.join(input_folder, image_files[0])) # Reading the first image
    height, width, layers = frame.shape # Getting the shape of the frame

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Codec
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height)) # Creating the video

    for image in image_files: # Looping through the images
        image_path = os.path.join(input_folder, image) # Getting the image path
        frame = cv2.imread(image_path)
        out.write(frame)

    out.release() # Releasing the videowriter
    cv2.destroyAllWindows() # Destroying all windows

    print(f'Video saved to {output_file}')