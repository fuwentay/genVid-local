import React, { useState } from 'react';

function TextBox({ onVideoUrlReceived, setIsLoading }) {
  const [inputText, setInputText] = useState('');

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setIsLoading(true);  // Set isLoading to true at the beginning of video generation

    try {
      const response = await fetch('/generate-video-url', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ inputText }),
      });

      if (response.status === 200) {
        const data = await response.json();
        const videoSource = data.videoSource;
        console.log('Video URL received:', videoSource);

        // Make an additional request to the /text route
        const textResponse = await fetch(`/${inputText}`, {
          method: 'GET',
        });

        if (textResponse.status === 200) {
          console.log('Text submitted successfully');
          // Only after /text route completes, inform App component about the video URL
          onVideoUrlReceived(videoSource);
        } else {
          console.error('Failed to submit text');
        }
      } else {
        console.error('Failed to generate video URL');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter text..."
          value={inputText}
          onChange={handleInputChange}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default TextBox;
