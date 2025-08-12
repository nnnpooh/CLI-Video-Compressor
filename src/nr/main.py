import os

from compress import compressVDO
from delete import deleteSourceVDO

#######################################################
ENCODE_QUALITY = 80
sourceFolder = os.path.join("E:", "temp")
print(sourceFolder)

compressVDO(sourceFolder=sourceFolder, encodeQuality=ENCODE_QUALITY, dryrun=False)
deleteSourceVDO(sourceFolder=sourceFolder, encodeQuality=ENCODE_QUALITY, dryrun=False)
