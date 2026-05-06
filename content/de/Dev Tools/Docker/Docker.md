---
title: "Docker"
---
[[ru/Dev Tools/Docker/Docker|RU]] | [[en/Dev Tools/Docker/Docker|EN]] | [[de/Dev Tools/Docker/Docker|DE]]
## 1) Grundbegriffe

- **Image (Abbild)** – Vorlage des Dateisystems + Metadaten. Geschichtete Struktur (Union-FS).
- **Container** – laufende Instanz eines Images (Prozess + Isolation).
- **Registry** – Speicherort für Images (Docker Hub, GitHub Container Registry, GitLab, privat).
- **Layer (Schicht)** – unveränderliche „Deltas“ eines Images. Build-Cache.
- **Tag** – Versionskennzeichnung eines Images (`:1.2.3`, `:latest`, `:dev`).
- **Volume** – persistente Daten außerhalb des Lebenszyklus eines Containers.
- **Network** – virtuelles Docker-Netzwerk (bridge/host/overlay).
- **Context** – Build-Ordner; alles, was in `docker build` einfließt (kontrolliere mit `.dockerignore`).
## 2) Installation und schneller Test

```bash
# version
docker version
# einfacher Test
docker run --rm hello-world
# interaktives Ubuntu
docker run -it --rm ubuntu:24.04 bash
```
## 3) Häufig verwendete Befehle (Einseiter)

```bash
# Images
docker images                                   
# List 
docker pull alpine:3.20
docker rmi IMAGE_ID

# Container
docker ps -a
docker run -d --name web -p 8080:80 nginx:1.27
docker logs -f web
docker exec -it web sh
docker stop web && docker rm web

# Build
docker build -t myorg/myapp:1.0.0 .
docker tag myorg/myapp:1.0.0 myorg/myapp:latest
docker push myorg/myapp:1.0.0

# Netzwerk und Volumes
docker network ls
docker network create appnet
docker volume ls
docker volume create pgdata
docker run -d --name pg --network appnet -v pgdata:/var/lib/postgresql/data postgres:16

# Bereinigung
docker system df
docker system prune -f
docker volume prune -f
```
## 4) .dockerignore (unbedingt)

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
## 5) Dockerfile — patterns
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
### 5.2 Python (uvicorn + fastapi), dünne Schicht, Caching über requirements

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

`requirements.txt` (Beispiel für die Einsatzbereitschaft):
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
### 5.4 Nginx как reverse-proxy с healthcheck

```bash
FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/nginx.conf
HEALTHCHECK --interval=10s --timeout=2s --retries=3 CMD wget -qO- http://localhost/health || exit 1
```

`nginx.conf`:
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
## 6) docker-compose: Fertige Stacks
### 6.1 Postgres + pgAdmin + Anwendung (Java/Python/Node — Einheitliche Vorlage)

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
      db:
        condition: service_healthy
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
      # для Spring:
      # SPRING_DATASOURCE_URL: jdbc:postgresql://db:5432/appdb
      # SPRING_DATASOURCE_USERNAME: appuser
      # SPRING_DATASOURCE_PASSWORD: appsecret
    ports:
      - "8080:8080"   # или 8000/3000
    depends_on:
      db:
        condition: service_healthy
    networks: [appnet]

volumes:
  dbdata:

networks:
  appnet:
    driver: bridge
```
## 6.2 Prod-Zwischenschicht: Nginx-Proxy vor der Anwendung

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
networks:
  appnet:
    driver: bridge
```
## 7) Tags und Versionen: Strategie

- Verlass dich im Produktivbetrieb niemals auf `:latest`.
- Verwende **semantische Tags**: `1.4.2`, plus „Kanäle“: `:prod`, `:staging`, `:dev`.
- - Unveränderliche Releases: `myorg/myapp:1.4.2` wird einmal veröffentlicht; Änderungen → neue Nummer.
## 8) Optimierung der Imagegröße

- Multi-Stage-Build (oben).
- Basis-Images wie `-slim`, `alpine` (vorsichtig bei glibc/musl).
- Caches löschen (`apt-get clean`, `rm -rf /var/lib/apt/lists/*`).
- Für Python – `--no-cache-dir`, für Node – Production-Install.
- Distroless/ubi-micro/runtime-only, Non-Root-Benutzer.
## 9) Sicherheit (minimal, aber zielgerichtet)

- **USER nonroot** in der Runtime-Schicht.
- Angriffsfläche minimieren: keine Compiler oder Shell im finalen Image.
- Basis-Images regelmäßig aktualisieren.
- **HEALTHCHECK**, `readOnlyRootFilesystem` (in k8s), Volumes nur, wo nötig.
- Keine Secrets im Image: Umgebungsvariablen, Secret-Stores oder `docker secret` (Swarm) bzw. k8s Secrets verwenden.
- Images signieren und prüfen (Cosign/SBOM — Syft/Grype) – im CI.
## 10) Logs, Debugging, Profile

```bash
docker logs -f app
docker exec -it app sh        
docker top app
docker inspect app | less
docker stats
docker cp app:/path/in/container ./local
```

Wenn der Container sofort „abstürzt“, füge einen „interaktiven“ Entrypoint zur Fehlersuche hinzu:
```bash
CMD ["sh","-c","sleep 3600"]
```

