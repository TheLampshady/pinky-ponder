#----------- Requirements --------
install-libs:
	# complicated make lib, uses pydistutils.cfg for docker
	if [ -f libs.txt ]; then \
		if [ -f ~/.pydistutils.cfg.backup ]; then \
			cp ~/.pydistutils.cfg.backup ~/.pydistutils.cfg; \
		fi; \
		pip install -t app -r libs.txt; \
		if [ -f ~/.pydistutils.cfg ]; then \
			rm ~/.pydistutils.cfg; \
		fi; \
	fi;

zip:
	mkdir -p build
	rm build/lambda.zip
	cd src
	zip -X -r ../build/lambda.zip *

deploy:
	aws lambda update-function-code --function-name ${FUNCTION} --zip-file fileb://build/lambda.zip
