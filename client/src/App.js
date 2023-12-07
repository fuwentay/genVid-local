import React, { useState } from 'react';
import TextBox from "./components/textbox/Textbox";
import Video from "./components/videos/Video";

function App() {
  const [videoSource, setVideoSource] = useState('');
  const [videoGenerationKey, setVideoGenerationKey] = useState(0);
  const [isLoading, setIsLoading] = useState(false);  // Introduced this state

  const handleVideoUrlReceived = (url) => {
    console.log('Video URL received:', url);
    setVideoSource(url);
    setVideoGenerationKey(prevKey => prevKey + 1);
    setIsLoading(false);  // Set isLoading to false once video is ready
  };

  return (
    <div className="App">
      <TextBox 
        onVideoUrlReceived={handleVideoUrlReceived} 
        setIsLoading={setIsLoading}  // Passing setIsLoading as a prop
      />
      {isLoading ? <div>Loading...</div> : (videoSource && <Video videoSource={videoSource} key={videoGenerationKey} />)}
    </div>
  );
}

export default App