# Kubernetes Homework

Приложение состоит из двух компонентов:

- Backend - Python Flask, 2 реплики.
- Frontend - Python Flask, 1 реплика.

Frontend принимает HTTP-запросы и перенаправляет их
на backend через Kubernetes Service.

Для оркестрации используется Kubernetes (Minikube).

## Структура проекта

- backend/ - исходный код и Dockerfile backend.
- frontend/ - исходный код и Dockerfile frontend.
- k8s/ - Kubernetes Deployment и Service YAML.

## Требования

- Docker Desktop
- Minikube
- kubectl

## Запуск

Запустить Docker Desktop.

Создать локальный Kubernetes-кластер:

    minikube start --driver=docker

Собрать Docker-образы:

    docker build -t homework-backend:v1 ./backend
    docker build -t homework-frontend:v1 ./frontend

Загрузить образы в Minikube:

    minikube image load homework-backend:v1
    minikube image load homework-frontend:v1

Развернуть приложение:

    kubectl apply -f k8s/

Проверить состояние:

    kubectl get deployments
    kubectl get pods
    kubectl get services

## Доступ к приложению

В отдельном терминале выполнить:

    minikube tunnel

Открыть в браузере:

    http://127.0.0.1:8080

## Проверка самовосстановления

Посмотреть список Pod:

    kubectl get pods

Удалить один из backend Pod:

    kubectl delete pod ИМЯ_BACKEND_POD

Повторно проверить:

    kubectl get pods

## Остановка

Остановить minikube tunnel с помощью Ctrl+C.

Остановить кластер:

    minikube stop

Для повторного запуска:

    minikube start --driver=docker
