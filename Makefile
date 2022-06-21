EXE_NAME=youtube-download
INSTALL_DIR=~/.local/bin

install:
	@cp -v ${EXE_NAME} ${INSTALL_DIR}/

uninstall:
	@rm -v ${INSTALL_DIR}/${EXE_NAME} 
