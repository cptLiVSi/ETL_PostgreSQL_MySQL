# Solution for Test task for Data Engineering Internship

Language used: python ver 3.10.6

## To run the project
WIN:
```
docker-compose -f .\task\docker_compose\docker-compose.yml up -d
```
macOS/Linux:
```
docker-compose -f ./task/docker_compose/docker-compose.yml up -d
```

## Logic and Structure

3 containers are being created on start:
```
* minio
* minio-create-bucket
* shylovapp
```

* shylovpp contains the project, keeps the port 8080 and starts the run.sh
* run.sh installs requirements and runs flask at port 8080
* flask is implemented in app.py
* app.py uses 2 scripts in .\logic
* minio_processor.py and csv_processor.py
* variables are stored in data.py


* minio_processor.py contains class MinioProcessor which implements connection and data exchange with Minio.
* sv_processor.py contains class CsvProcessor which processes csv and filters.
* these classes are used by function sensor() in app.py which provides the service.


# Working process
This service processes input data to Minio (http://localhost:9001/) to "sourcedata" bucket.
The output.csv is put to "datalake" bucket in folder "processed_data".
This happens on start and autoupdate occurs every 500 seconds.
Also, database can be reached at http://localhost:8080/data. Filters are implemented
via ? and **kwargs is_image_exists=True/False, min_age, max_age after the address.

E.g. to get all data of persons from 20 to 29 without image, the request should be:

* http://localhost:8080/data?min_age=20&max_age=29&is_image_exists=False

(position of filters doesn't matter)

With same logic filters can be applied to calculation of average age (e.g. of users with image and 35 or more y.o.):

* http://localhost:8080/stats?is_image_exists=True&min_age=35

`Only full years are calculated for users, and used to get average age, which is rounded`

POST request to http://localhost:8080/data triggers update of DB.
