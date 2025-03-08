# Production Cockpit With ODMANTIC

This is a sample project to test [odmantic](https://art049.github.io/odmantic/) library with [FastAPI](https://fastapi.tiangolo.com/) to build a backend app for a machine monitoring. 

>**Warning:** This is just an example to play with the libraries, do not use in a production environment. 

## What is Odmantic?🤷‍♂️

It is an Object Document Mapper (ODM) to interact with MongoDB, which uses the yet powerful library [Pydantic](https://docs.pydantic.dev/latest/) as a validation layer.

## Production Cockpit 🏭

With this sample app you could store and retrieve metrcs from machines in the producction floor of any industry.

### Data structure ⛩️ 

For the purpouse of this app, i've created 3 entities; Machine, Probe and Metric.

<img src="/docs/assets/entities.png" width="500" alt="data structure">

#### Machine 🤖

Abstraction for the context where the measurements come from, for example `robot01`. This entity will have one to many [probes](#probe-️) with its metrics. 

**Attributes**

|Name|Description|Data type|Default|Optional|
|:----|:----:|:----:|:----:|:----:|
|name|The name of the machine|`string`|`None`|`False`|
|reference|Optionally we can introduce a references, for example the serial name|`string`|`None`|`True`|


#### Probe 🌡️

This entity will store all metrics from a specific point. Using the same example, in `robot01` we can create the probe `resolver_axis01_temperature` to store the metrics of this element. 

**Attributes**

|Name|Description|Data type|Default|Optional|
|:----|:----:|:----:|:----:|:----:|
|machine_id|The id of the machine this probe belobngs to|`ObjectId`|`None`|`False`|
|name|Name of the probe|`string`|`None`|`False`|
|units|Measurement units of the metrics it will store, for example ºC for temperature|`string`|`None`|`True`|
|severity|Impact of this metrics on the global context|`string`|`low`|`True`|
|description|Short description |`string`|`None`|`True`|


#### Metric 📈

A measurement for a specific [probe](#probe-️)

**Attributes**

|Name|Description|Data type|Default|Optional|
|:----|:----:|:----:|:----:|:----:|
|probe_name|The name of the probe this metric belongs to|`string`|`None`|`False`|
|value|Amount |`string`|`float`|`int`|`None`|`True`|


## Install dependencies 📦

You can run this project locally on your pc, the most easy way to do it is using docker to set up a mongodb instance locally.

```
docker run -d --name mongodb -p 27017:27017 mongodb/mongodb-community-server
```



Now you have a mongoDB running locally on your machine. To get the code, clone the repo:
```
git clone git@github.com:jmpulo/production-cockpit.git
```


Navigate to the backend folder:

```
cd backend
```


You will need the python dependencies to run the code. The most recomended way is to use a virtual env with `venv` or `conda`. I will use venv:

```
python3 -m venv venv
```

Activate the virtualenv 

```
source venv/bin/activate
```

Install the dependencies 📦

```
pip install -r requirements.txt
```


## Run it 🚀

Once you have set all the [dependencies](#install-dependencies-) yo can run it. Go to the folder `/backend/app`. If you come from the previous step, just run `cd app`.

Now run:

```
fastapi dev main.py
```

You should see this output in your terminal


<img src="/docs/assets/fastapi_init.png" width="500" alt="FastAPI init">

Now you can navigate to [localhost:8000/docs](http://localhost:8000/docs) and you should be able to interact with your app using swagger.

<img src="/docs/assets/swagger_general.png" width="500" alt="swagger">

