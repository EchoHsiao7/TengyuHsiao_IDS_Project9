setup:
	pip install -r requirements.txt


lint:
	pylint --disable=R,C,locally-disabled --ignore-patterns=test_.*?py *.py

format:	
	black *.py 


test:
	pytest 


dev:
	docker-compose up --build


clean:
	find . -type f -name "*.pyc" -delete
