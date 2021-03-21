help:
	@echo "    run"
	@echo "        start the web scraper"
	@echo "    "

.PHONY: run
run:
	@docker-compose up -d --build && docker-compose logs -tf
