# Use a base Python image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the source code into the container
COPY main.py utils.py storyline.py image.py speech.py video.py instagram.py .env project database.py ./

# Install any dependencies, such as instagrapi and dotenv
RUN pip install langchain yake opencv-python openai moviepy gTTS mutagen instagrapi python-dotenv pymongo boto3
#imageio-ffmpeg==0.2.0

# Install the cv2 dependencies that are normally present on the local machine, but might be missing in the Docker container
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# ffmpeg=3.4.13

# Define the entry point as a dummy command (When testing locally)
# ENTRYPOINT ["tail", "-f", "/dev/null"]

# Run main.py when invoked (When testing on Lambda)
CMD ["python", "main.py"]