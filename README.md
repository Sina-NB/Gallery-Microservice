
<h1 align="center">Gallery-Microservice</h1>
<p align="center">
  <img src="./Images/Arch.png" width=400>
</p>
<p><br></p>
A Simple Gallery app implemented with microservice architecture.

### Overview
- [Features](#features)
- [MicroServices](#microservices)
- [Getting ready](#getting-ready)
- [Bugs or Opinion](#bugs-or-opinion)

### Features
- MicroService
- Class Based
- Broker(RabbitMQ)
- REACT
- linting tools
- Dockerize

### MicroServices
| Name | Responsibility |
| --- | --- |
| Admin | CRUD Operations |
| Main | Like and List Photos |

### Getting ready
Change directory to `FrontEnd` and install REACT app dependecies.
```bash
npm install
```
Change directory to `Backend` and build docker images.
```bash
docker compose build
```
Run backend server.
```bash
docker compose up
```
Change directory to `FrontEnd` and Run FrontEnd server.
```bash
npm start
```
### Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo.
