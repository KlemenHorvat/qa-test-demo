# QA Test Framework Demo

A containerised test automation project showcasing **API**, **E2E**, and **load testing** — built with **pytest**, **Playwright**, and **Locust**, running in **Docker** and verified by **GitHub Actions**.

This repo demonstrates my approach to testing in a modern, safety‑critical software environment (healthcare‑focused).

## 📁 Project Structure

```
qa-test-demo/
├── api-tests/ # REST API integration tests (pytest + requests)
│ ├── Dockerfile
│ ├── requirements.txt
│ └── tests/
│ ├── conftest.py
│ └── test_posts.py
├── e2e-tests/ # End‑to‑end UI tests (Playwright + pytest)
│ ├── Dockerfile
│ ├── requirements.txt
│ └── tests/
│ └── test_hapi_fhir_ui.py
├── load-tests/ # Performance / load tests (Locust)
│ ├── Dockerfile
│ ├── requirements.txt
│ └── locustfile.py
└── .github/workflows/ # CI pipelines for each test type
├── run-tests.yml (API)
├── e2e-tests.yml (E2E)
└── load-tests.yml (Load)
```

## 🧪 API Tests

**Target:** [JSONPlaceholder](https://jsonplaceholder.typicode.com) (fake REST API) – easily swappable for any REST API via environment variables.

- 8 integration tests covering `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- JSON schema validation, status codes, headers
- Dockerised, runs with a single command
- GitHub Actions CI runs on every push to `api-tests/`

```bash
docker build -t api-tests ./api-tests
docker run --rm api-tests
```

To run against a different API:
```bash
docker run --rm -e BASE_URL="https://your-api.example.com" api-tests
```

## 🎭 E2E Tests (Playwright)

**Target:** HAPI FHIR Patient Browser UI

- Smoke test that loads the search page, clicks **Search**, and verifies patient results appear
- Uses Playwright with Chromium (headless) inside Docker
- CI triggers automatically on changes to `e2e-tests/`

```bash
docker build -t e2e-tests ./e2e-tests
docker run --rm e2e-tests
```

## 🦗 Load Tests (Locust)

**Target:** HAPI FHIR REST API (`https://hapi.fhir.org/baseR4`)

- Simulates concurrent clinicians searching for patients
- Run headless in Docker (30s, 10 users by default)
- **Real‑world observation:** The test triggered HTTP 429 (Too Many Requests) responses, demonstrating that the server has rate‑limiting enabled – a realistic condition to account for in test planning.

```bash
docker build -t locust-tests ./load-tests
docker run --rm locust-tests
```

For interactive mode (web UI):
```bash
docker run --rm -p 8089:8089 locust-tests locust --host https://hapi.fhir.org
```

## 🔁 CI / CD

All test suites run in GitHub Actions:

- **API Tests** – triggered on changes to `api-tests/`
- **E2E Tests** – triggered on changes to `e2e-tests/`
- **Load Tests** – triggered on changes to `load-tests/`

Each workflow builds the Docker image, runs the tests, and publishes a test report (API/E2E) or prints a summary (Load).

## 💡 Key Skills Demonstrated

- REST API testing (HTTP methods, JSON schema validation)
- UI automation (Playwright, locators, auto‑waiting)
- Performance testing (Locust, concurrent users, rate‑limit awareness)
- Test containerisation (Docker, multi‑stage Dockerfiles)
- CI/CD integration (GitHub Actions, artifact publishing)
- Environment‑driven configuration (base URLs, env vars)
- Clean monorepo organisation and small, logical Git history

## 📄 Attribution

This project is a personal learning and demonstration repository built with the assistance of AI tools. All logic has been reviewed and understood by the author.

