# AudioDatasetConverter
Convert large amounts of audio files for Data Science/DJ/Producer tings.

The command line arguments are: -i <input_folder> -o <output_folder> -fInput <input_format> -fOutput <output_format>

Accepted arguments for the format (both input and output) are: .wav, .ogg, .flac, .mp3, .aiff, .aif

To install this tool make sure you have these libraries installed through pip
import argparse
import os
import pathlib
import soundfile
from glob
