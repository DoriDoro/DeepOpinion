generate_secret_key:
	python -c 'import secrets; print(secrets.token_hex(32))'

server:
	flask --app server run --debug

shell:
	ipython
