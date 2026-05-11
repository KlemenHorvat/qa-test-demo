# API Testing Demo

A containerised API testing project using **pytest** and **Docker**, with CI via GitHub Actions.

This repo demonstrates:
- Automated REST API tests (HTTP methods, status codes, JSON schema validation)
- Test execution in a reproducible Docker container
- Continuous integration pipeline that runs tests on every push

## Tested API

The tests target the free [JSONPlaceholder](https://jsonplaceholder.typicode.com) REST API.

## Running Tests Locally (with Docker)

```bash
# Build the Docker image
docker build -t api-tests .

# Run the tests
docker run --rm api-tests
