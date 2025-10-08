---
title: "Docker"
---
## 1) Базовые понятия

- **Image (образ)** — шаблон файловой системы + метаданные. Слоистая структура (union FS).
- **Container (контейнер)** — запущенный экземпляр образа (процесс + изоляция).
- **Registry** — хранилище образов (Docker Hub, GitHub Container Registry, GitLab, приватный).
- **Layer (слой)** — неизменяемые «дельты» образа. Кэш сборки.
- **Tag** — метка версии образа (`:1.2.3`, `:latest`, `:dev`).
- **Volume** — постоянные данные вне жизненного цикла контейнера.
- **Network** — виртуальная сеть Docker (bridge/host/overlay).
- **Context** — папка сборки; всё, что попадёт в `docker build` (контролируй через `.dockerignore`).
## 2) Установка и быстрый тест

```bash
# версия
docker version
# простой тест
docker run --rm hello-world
# интерактивный Ubuntu
docker run -it --rm ubuntu:24.04 bash
```
## 3) Часто используемые команды (1-страничник)

```bash
# Образы
docker images                                   # список
docker pull alpine:3.20
docker rmi IMAGE_ID

# Контейнеры
docker ps -a
docker run -d --name web -p 8080:80 nginx:1.27
docker logs -f web
docker exec -it web sh
docker stop web && docker rm web

# Сборка
docker build -t myorg/myapp:1.0.0 .
docker tag myorg/myapp:1.0.0 myorg/myapp:latest
docker push myorg/myapp:1.0.0

# Сеть и тома
docker network ls
docker network create appnet
docker volume ls
docker volume create pgdata
docker run -d --name pg --network appnet -v pgdata:/var/lib/postgresql/data postgres:16

# Очистка
docker system df
docker system prune -f
docker volume prune -f
```
## 4) .dockerignore (обязательно)

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
## 5) Dockerfile — паттерны
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
### 5.2 Python (uvicorn + fastapi), тонкий слой, кэш через requirements

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

`requirements.txt` (пример для готовности):
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

`nginx.conf` минимальный:
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
## 6) docker-compose: готовые стеки
### 6.1 Postgres + pgAdmin + приложение (Java/Python/Node — единый шаблон)

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
      - "8080:8080"   # или 8000/3000 в зависимости от приложения
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
## 6.2 Prod-прокладка: Nginx-proxy перед приложением

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
## 7) Теги и версии: стратегия

- Никогда не полагайся на `:latest` в проде.
- Ставь **семантические теги**: `1.4.2`, плюс «каналы»: `:prod`, `:staging`, `:dev`.
- Иммутабельные релизы: `myorg/myapp:1.4.2` публикуется один раз; правки — новый номер.
## 8) Оптимизация размера образа

- Multi-stage build (сверху).
- Базовые образы `-slim`, `alpine` (осторожно с glibc/musl).
- Удаляй кеши (`apt-get clean`, `rm -rf /var/lib/apt/lists/*`).
- Для Python — `--no-cache-dir`, для Node — production-install.
- Distroless/ubi-micro/runtime-only, non-root пользователь.
## 9) Безопасность (минимум, но по делу)

- **USER nonroot** в runtime-слое.
- Минимизируй поверхность: без компиляторов и шелла в финальном образе.
- Регулярно обновляй базовые образы.
- HEALTHCHECK, `readOnlyRootFilesystem` (в k8s), тома только там, где нужно.
- Secrets не встраивать в образ: использовать переменные окружения/secret-хранилища/`docker secret` (Swarm) или k8s Secrets.
- Подписывай и проверяй образы (Cosign/SBOM — Syft/Grype) — в CI.
## 10) Логи, отладка, профили

```bash
docker logs -f app
docker exec -it app sh        # или bash
docker top app
docker inspect app | less
docker stats
docker cp app:/path/in/container ./local
```

Если контейнер сразу «падает», добавь «интерактивный» entrypoint для отладки:
```bash
CMD ["sh","-c","sleep 3600"]
```

или временно перезапусти с интерактивом:
```bash
docker run --rm -it --entrypoint sh myorg/myapp:1.0.0
```
## 11) Ресурсные лимиты и рестарт-политики

```bash
docker run -d --name app \
  --memory=512m --cpus=1.0 \
  --restart=unless-stopped \
  myorg/myapp:1.0.0
```
Политики: `no` (дефолт), `on-failure`, `unless-stopped`, `always`.

## 12) Сети: типы и кейсы

- **bridge** (дефолт): изоляция между проектами, сервисы достучатся по имени.
- **host**: без NAT, порты хоста = порты контейнера (Linux only).
- **overlay**: для Swarm/мульти-хоста.
- Быстрый линк: `--network appnet` + обращение по `http://service_name:port`.
## 13) Томá: данные вне контейнера

- **named volume** для БД: долговечность и переносимость.
- **bind mount** для локальной разработки (монтируешь исходники).
- Пример разработки Node:
```bash
docker run -it --rm \
  -v $PWD:/app -w /app \
  -p 3000:3000 node:22-alpine sh
```
## 14) CI/CD: GitHub Actions (готовый workflow)

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
## 15) Buildx и кросс-платформенность

```bash
docker buildx create --use
docker buildx ls
docker buildx build --platform linux/amd64,linux/arm64 -t myorg/myapp:1.0.0 --push .
```
## 16) Тонкости для продакшена

- **Иммутабельность**: деплой только по тегам, rollback — переключением тега.
- **Readiness/Liveness** (через HEALTHCHECK, а в k8s — probes).
- **Конфиги**: через переменные окружения/файлы в volume; один образ — много окружений.
- **Отключай root**, включай `umask`, ограничивай `CAP_*` (в k8s SecurityContext).
- **SBOM/сканирование уязвимостей** в CI до публикации.
## 17) Типовые проблемы и решения

- **Порт не слушается**: внутри приложение слушает `127.0.0.1`; укажи `0.0.0.0`.
- **Большой образ**: включи multi-stage и slim-базу; чисти кеши и dev-зависимости.
- **Кэш сборки не работает**: проверь порядок `COPY` — сначала lock-файлы/зависимости, потом исходники.
- **Права доступа к файлам**: меняй владельца в runtime-слое (`chown`) и используй `USER`.
- **«Не видит БД»**: проверь сеть и имя сервиса (`db`), дождись readiness (healthcheck + `depends_on`).
## 18) Мини-шаблоны для реального старта
### 18.1 Spring Boot + Postgres (Compose + Dockerfile)

```bash
**Dockerfile** — как в §5.1  
**docker-compose.yml** — как в §6.1 (порт `8080:8080`, env для Spring закомментированы — раскомментируй при необходимости).
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
### 18.3 Node HTTP сервер (без фреймворков)

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
Dockerfile — из §5.3.
## 19) Локальная разработка vs прод

- **Dev**: bind mounts, live-reload, `docker compose up --build`.
- **Prod**: только иммутабельные образы, конфиги через env/секреты, прокси, healthchecks, лимиты ресурсов.
## 20) Swarm и Kubernetes (куда дальше)

- **Swarm**: простой оркестратор Docker (`docker swarm init`, `docker stack deploy -c docker-compose.yml mystack`).
- **Kubernetes**: стандарт индустрии. Переход: разбивай compose на манифесты (Deployment/Service/Ingress/ConfigMap/Secret) или используй Kompose/Helm. Следи за probes, ресурсы/лимиты, securityContext.
## 21) Чек-лист перед релизом

1. Multi-stage + `.dockerignore`.
2. Non-root пользователь.
3. HEALTHCHECK работает.
4. Теги версий проставлены.
5. Образ отсканирован (Vulns/SBOM).
6. Конфиги и секреты не «запечены» в образ.
7. Лимиты CPU/RAM заданы.
8. CI собирает и пушит артефакты по тегам.
9. Есть быстрый rollback (старый тег).
