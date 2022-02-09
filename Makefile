DOCKER := docker
DOCKER_COMPOSE := docker-compose
SENSYNE_SERVICE := sensyne

FLAKE8 := flake8 . --ignore=E501,W503 --exclude=venv,migrations
BANDIT := bandit .
BLACK := black --check .
MYPY := mypy . --ignore-missing-imports --exclude migrations
TEST_CMD := scripts/run_tests.sh

RUN_LINTER := ${DOCKER_COMPOSE} run --rm linter

build:
	${DOCKER_COMPOSE} build 

.PHONY: up
up: build
	${DOCKER_COMPOSE} up ${SENSYNE_SERVICE}

.PHONY: flake8
flake8:
	$(RUN_LINTER) $(FLAKE8)

.PHONY: bandit
bandit:
	$(RUN_LINTER) $(BANDIT)

.PHONY: black
black:
	$(RUN_LINTER) $(BLACK)

.PHONY: mypy
mypy:
	$(RUN_LINTER) $(MYPY)

.PHONY: lint
lint: build mypy flake8 bandit black

.PHONY: test
test: build
	$(PREFIX_COMPOSE) stop
	$(PREFIX_COMPOSE) rm -f
	$(PREFIX_COMPOSE) run --rm gms_state_handler sh -c "./docker-entrypoint.sh && ${TEST_CMD}"
	$(PREFIX_COMPOSE) stop

.PHONY: pyclean
pyclean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +
