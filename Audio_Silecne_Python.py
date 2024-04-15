import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Specify the path to ffmpeg
AudioSegment.converter = "../ffmpeg/bin/ffmpeg.exe"

# Path to the folder with input files
input_folder = "../input/"

# Path to the folder with output files
output_folder = "../output/"

# Get a list of all wav files in the input folder
wav_files = [f for f in os.listdir(input_folder) if f.endswith('.wav')]

# Process each wav file
for wav_file in wav_files:
    # Load the audio file
    audio = AudioSegment.from_wav(os.path.join(input_folder, wav_file))

    # Split the audio file into parts by silence
    chunks = split_on_silence(audio, min_silence_len=2000, silence_thresh=-16)

    # Export each chunk to a separate file
    for i, chunk in enumerate(chunks):
        chunk.export(os.path.join(output_folder, f"{wav_file}_chunk{i}.wav"), format="wav", bitrate="24k")

print("All audio files have been successfully split into parts.")