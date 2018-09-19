# -*- mode: python -*-

block_cipher = None


a = Analysis(['RegimUI.py'],
             pathex=['C:\\Users\\Fabian\\Desktop\\Fabi_py_Projects\\RegimUI'],
             binaries=[],
             datas=[('images/*', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Regim-2.7',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , version='version.txt', icon='images/icon.ico')
