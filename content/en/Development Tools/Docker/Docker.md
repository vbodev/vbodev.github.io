---
title: Docker
---
## 1) Basic Concepts
- **Image (образ)** — filesystem template + metadata. Layered structure (union FS).
- **Container (контейнер)** — a running instance of an image (process + isolation).
- **Registry** — an image repository (Docker Hub, GitHub Container Registry, GitLab, private).
- **Layer (слой)** — immutable "deltas" of the image. Build cache.
- **Tag** — image version label (`:1.2.3`, `:latest`, `:dev`).
- **Volume** — persistent data outside the container lifecycle.
- **Network** — Docker virtual network (bridge/host/overlay).
- **Context** — build directory; everything that ends up in `docker build` (controlled via `.dockerignore`).

## 2) Installation and Quick Test
```bash
# version
docker version
# simple test
docker run --rm hello-world
# interactive Ubuntu
docker run -it --rm ubuntu:24.04 bash
```

## 3) Frequently Used Commands (One-Pager)
```bash
# Images
docker images  # list
docker pull alpine:3.20
docker rmi IMAGE_ID

# Containers
docker ps -a
docker run -d --name web -p 8080:80 nginx:1.27
docker logs -f web
docker exec -it web sh
docker stop web && docker rm web

# Build
docker build -t myorg/myapp:1.0.0 .
docker tag myorg/myapp:1.0.0 myorg/myapp:latest
docker push myorg/myapp:1.0.0

# Network and Volumes
docker network ls
docker network create appnet
docker volume ls
docker volume create pgdata
docker run -d --name pg --network appnet -v pgdata:/var/lib/postgresql/data postgres:16

# Cleanup
docker system df
docker system prune -f
docker volume prune -f
```

## 4) .dockerignore (Mandatory)
```.dockerignore
.git
.gitignore
target
build
dist
node_modules
.cache
__pycache__
*.log
*.tmp
.DS_Store
.env
```

## 5) Dockerfile — Patterns
### 5.1 Multi-stage (Java Spring Boot, JDK 21)
```bash
# ====== Build stage ======
FROM maven:3.9.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -B -q -e -DskipTests dependency:go-offline
COPY src ./src
RUN mvn -B -q -e -DskipTests package

# ====== Runtime stage (distroless) ======
FROM gcr.io/distroless/java21-debian12:latest
WORKDIR /app
COPY --from=build /app/target/*.jar /app/app.jar
EXPOSE 8080
USER nonroot
ENV JAVA_TOOL_OPTIONS="-XX:+UseContainerSupport -XX:MaxRAMPercentage=75"
ENTRYPOINT ["java","-jar","/app/app.jar"]
```

### 5.2 Python (uvicorn + fastapi), thin layer, cache via requirements
```bash
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /app
RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY app ./app
EXPOSE 8000
CMD ["python","-m","uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
```
`requirements.txt` (example for readiness):
```ini
fastapi==0.115.5
uvicorn==0.32.0
```

### 5.3 Node.js (PNPM), production-install, non-root
```bash
FROM node:22-alpine AS deps
WORKDIR /app
RUN corepack enable
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

FROM node:22-alpine AS build
WORKDIR /app
RUN corepack enable
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN pnpm run build

FROM node:22-alpine AS runtime
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup -S app && adduser -S app -G app
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
EXPOSE 3000
USER app
CMD ["node","dist/server.js"]
```

### 5.4 Nginx as reverse-proxy with healthcheck
```bash
FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/nginx.conf
HEALTHCHECK --interval=10s --timeout=2s --retries=3 CMD wget -qO- http://localhost/health || exit 1
```

`nginx.conf` minimal:
```nginx
worker_processes auto;
events { worker_connections 1024; }
http {
  include /etc/nginx/mime.types;
  server {
  listen 80;
  location / {
  proxy_pass http://app:3000;
  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
  }
  location = /health { return 200 "OK"; add_header Content-Type text/plain; }
  }
}
```

