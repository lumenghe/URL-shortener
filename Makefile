COMPOSE = docker-compose -p url_shortener

.PHONY: run
run:
	$(COMPOSE) build app deprecation
	$(COMPOSE) up app deprecation


.PHONY: down
down:
	$(COMPOSE) down --volumes


.PHONY: format
format:
	$(COMPOSE) build format-imports
	$(COMPOSE) run format-imports
	$(COMPOSE) build format
	$(COMPOSE) run format


.PHONY: check-format
check-format:
	$(COMPOSE) build check-format-imports
	$(COMPOSE) run check-format-imports
	$(COMPOSE) build check-format
	$(COMPOSE) run check-format


.PHONY: style
style: check-format
	$(COMPOSE) build style
	$(COMPOSE) run style


.PHONY: test-unit
test-unit:
	$(COMPOSE) build test-unit
	$(COMPOSE) run test-unit

.PHONY: test-integration
test-integration:
	$(COMPOSE) build test-integration
	$(COMPOSE) run test-integration

.PHONY: test
test: test-unit test-integration

