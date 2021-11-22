# -*- coding: utf-8 -*-
# -*- mode: python -*-
# PmxTailor 64bit版

block_cipher = None


a = Analysis(['src\\executor.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources', 'wx._adv', 'wx._html', 'bezier', 'quaternion', 'PIL', 'module.MParams', 'utils.MBezierUtils'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['mkl','libopenblas', 'tkinter', 'win32comgenpy', 'traitlets', 'IPython', 'pydoc', 'lib2to3', 'pygments', 'matplotlib'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('.\\src\\pmx_tailor.ico','.\\src\\pmx_tailor.ico', 'Data'), ('.\\src\\locale\\en_US\\messages.json','.\\src\\locale\\en_US\\messages.json', 'Data'), ('.\\src\\locale\\ja_JP\\messages.json','.\\src\\locale\\ja_JP\\messages.json', 'Data'), ('.\\src\\locale\\zh_CN\\messages.json','.\\src\\locale\\zh_CN\\messages.json', 'Data')]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='PmxTailor_1.00.00_β25',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='.\\src\\pmx_tailor.ico')

