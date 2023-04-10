# -*- mode: python ; coding: utf-8 -*-

import dataui
duipath = os.path.dirname(dataui.__file__)

block_cipher = None


a = Analysis(['../src/gadget.py'],
             pathex=['/Volumes/home/ymq/pydev/github/gadget/src'],
             binaries=[],
             datas=[
				(f'{duipath}/tmpl/bricks/*.*', 'dataui/tmpl/bricks')
			 ],
             hiddenimports=[
				'sqlite3',
				'aiopg',
				'aiomysql'
			 ],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='gadget',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
