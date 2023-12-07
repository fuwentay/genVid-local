# genVid - Generation of Videos through AI

## Updates 7 Dec 23
- I started working on this after my summer internship before I went back to uni. Initially, I was planning to keep this repo private as I thought it could become some sort of a side-hustle. However, my instagram account was banned so I decided to make this public.
- The webapp is not deployed but works on localhost. I would elaborate on this further below.
- It is currently abandoned as I have other projects I would like to work on.

## Issues
The webapp is hosted on Heroku but is not fully functional as the API timeouts due to its long processing time (generation of video). The plan was to use Celery and Redis to offload the task as a background task but school was starting and I didn't have enough time to look into it. Regardless, the webapp is fully functional locally.

## Motivation
Ever since the surge in popularity of GenAI, I noticed more social media content that is homogeneous, following a very standard format that is easy to generate. As such, I wanted to figure out how difficult is it to deploy your own "shit-posting" bot on Instagram that generates content systematically through the technologies we have available today.

## Overview
### Building of Instagram Bot
1. Fetch previous post's comment from post metadata on MongoDB (from step 8)
2. Question Generation
3. Storyline Generation
4. Image Generation -> Video Generation
5. TTS
6. Add TTS to Video 
7. Upload Video to Instagram
8. Upload post metadata to MongoDB

### Building of Web App
1. Set up AWS S3 Bucket (set to public)
2. Build Components:
    - Video player
    - Text input box
3. Write API Endpoints

### Containerisation
Build container `docker build . -t main.py`  
Run container `docker run main.py`  
Obtain container ID `docker ps`  
Enter bash to communicate with contents of container `docker exec -it <containerID>`  
Update scripts in container `docker cp .env <containerID>:/app/`

### Deployment
Install aws cli `sudo apt-get install awscli`  
Config aws keys `aws configure`  
Creating Docker image in ECR (Elastic Container Registry): Follow browser commands  
Creating Lambda function: Select image from ECR  
Add a Trigger: EventBridge trigger to invoke Lambda function daily

### Database
MongoDB was chosen due to it's ease of deployment and noSQL nature.  

## Difficulties
- Configuring the scripts to be compatible with AWS Lambda: Due to the nature of Lambda, only files in /tmp are writable, so there was a need to change the location that intermediate files are saved to. In addition, tmp files created by the .write_videofile method was raising `OSError: [Errno 32] Broken pipe` because it was being written to /app instead of /tmp. Unfamiliar with this error, I thought I had to modify the Moviepy library, and copy it into my Docker container. Fortunately, there is an optional argument `temp_audiofile` that allowed me to save the location of the tmp file.
- Configuring the S3 bucket to make objects within it public.
- From localhost to live server: First time deploying a full stack web app (Frontend on Github pages and Backend on Heroku). 
- #TODO: Hitting timeout on Heroku. Have to run API as a background process. (Celery)

## Learning Points
When building an app, it is important to work on a virtual environment. It would reduce the chance of having conflicting packages from different projects due to their versions.  

## Costs
1. Currently using OpenAI's free trial credits, but it costs about SGD $0.10 to generate the content for 1 post at the lowest resolution possible.
2. Currently using the AWS free trial. Would incur a cost for Lambda and ECR in the future.

## Precautions
Instagram has a suite of bot-detection algorithms. So it is important to implement delays between Instagrapi API requests. I have also added some variance in the uploading times.

## Future Work
In the future, videos would then be stored on an AWS S3 bucket, and displayed on a webapp as a library of user-generated videos.

## Output
