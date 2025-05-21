docker build -t charger-status .
docker stop charger-status
docker run -p 8000:8000 --name charger-status --rm charger-status