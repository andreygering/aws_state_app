### How to execute the docker file.

Please build the docker and choose the version:
example: 
```
docker build -t aws_app_run:v-<number of version> <path/to/project/folder>project
```

Please run the docker-compose file:
```
docker-compose up -d
```

Please run the docker file:

example: docker run -itd --name aws_state_app_<number of version> -v "$(pwd)":/usr/src/app aws_app_run:v-<number of version> python aws_instanses


EXAMPLE with parameters: 
```
docker build -t aws_app_run:v-0.1.0.1 /home/andrey/git/CarticaDevOps/.drafts/JB/project
```
```
docker run -itd --name aws_state_app_0_1_0_1 -v "$(pwd)":/usr/src/app aws_app_run:v-0.1.0.1 python aws_instanses
```


Please put quor AWS credentials in file .env
example: 
KEY_ID=<ID>
ACCESS_KEY=<KEY>




At the end of the program execution you will receive instance_log_file.json file with logs.
