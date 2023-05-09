import os
from PIL import Image, ExifTags
from io import BytesIO
from aiohttp.web_exceptions import (
	HTTPException,
	HTTPExpectationFailed,
	HTTPForbidden,
	HTTPMethodNotAllowed,
	HTTPNotFound,
)
from aiohttp.web_response import Response, StreamResponse

from appPublic.registerfunction import RegisterFunction
from appPublic.jsonConfig import getConfig
from ahserver.filedownload import file_download
from id2file import getFilenameFromId

def www_abspath(fp):
	if fp[0] == '/':
		fp = fp[1:]
	config = getConfig()
	return os.path.join(config.filesroot, fp)

async def idFileDownload(*args, **kw):
	print(f'idFileDownload(): {args=}, {kw=}')
	fname = kw.get('path', None)
	path = www_abspath(fname)
	print(f'{fname=}, {path=}')
	request = kw.get('request')
	return await file_download(request,path)
