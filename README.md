# Flipkart search indexer — tag, push and pull, and be exact about what a tag promises

`GET /index` reports an indexing run. The service is incidental; the registry is the subject.

## Authenticating to GitHub Container Registry with a token you already have

`ghcr.io` accepts a GitHub personal access token with the `write:packages` scope. Create one at
**Settings → Developer settings → Personal access tokens**, then:

    echo "$GHCR_TOKEN" | docker login ghcr.io -u YOUR-GITHUB-USERNAME --password-stdin

⚠️ `docker login ghcr.io` **succeeds even when the token cannot push** — GHCR authorises at
push time, not at login. So a successful login is not evidence you are done; the first push is.
That is worth knowing before you spend an hour debugging the wrong step.

## Build and tag

    docker build -t ghcr.io/YOUR-GITHUB-USERNAME/search-indexer:0.1.0 .

## Pull it back by digest

A tag can be moved; a digest cannot. After pushing:

    docker inspect --format '{{index .RepoDigests 0}}' ghcr.io/YOUR-GITHUB-USERNAME/search-indexer:0.1.0
    docker pull ghcr.io/YOUR-GITHUB-USERNAME/search-indexer@sha256:...

## Run it

    python3 app/server.py
    curl localhost:8080/index
