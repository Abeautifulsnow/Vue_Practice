# user-system

> A simple application built with VUE.

## Use Intro

### 1、json-server

#### 1.1 Intro

Get a full fake REST API with zero coding in less than 30 seconds (seriously).
We can go to [getting-started](https://github.com/typicode/json-server#getting-started) for further reference.

#### 1.2 How to use json-server

* Install json-server global: ```sudo npm install -g json-server```(or use ```sudo cnpm install -g json-server```)
* Install json-server local: ```npm(cnpm) install json-server --save```
* Create a ```db.json``` with some data
* Initialize a ```package.json``` file via ```npm(cnpm) init``` in your project root directory and customize it by referring to my ```package.json``` configuration.

```json
...
"scripts": {
    "json:server": "json-server --watch db.json",   // customize start-scripts
    "json:server:remote": "json-server http://jsonplaceholder.typicode.com/db"
  },
...
```

* Start json-server service: ```(npm)cnpm run json:server```, and now we can go to http://localhost:3000/users to get data by chrome.

### 2、user-back-system

#### How to do

Suppose you have ```vue-cli```、```webpack```、```node.js``` installed.

```bash
vue-init webpack project-name
cd project-name
npm(cnpm) install
npm(cnpm) install vue-resource
npm(cnpm) run dev
```

Next, we will improve the rest functional development of this vue project.

### 3、Run

* Start these two services separately.

```bash
cnpm run json:server
cnpm run dev
```

## Reference

* [jsonplaceholder](http://jsonplaceholder.typicode.com/)
* [json-server](https://github.com/typicode/json-server)
* [bootstrap3](https://v3.bootcss.com/)
