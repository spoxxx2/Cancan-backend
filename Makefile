publish:
	git add .
	git commit -m "Final SGO v1.3 Deployment" || true
	git push origin main
	@echo "--- CANCAN KERN DOI v1.3 LIVE ---"
