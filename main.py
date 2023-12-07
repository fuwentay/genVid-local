from storyline import get_storyline, get_sentences, get_reduced_sentence
from image import get_image, decode_json
from speech import text_to_speech, text_to_speech_overall, get_all_mp3_duration
from video import images_to_video, compile_video_audio
from utils import clean_dir, move_files, random_wait, long_wait, upload_to_s3
from instagram import post_video, get_latest_post_id, get_comment, get_username

# question = "what would happen if a needle hits the surface of the earth at the speed of light? could you give me a detailed explanation using physics as well as a description of the series of events?"
# question = "Are Reptilian Shape-Shifters Among Us? Could you come up with a conspiracy theory? For example, many people think Mark Zuckerberg is a reptile."
# question = "What would happen if the sun starts to disintegrate in our solar system? Could you describe the series of events as well as the physics behind it? Not more than 3 sentences."
# question = "What happened to the lost city of Atlantis? Can you come up with a short story that is not more than 5 sentences?"

# No unallowed symbols like / ? etc.
instruction = "Please write a paragraph (less than 5 sentences) on the following:"
# TODO: it will break if the comment includes above characters.
question = get_comment(get_latest_post_id())
prompt = instruction + question

# To generate a script for the video.
storyline = get_storyline(prompt)

# Extract the sentences in the script. Each sentence will use 1 video.
sentences_lst = get_sentences(storyline)

for sentence in sentences_lst:
    # Generates file saved as json
    get_image(sentence)

    # Generates mp3 files for the sentence.
    text_to_speech(sentence)

# Decode all json to png
decode_json()

# Stitch images together based on mp3 duration
images_to_video(get_all_mp3_duration(sentences_lst), sentences_lst)

# Generates storyline string. Unable to use storyline from above because it may contain "\n" strings which will result in OSError.
storyline = ""
for sentence in sentences_lst:
    storyline += sentence + ". "

# Generates mp3 file for the whole storyline. 
# FIXME: might have too stitch the individual audios together to get the right timing    
text_to_speech_overall(storyline)

print("Compiling video")

# Add the MP3 to MP4 file.
compile_video_audio(sentences_lst)

print("Video compiled")

upload_to_s3(question)

# Move files and folders to projects folder.
move_files(question, storyline)

# Delay post to try avoid bot detection algo
# random_wait()

# Posts video from the projects folder onto Instagram.
post_video(question)