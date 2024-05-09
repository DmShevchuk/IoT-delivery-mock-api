# IoT: Mock-api сервисов доставки

## Ozon

```commandline
cd ozon
```

```commandline
docker build -t ozon_image .
```

```commandline
docker run -d --name ozon -p 5000:80 ozon_image
```


## Самокат

```commandline
cd samokat
```

```commandline
docker build -t samokat_image .
```

```commandline
docker run -d --name samokat -p 5001:80 samokat_image
```


## Яндекс

```commandline
cd yandex
```

```commandline
docker build -t yandex_image .
```

```commandline
docker run -d --name yandex -p 5002:80 yandex_image
```

## Сбер

```commandline
cd sber
```

```commandline
docker build -t sber_image .
```

```commandline
docker run -d --name sber -p 5003:80 sber_image
```


## Взаимодействие

- Для запросов: ```http://localhost:{номер_порта}/{название_сервиса}/api/v1/products/```
- Swagger: ```http://localhost:{номер_порта}/docs#/```
- Запустить из IDE: ```fastapi dev main.py```
