import React, { useState, useEffect } from 'react';

const Video = ({ videoSource }) => {
  const [refreshedVideoSource, setRefreshedVideoSource] = useState(videoSource);

  useEffect(() => {
    console.log('videoSource:', videoSource);

    const intervalId = setInterval(() => {
      console.log('Refreshing video source...');
      setRefreshedVideoSource(videoSource);
    }, 5000);

    // Clean up the interval when the component unmounts
    return () => {
      clearInterval(intervalId);
      console.log('Interval cleared.');
    };
  }, [videoSource]);

  console.log('refreshedVideoSource:', refreshedVideoSource);

  return (
    <div className="video-container">
      <video controls key={refreshedVideoSource}>
        <source src={`${refreshedVideoSource}?t=${Date.now()}`} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default Video;
