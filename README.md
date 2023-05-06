# Diamond-and-Tofu

## 1. Introduction

This is a project for our talktalk forum. We are going to use Django to build a website for our forum. The website will have a login system, a forum system, a comment system, and a search system. The website will also have a Postgres database to store the information of the users and the posts. The website will be deployed on Docker.

## 2. Run the project

### 2.1. Install Docker

Please follow the instructions on the official website to install Docker on your computer.

### 2.2. Build the image

Open the terminal and go to the directory of the project. Then run the following command to build the image:

```bash
docker-compose up --build
```

### 2.3. Run the container

After the image is built, run the following command to run the container:

```bash
docker-compose up
```

### 2.4. Access the website

Open your browser and go to the following address:

```bash
http://0.0.0.0:8000/
```

