import os
import subprocess

from utils import SUPPORTED_VIDEO_FORMATS, getSuffix


def appendFilename(filename, suffix):
    return "{0}_{2}.{1}".format(*filename.rsplit(".", 1) + [suffix])


def getVideosToCompress(sourceFolder, encodeQuality):
    sourceVideos: list[str] = []
    targetVideos: list[str] = []
    suffix = getSuffix(encodeQuality)
    for root, _, files in os.walk(sourceFolder):
        for file in files:
            if (file.endswith(SUPPORTED_VIDEO_FORMATS)) and (suffix not in file):
                sourceVideos.append(os.path.join(root, file))
                targetVideos.append(os.path.join(root, appendFilename(file, suffix)))
    return sourceVideos, targetVideos


def compressVDO(sourceFolder, encodeQuality, dryrun=True):
    sourceVideos, targetVideos = getVideosToCompress(
        sourceFolder=sourceFolder, encodeQuality=encodeQuality
    )
    for idx, (sourceVideo, targetVideo) in enumerate(zip(sourceVideos, targetVideos)):
        print(f"{idx + 1}: {sourceFolder} ===> {targetVideo}")

    if dryrun:
        return

    for sourceVideo, targetVideo in zip(sourceVideos, targetVideos):
        if not os.path.exists(targetVideo):
            subprocess.run(
                [
                    "pack",
                    sourceVideo,
                    "--output",
                    targetVideo,
                    "-q",
                    f"{encodeQuality}",
                ],
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