## 6) docker-compose: ready stacks
### 6.1 Postgres + pgAdmin + application (Java/Python/Node — single template)
```yaml
version: "3.9"
services:
  db:
  image: postgres:16
  container_name: db
  restart: unless-stopped
  environment:
  POSTGRES_DB: appdb
  POSTGRES_USER: appuser
  POSTGRES_PASSWORD: appsecret
  volumes:
  - dbdata:/var/lib/postgresql/data
  networks: [appnet]
  healthcheck:
  test: ["CMD-SHELL","pg_isready -U appuser -d appdb"]
  interval: 10s
  timeout: 3s
  retries: 5

  pgadmin:
  image: dpage/pgadmin4:8
  container_name: pgadmin
  restart: unless-stopped
  environment:
  PGADMIN_DEFAULT_EMAIL: admin@example.com
  PGADMIN_DEFAULT_PASSWORD: admin123
  ports:
  - "5050:80"
  depends_on:
  - db
  networks: [appnet]

  app:
  build:
  context: .
  dockerfile: Dockerfile
  container_name: app
  restart: unless-stopped
  environment:
  DB_HOST: db
  DB_PORT: "5432"
  DB_NAME: appdb
  DB_USER: appuser
  DB_PASSWORD: appsecret
  # for Spring:
  # SPRING_DATASOURCE_URL: jdbc:postgresql://db:5432/appdb
  # SPRING_DATASOURCE_USERNAME: appuser
  # SPRING_DATASOURCE_PASSWORD: appsecret
  ports:
  - "8080:8080"  # or 8000/3000 depending on the application
  depends_on:
  - db
  networks: [appnet]

volumes:
  dbdata:

networks:
  appnet:
  driver: bridge
```

### 6.2 Prod proxy: Nginx before the application
```yaml
version: "3.9"
services:
  app:
  image: myorg/myapp:1.0.0
  networks: [appnet]
  proxy:
  build:
  context: ./proxy
  dockerfile: Dockerfile
  ports:
  - "80:80"
  depends_on:
  - app
  networks: [appnet]
```

## 17) Typical Problems and Solutions
- **Port not listening**: The application listens on `127.0.0.1`; specify `0.0.0.0`.
- **Large image**: Use multi-stage and slim base images; clean caches and dev dependencies.
- **Build cache not working**: Check the order of `COPY` – lock files/dependencies first, then source code.
- **File access rights**: Change ownership in the runtime layer (`chown`) and use `USER`.
- **"Cannot see DB"**: Check the network and service name (`db`), wait for readiness (healthcheck + `depends_on`).

## 18) Mini-Templates for Real Start
### 18.1 Spring Boot + Postgres (Compose + Dockerfile)
```bash
**Dockerfile** — as in §5.1
**docker-compose.yml** — as in §6.1 (port `8080:8080`, env for Spring commented out — uncomment if needed).
```

### 18.2 FastAPI hello-world
`app/main.py`:
```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health(): return {"status": "ok"}
@app.get("/")
def root(): return {"hello": "world"}
```
`requirements.txt` — as in §5.2, `Dockerfile` — as in §5.2, then:
```bash
docker build -t fastapi-hello:1.0 .
docker run -d -p 8000:8000 --name api fastapi-hello:1.0
```

### 18.3 Node HTTP server (without frameworks)
`package.json`:
```json
{
  "name": "node-hello",
  "version": "1.0.0",
  "type": "module",
  "scripts": { "start": "node dist/server.js", "build": "mkdir -p dist && cp -r src/* dist/" }
}
```
`src/server.js`:
```js
import http from "http";
const port = 3000;
const server = http.createServer((req, res) => {
  if (req.url === "/health") { res.writeHead(200, {"Content-Type":"text/plain"}); res.end("OK"); return; }
  res.writeHead(200, {"Content-Type":"application/json"});
  res.end(JSON.stringify({ hello: "world" }));
});
server.listen(port, "0.0.0.0", () => console.log(`Listening on :${port}`));
```
Dockerfile — as in §5.3.

## 19) Local Development vs Prod
- **Dev**: bind mounts, live-reload, `docker compose up --build`.
- **Prod**: only immutable images, config via env/secrets, proxies, healthchecks, CPU/RAM limits.

## 20) Swarm and Kubernetes (where to go next)
- **Swarm**: simple Docker orchestrator (`docker swarm init`, `docker stack deploy -c docker-compose.yml mystack`).
- **Kubernetes**: industry standard. Transition: break compose into manifests (Deployment/Service/Ingress/ConfigMap/Secret) or use Kompose/Helm. Monitor probes, resources/limits, securityContext.

## 21) Checklist Before Release
1. Multi-stage + `.dockerignore`.
2. Non-root user.
3. HEALTHCHECK works.
4. Version tags are set.
5. Image has been scanned (Vulns/SBOM).
6. Configs and secrets are not baked into the image.
7. CPU/RAM limits are set.
8. CI builds and pushes artifacts by tag.
9. There is a quick rollback (old tag).