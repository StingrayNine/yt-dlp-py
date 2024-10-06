import subprocess
from pprint import pprint
import inquirer

# Some variables
ytdlpPath = "./Assets/yt-dlp"
ffmpegPath = '''"--ffmpeg-location", "./Assets/ffmpeg-2024-10-02-git-358fdf3083-full_build/bin/ffmpeg.exe"'''
batchFilePath = '''"-a", ./Input/URLS.txt"'''
batchLink = "link"
audio = '''"-x", "--audio-format", "mp3"'''
video = '''"-f", state["format"]'''
output = '''"-P", "Output"'''

importQuestion = [
    inquirer.List(
        "type",
        message="What type of import are you using?",
        choices=["batch", "link"],
    ),
]
importState = inquirer.prompt(importQuestion)
pprint(importState)

formatQuestions = [
        inquirer.List(
            "format",
            message="What format do you need?",
            choices=["mp4", "mp3", "webm"],
            ),
            ]
state = inquirer.prompt(formatQuestions)
pprint(state["format"])

if importState["type"] == "batch":
    batchLink = batchFilePath
else:
	# Sanitize this, this is gross and insecure
	batchlink = str(input("Paste your youtube link: "))
    
if state["format"] == "mp3":
    subprocess.run([ytdlpPath, audio, ffmpegPath, output, batchLink])
else:
	subprocess.run([ytdlpPath, video, ffmpegPath, output, batchLink])

input("Press anykey to continue...")
