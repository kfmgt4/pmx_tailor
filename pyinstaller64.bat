rem@echo off
rem --- 
rem ---  exe�𐶐�
rem --- 

rem ---  �J�����g�f�B���N�g�������s��ɕύX
cd /d %~dp0

cls

del dist\*.lnk
move /y dist\*.exe dist\past

activate vmdsizing_np && cd src && python translate.py && cd .. && activate vmdsizing_cython && src\setup_install.bat && pyinstaller --clean pmx_tailor.spec && copy /y archive\Readme.txt dist\Readme.txt && copy /y archive\����Readme.txt dist\����Readme.txt && activate vmdsizing_np && cd src && python lnk.py && cd ..
rem activate vmdsizing_cython && pyinstaller --clean pmx_tailor.spec

net start beep
rundll32 user32.dll,MessageBeep
net stop beep
