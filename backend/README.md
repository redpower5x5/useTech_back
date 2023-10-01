# Figma Code Generator with FastAPI Backend

This project provides a FastAPI backend that can generate code from Figma designs. By leveraging the power of FastAPI and Figma's API, you can seamlessly transform your design prototypes into usable code.

## Features

- **FastAPI Backend**: A robust and fast backend framework for building APIs.
- **Code Generation**: Transforms Figma designs into usable code.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- OpenAI API token

## Setup

1. **Environment Variables**: Before starting the service, you need to set up your environment variables. Rename the `.env.example` to `.env` and fill in the necessary details, especially your Figma API token.

    ```bash
    cp .env.example .env
    ```

    Then, edit the `.env` file:

    ```env
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

2. **Docker Compose**: To run the service, navigate to the project directory and use Docker Compose.

    ```bash
    docker compose up
    ```

    This will build the necessary Docker images and start the FastAPI server. Once the server is up and running, you can access the API at `http://localhost:8000/docs`.



## API Endpoints

- `POST /compile`: creates ready for deploy project from given parsed code from figma design. returns generated project id.
- `GET /dwnload/{uuid}`: downloads project by its generated id.


MISIS IWCD 2023