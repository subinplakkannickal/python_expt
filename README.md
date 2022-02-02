# python
python experiments

Run pytest:
===========
	cd python_expt/
	pytest -v

Check coverage:
===============
	coverage run <file_name>
	coverage report -m
	# Togenerate html report
	coverage html 

Check coverage of testing:
==========================
	pytest --cov=source --cov-report=html

CI/CD implementation with jenkins
=================================
References:
- https://medium.com/swlh/build-your-first-automated-test-integration-with-pytest-jenkins-and-docker-ec738ec43955
- https://medium.com/@mreigen/integrate-jenkins-builds-into-github-pull-requests-33bc053d6210
- https://dzone.com/articles/adding-a-github-webhook-in-your-jenkins-pipeline

* Testing tags overriding
