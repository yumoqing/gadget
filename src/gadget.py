import os
import sys
import argparse
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
from idfile import idFileDownload
from myauth import MyAuthAPI
from rf import getPublicKey, getI18nMapping
from loadplugins import load_plugins
from version import __version__
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog="Gadget")
	parser.add_argument('-w', '--workdir')
	parser.add_argument('-p', '--port')
	args = parser.parse_args()
	workdir = args.workdir or os.getcwd()
	p = ProgramPath()
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
	server = ConfiguredServer(auth_klass=MyAuthAPI, workdir=workdir)
	load_plugins(workdir)
	logger.info(f'gadget version={__version__}')
	logger.debug(f'debug mode show ?')
	port = args.port or config.website.port or 8080
	port = int(port)
	server.run(port=port)
