import cv2
import os
from moviepy.editor import VideoFileClip, AudioFileClip

# Stitching images to a video.
def images_to_video(frame_durations, sentences_lst):
    image_folder = "/tmp/images"
    output_video = "/tmp/output.mp4"

    images = []
    for sentence in sentences_lst:
        images.append(sentence[:10] + ".png")

    # Load the first image to get its dimensions and fps
    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = first_image.shape

    fps = 60

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # You can change the codec as needed
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for image, duration in zip(images, frame_durations):
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)

        # Calculate the number of frames based on the duration
        num_frames = int(duration * fps)

        for _ in range(num_frames):
            video.write(frame)

    cv2.destroyAllWindows()
    video.release()

# frame_durations = [1, 1, 1]  # Durations for each image in seconds
# images_to_video(frame_durations)

def compile_video_audio(sentences_lst):
    video_clip = VideoFileClip('/tmp/output.mp4')
    final_audio = "/tmp/" + sentences_lst[0][:10] + ".mp3"
    audio_clip = AudioFileClip(final_audio)

    # Make sure the audio duration matches the video duration
    if audio_clip.duration > video_clip.duration:
        audio_clip = audio_clip.subclip(0, video_clip.duration)

    # Set the video clip's audio to the loaded audio clip
    video_clip = video_clip.set_audio(audio_clip)

    # Write the final video with audio to the output file
    # Change path of temp audio file
    video_clip.write_videofile("/tmp/video.mp4", codec="libx264", temp_audiofile='/tmp/temp-audio.m4a', remove_temp=True, audio_codec="aac")

# compile_video_audio(["The sun wialdnawdlnd", "The energy aodbaobdawdw"])