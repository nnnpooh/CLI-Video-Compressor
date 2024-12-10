import os

from utils import getSuffix


def removeFilename(filename, suffix):
    return filename.replace(f"_{suffix}", "")


def getVideosToDelete(sourceFolder, encodeQuality):
    removedVideos: list[str] = []
    suffix = getSuffix(encodeQuality)
    for root, _, files in os.walk(sourceFolder):
        for file in files:
            if suffix in file:
                sourceVideo = os.path.join(root, removeFilename(file, suffix))
                if os.path.exists(sourceVideo):
                    removedVideos.append(sourceVideo)

    return removedVideos


def deleteSourceVDO(sourceFolder, encodeQuality, dryrun=True):
    removedVideos = getVideosToDelete(
        sourceFolder=sourceFolder, encodeQuality=encodeQuality
    )
    for idx, removedVideo in enumerate(removedVideos):
        print(f"{idx + 1} Removing {removedVideo}")
        if not dryrun:
            os.remove(removedVideo)
