# Configured Prometheus: 
![image](https://github.com/frog-da/DevOps/assets/84839431/496d89dd-7cc5-4441-a525-0476e63fe4d6)

# Dasboards screenshots:
## Loki:
![image](https://github.com/frog-da/DevOps/assets/84839431/5ac7e10c-34d1-447f-ae41-10714dc09fcc)
![image](https://github.com/frog-da/DevOps/assets/84839431/713c6906-27c8-4444-a3ec-6dcd6f868641)
![image](https://github.com/frog-da/DevOps/assets/84839431/16f1c77f-e8ed-40f7-90ac-1cbcdacc886e)

## Prometheus:
![image](https://github.com/frog-da/DevOps/assets/84839431/2de07972-f4fd-4f22-bb23-81b79bada0ce)
![image](https://github.com/frog-da/DevOps/assets/84839431/d38dc305-425d-4cc7-9122-ef47b5f8395e)
![image](https://github.com/frog-da/DevOps/assets/84839431/b8bb6098-a81a-42fb-8ccd-a2ea6ff77603)
![image](https://github.com/frog-da/DevOps/assets/84839431/5b2fce5b-7a16-42fb-b7dc-ae049aa0ec84)
![image](https://github.com/frog-da/DevOps/assets/84839431/2eb57f6b-7300-4c6b-ab54-afb651e80377)
![image](https://github.com/frog-da/DevOps/assets/84839431/8bce5200-e30f-4e81-8e4f-daa340b9d443)
![image](https://github.com/frog-da/DevOps/assets/84839431/e722837e-a13e-4ac9-a7b2-acf48f41ff92)

## Service Configuration Updates:

- Log rotation is implemented by specifying the `max-size` and `max-file` options of logging with `json-file` driver.
- Memory limits are specified by adding such field to containers:

```yaml
deploy:
  resources:
    limits:
      memory: 500M
```

that limits container memory usage to 500MB
