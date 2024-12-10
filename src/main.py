# Need to install exiftool using (for example) choco

import os
import subprocess

ENCODE_QUALITY = 80


def appendFilename(filename, txt):
    return "{0}_{2}.{1}".format(*filename.rsplit(".", 1) + [txt])


SUPPORTED_VIDEO_FORMATS = (".mp4", ".mov", ".MP4", ".MOV")

sourceFolder = "C://Users//nnnpo//Desktop//1-3"
sourceVideos: list[str] = []
targetVideos: list[str] = []
for root, _, files in os.walk(sourceFolder):
    for file in files:
        if (file.endswith(SUPPORTED_VIDEO_FORMATS)) and ("_compressed" not in file):
            sourceVideos.append(os.path.join(root, file))
            targetVideos.append(os.path.join(root, appendFilename(file, "compressed")))

print(sourceVideos)
print(targetVideos)
for sourceVideo, targetVideo in zip(sourceVideos, targetVideos):
    if not os.path.exists(targetVideo):
        subprocess.run(
            ["pack", sourceVideo, "--output", targetVideo, "-q", f"{ENCODE_QUALITY}"],
            shell=True,
        )
        subprocess.run(
            [
                "exiftool",
                "-ee",
                "-tagsFromFile",
                sourceVideo,
                "-All:All",
                targetVideo,
                "-overwrite_original",
            ]
        )

for sourceVideo in sourceVideos:
    os.remove(sourceVideo)
