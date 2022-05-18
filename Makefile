MAIN_SRC_FILE="youtube-download.py" # No extension
EXE_NAME=youtube-download
INSTALL_DIR=/usr/bin

build:
	pyinstaller src/${MAIN_SRC_FILE} --onefile -n ${EXE_NAME}
	
install: clean build
	sudo cp dist/${EXE_NAME} ${INSTALL_DIR}

uninstall:
	rm -v ${INSTALL_DIR}/${EXE_NAME} 

clean:
	rm -rfv .mypy_cache build dist `find . -type d -name __pycache__` '${EXE_NAME}.spec'
