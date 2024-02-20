# Lab1 (extra) Go web application for time

## Overview

This app displays cute kitten from imgur.

## Installation

### Prerequisites

- Go

### Installation steps

- Clone the repository

 ```bash
 git clone git@github.com:y4cer/S24-core-course-labs.git
 ```

- Navigate to the application directory

```bash
cd S24-core-course-labs/app_go
```

- Build the application

 ```bash
 go build
 ```

## Usage

1. `./webapp`
2. Open the `http://127.0.0.1:8080/` in browser to see cure kitty!!

## Docker

You can either build the image by yourself by:
- Navigate to the application directory

```bash
cd S24-core-course-labs/app_go
```

- Build the image

```bash
docker build -t <tag_here> .
```

- Run the image

```bash
docker run <tag_here>
```
