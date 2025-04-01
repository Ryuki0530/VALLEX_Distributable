@echo off
git clone https://github.com/Plachtaa/VALL-E-X.git
copy .\mainWithGUIv2.1.py .\VALL-E-X
copy .\icon.ico .\VALL-E-X
cd .\VALL-E-X
mkdir outputs
cd ..\
.\Python310\python.exe -m venv valle_env
call .\valle_env\Scripts\activate
python --version
pip install -r requirementsForGUI.txt
pause
exit