import os
import subprocess

# define input and output folder paths
input_folder = os.getcwd()
output_folder = os.path.join(os.getcwd(), "frames_output")

# create output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    print(f"Output folder {output_folder} already exists, skipping creation.")

# iterate over video files in input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mkv") or filename.endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)
        output_subfolder = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, output_subfolder)

        # create subfolder for output frames
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # use ffmpeg to burn subtitles into video
        subtitle_args = f"subtitles='{input_path}:stream_index=2:force_style=Fontsize=20,Fontname=Arial,PrimaryColour=&H00FFFFFF&'"
        command = ['ffmpeg', '-i', input_path, '-vf', subtitle_args, '-crf', '23', '-r', '0.3', '-q:v', '1', '-start_number', '1', os.path.join(output_path, '%03d.jpg')]

        subprocess.call(command)
