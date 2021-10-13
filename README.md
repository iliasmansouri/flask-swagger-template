<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

A REST API template for ML-based applications.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Docker](https://www.docker.com)
- [Connexion](https://github.com/zalando/connexion)
- [Swagger](https://swagger.io/)
- [Gunicorn](https://gunicorn.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

Make sure to use a Python 3.6 environment:

```sh
  conda create -n swagger python=3.6
```

### Installation

Make sure to run the commands below from the root of this cloned repo:

1. ```sh
   pip install -r front_end/requirements.txt
   ```

2. ```sh
   docker build -t "swagger-ui" -f back_end/Dockerfile .
   ```

3. ```sh
   docker run -p 8296:8296 swagger-ui
   ```

4. ```sh
   streamlit run main.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Ilias Mansouri - [@LinkedIn](https://www.linkedin.com/in/ilias-mansouri/)

<p align="right">(<a href="#top">back to top</a>)</p>
```
````
