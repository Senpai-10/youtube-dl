EXE_NAME="youtube-download"
INSTALL_DIR=/usr/bin

install:
	cp ${EXE_NAME} ${INSTALL_DIR}/

uninstall:
	rm -v ${INSTALL_DIR}/${EXE_NAME} 