oder starte ihn vorübergehend interaktiv neu:
```bash
docker run --rm -it --entrypoint sh myorg/myapp:1.0.0
```
## 11) Ressourcenlimits und Neustart-Richtlinien

```bash
docker run -d --name app \
  --memory=512m --cpus=1.0 \
  --restart=unless-stopped \
  myorg/myapp:1.0.0
```
Richtlinien: `no` (Standard), `on-failure`, `unless-stopped`, `always`.

## 12) Netzwerke: Typen und Anwendungsfälle

- **bridge** (Standard): Isolation zwischen Projekten, Dienste erreichbar über Namen.
- **host**: ohne NAT, Host-Ports = Container-Ports (nur unter Linux).
- **overlay**: für Swarm/Multi-Host-Setups.
- Schnelle Verbindung: `--network appnet` + Zugriff über `http://service_name:port`.
## 13) Volumes: Daten außerhalb des Containers

- **Named Volume** für Datenbanken: Langlebigkeit und Portabilität.
- **Bind Mount** für lokale Entwicklung (Quellcode einbinden).
- Beispiel für Node-Entwicklung:
```bash
docker run -it --rm \
  -v $PWD:/app -w /app \
  -p 3000:3000 node:22-alpine sh
```
## 14) CI/CD: GitHub Actions (fertiger Workflow)

`.github/workflows/docker-build-push.yml`:
```yaml
name: Build and push image
on:
  push:
    branches: [ "main" ]
    tags: [ "v*" ]

jobs:
  docker:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
      id-token: write
    steps:
      - uses: actions/checkout@v4

      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3

      - name: Set up Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=ref,event=branch
            type=ref,event=tag
            type=sha

      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          platforms: linux/amd64,linux/arm64
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```
## 15) Buildx und Plattformübergreifendes Bauen

```bash
docker buildx create --use
docker buildx ls
docker buildx build --platform linux/amd64,linux/arm64 -t myorg/myapp:1.0.0 --push .
```
## 16) Feinheiten für den Produktionseinsatz

- **Unveränderlichkeit**: Deployment nur per Tags, Rollback durch Tag-Umschaltung.
- **Readiness/Liveness** (über HEALTHCHECK, in k8s – Probes).
- **Konfigurationen**: über Umgebungsvariablen/Dateien in Volumes; ein Image – mehrere Umgebungen.
- **Root deaktivieren**, `umask` aktivieren, `CAP_*` einschränken (in k8s SecurityContext).
- **SBOM/Schwachstellenscans** im CI vor der Veröffentlichung.
## 17) Typische Probleme und Lösungen

- **Port wird nicht gehört**: Die Anwendung hört intern auf `127.0.0.1`; gib `0.0.0.0` an.
- **Großes Image**: Aktiviere Multi-Stage-Builds und verwende ein Slim-Basisimage; lösche Caches und Dev-Abhängigkeiten.
- **Build-Cache funktioniert nicht**: Überprüfe die Reihenfolge der `COPY`-Befehle – zuerst Lock-Dateien/Abhängigkeiten, dann Quellcode.
- **Dateiberechtigungen**: Ändere den Besitzer in der Runtime-Schicht (`chown`) und verwende `USER`.
- **„Sieht die Datenbank nicht“**: Überprüfe Netzwerk und Servicenamen (`db`), warte auf Readiness (Healthcheck + `depends_on`).
## 18) Mini-Vorlagen für den echten Start
### 18.1 Spring Boot + Postgres (Compose + Dockerfile)

```bash
**Dockerfile** — wie in §5.1  
**docker-compose.yml** — wie in §6.1 (Port `8080:8080`, Umgebungsvariablen für Spring sind auskommentiert — kommentiere sie bei Bedarf wieder ein).
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

`requirements.txt` — из §5.2, `Dockerfile` — из §5.2, затем:
```bash
docker build -t fastapi-hello:1.0 .
docker run -d -p 8000:8000 --name api fastapi-hello:1.0
```
### 18.3 Node HTTP сервер (ohne frameworks)

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
Dockerfile — §5.3.
## 19) Lokale Entwicklung vs Produktion

- **Dev**: Bind-Mounts, Live-Reload, `docker compose up --build`.
- **Prod**: nur unveränderliche Images, Konfiguration über Env/Secrets, Proxy, Healthchecks, Ressourcenlimits.
## 20) Swarm и Kubernetes (Wie geht es weiter)

- **Swarm**: einfacher Docker-Orchestrator (`docker swarm init`, `docker stack deploy -c docker-compose.yml mystack`).
- **Kubernetes**: Branchenstandard. Umstieg: zerlege Compose in Manifeste (Deployment/Service/Ingress/ConfigMap/Secret) oder nutze Kompose/Helm. Achte auf Probes, Ressourcen/Limits, SecurityContext.
## 21) Checkliste vor dem Release

1. Multi-Stage-Build + `.dockerignore`.
2. Non-Root-Benutzer.
3. **HEALTHCHECK** funktioniert.
4. Versions-Tags gesetzt.
5. Image gescannt (Vulnerabilities/SBOM).
6. Konfigurationen und Secrets nicht ins Image „eingebacken“.
7. CPU/RAM-Limits definiert.
8. CI baut und pusht Artefakte anhand der Tags.
9. Schneller Rollback möglich (alter Tag).
