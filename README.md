# Flask Docker Communication Project

This project contains two Flask applications (`app1` and `app2`) running in separate Docker containers that communicate with each other over a shared Docker network.

## Run Locally

```bash
docker network create flasknet
docker build -t app1_image ./app1
docker build -t app2_image ./app2
docker run -d --network flasknet -p 5000:5000 --name app1_container app1_image
docker run -d --network flasknet -p 5001:5001 --name app2_container app2_image
docker logs first_app_container
docker logs second_app_container
