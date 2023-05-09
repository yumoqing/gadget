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
from ahserver.filedownload import file_download
from id2file import getFilenameFromId

async def idFileDownload(*args, **kw):
	print(f'idFileDownload(): {args=}, {kw=}')
	id = kw.get('id', None)
	fname = await getFilenameFromId(id)
	request = kw.get('request')
	return await file_download(request,fname)
