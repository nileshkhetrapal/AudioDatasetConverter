"""
DESCRIPTION OF THE MODULE GOES HERE
Author: Nilesh Khetrapal
Class: CSI-260-01
Assignment: FINAL PROJECT

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
"""
This tool was written with help from GitHub Co-Pilot. I love GitHub Co-Pilot! I wonder if it feels the same about me?
The goal of this script is to convert Audio files in a dataset while preserving the directory structure.
This tools needs to be run from the command line. 
The command line arguments are: -i <input_folder> -o <output_folder> -fInput <input_format> -fOutput <output_format>
Accepted arguments for the format (both input and output) are: .wav, .ogg, .flac, .mp3, .aiff, .aif
"""
import argparse
import os
import pathlib
import soundfile as sf
from glob import glob

def convert_audio(input_folder, output_folder, input_format, output_format):
    """
    This function converts audio files from one format to another.
    The input_folder is the folder that contains the audio files.
    The output_folder is the folder where the converted audio files will be stored.
    The input_format is the format of the audio files in the input_folder.
    The output_format is the format of the audio files in the output_folder.
    """
    # Get the list of folders in the folder_path
    folders = glob(input_folder + "/*", recursive=True)
    # For each folder, get the list of audio files
    for folder in zip(folders, input_format):
        # Get the list of audio files in the folder
        audio_files = glob(folder[0] + "/*" + folder[1])
        # For each audio file, convert it to the output_format
        for audio_file in audio_files:
            # Get the name of the audio file
            audio_name = path.basename(audio_file)
            # Get the name of the output file
            output_name = audio_name.replace(folder[1], output_format)
            # Get the path of the output file
            output_path = (output_folder + "/" + output_name)
            #if output_folder does not exist, create it
            # Convert the audio file to the output_format
            data, samplerate = sf.read(audio_file)
            sf.write(output_path, data, samplerate)
            #sound = AudioSegment.from_ogg(ogg_file)
            #sound.export(wav_path, format="wav")    
    return output_folder;

class main():
    """
    This function is the main function of the script.
    """
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Convert audio files from one format to another.')
    parser.add_argument('-i', '--input_folder', help='The folder that contains the audio files.')
    parser.add_argument('-o', '--output_folder', help='The folder where the converted audio files will be stored.')
    parser.add_argument('-fI', '--input_format', help='The format of the audio files in the input_folder.')
    parser.add_argument('-fO', '--output_format', help='The format of the audio files in the output_folder.')
    args = parser.parse_args()
    # Input error fixing
    if args.input_folder == None:
        args.input_folder = input("Enter the input folder: ")
    if args.output_folder == None:
        args.output_folder = input("Enter the output folder: ")
    if args.input_format == None:
        args.input_format = input("Enter the input format: ")
    if args.output_format == None:
        args.output_format = input("Enter the output format: ")
    # Convert the audio files
    convert_audio(args.input_folder, args.output_folder, args.input_format, args.output_format)
main()
