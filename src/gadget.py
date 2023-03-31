import os
import sys
from dataui.crud_parser import BricksCRUDProcessor
from ahserver.configuredServer import ConfiguredServer

from appPublic.registerfunction import RegisterFunction
from appPublic.objectAction import ObjectAction
from appPublic.app_logger import create_logger
from appPublic.folderUtils import ProgramPath
from appPublic.jsonConfig import getConfig
from appPublic.i18n import getI18N

from ahserver.filedownload import path_encode
from imgThumb import thumb
from idFile import idFileDownload
from myauth import MyAuthAPI
from rf import getPublicKey, getI18nMapping
from loadplugins import load_plugins
from version import __version__

def encodeFilepath(id,event,d):
	if d is None:
		return d

	if type(d) == type([]):
		return ArrayEncodeFilepath(d)

	d['rows'] = ArrayEncodeFilepath(d['rows'])
	return d
	
def ArrayEncodeFilepath(d):
	ret = []
	for r in d:
		r['name'] = path_encode(r['name'])
		ret.append(r)
	return ret

if __name__ == '__main__':
	p = ProgramPath()
	workdir = os.getcwd()
	if len(sys.argv) > 1:
		print(workdir, sys.argv[1])
		workdir = sys.argv[1]
	print(workdir)
	config = getConfig(workdir, NS={'workdir':workdir, 'ProgramPath':p})
	if config.logger:
		logger = create_logger(config.logger.name or 'gadget',
							levelname=config.logger.levelname or 'debug',
							file=config.logger.logfile or None)
	else:
		logger = create_logger('gadget', levelname='debug')
	rf = RegisterFunction()
	rf.register('makeThumb',thumb)
	rf.register('idFileDownload',idFileDownload)
	rf.register('getPublicKey', getPublicKey)
	rf.register('getI18nMapping', getI18nMapping)

	i18n = getI18N(path=workdir)
	server = ConfiguredServer(auth_klass=MyAuthAPI)
	load_plugins(workdir)
	logger.info(f'gadget version={__version__}')
	logger.debug(f'debug mode show ?')
	server.run()
