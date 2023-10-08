folder `ml`:

The model is trained here. This part will be deployed later.

build the image:

`sudo docker build -t housingpricepred:latest .`

create and run the container with:

`sudo docker run --rm -it -v /home/xichuz/workspace/housing-price-predict/ml:/app --name my_container housingpricepred:latest /bin/bash`

Python code outside `ml`:

Collects data and store in MySQL database