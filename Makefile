APP_DIR=src

#----------- Requirements --------
install-libs:
	# complicated make lib, uses pydistutils.cfg for docker
	if [ -f libs.txt ]; then \
		if [ -f ~/.pydistutils.cfg.backup ]; then \
			cp ~/.pydistutils.cfg.backup ~/.pydistutils.cfg; \
		fi; \
		pip install -t $(APP_DIR) -r libs.txt; \
		if [ -f ~/.pydistutils.cfg ]; then \
			rm ~/.pydistutils.cfg; \
		fi; \
	fi;

build:
	rm -f lambda.zip
	cd $(APP_DIR) && \
	zip -X -r ../lambda.zip *

deploy:
	aws lambda update-function-code --function-name ${FUNCTION} --zip-file fileb://lambda.zip --profile ${PROFILE}
