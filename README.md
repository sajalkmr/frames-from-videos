# frames-from-videos

<html>

<body>
	<h1>Extract Video Frames with Subtitles using ffmpeg</h1>
	<p>This project provides a Python script to extract frames from video files and burn subtitles into the video using the ffmpeg library. The resulting frames are saved as .jpg files in a new subdirectory under the specified output folder.</p>
  <br>
  
  <h2>Sample Output</h2>
<p>Below is an example of output and a frame extracted with subtitles from a video file using this script:</p>
<figure>
  <img src="/screenshot.png" alt="Sample Output">
  <img src="/frame.png" alt="frame">
  
</figure>

  
  
  
  
<h2>How to Run</h2>
<p>To run this script, follow the steps below:</p>
<ol>
	<li>Install ffmpeg. Instructions can be found <a href="https://ffmpeg.org/download.html">here</a>.</li>
	<li>Download or clone this repository to your local machine.</li>
	<li>Open a terminal or command prompt and navigate to the root directory of the downloaded repository.</li>
	<li>Run the following command: <code>frames.py</code></li>
	<li>The extracted frames with subtitles will be saved in the "frames_output" folder.</li>
</ol>

<h2>How it works</h2>
<p>The Python script, <code>extract_frames_with_subtitles.py</code>, performs the following steps:</p>
<ol>
	<li>Defines the input and output folder paths. The input folder is set to the current working directory, and the output folder is set to a new subdirectory called "frames_output" under the current working directory.</li>
	<li>Creates the output folder if it does not already exist.</li>
	<li>Iterates over each file in the input folder that has a .mkv or .mp4 extension.</li>
	<li>Creates a new subdirectory under the output folder with the same name as the input video file (without the extension).</li>
	<li>Calls ffmpeg as a subprocess to extract frames from the video file, burn subtitles into the video using the specified font size, font name, and primary color, and save the resulting frames as .jpg files in the new subdirectory.</li>
	<li>The output frames are saved with a filename format of 3 digits, padded with leading zeros, starting from 001, and increasing by 1 for each subsequent frame. The frame rate is set to 0.3 frames per second, and the video quality is set to a constant rate factor (CRF) of 23. The video quality is set to a value of 1 to preserve the original quality.</li>
</ol>

<h2>Dependencies</h2>
<p>The script depends on the following:</p>
<ul>
	<li>Python 3</li>
	<li>ffmpeg</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE.md">LICENSE.md</a> file for details.</p>
  
</body>
</html>
