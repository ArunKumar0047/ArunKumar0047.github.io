# Personal Website and Blog

A clean, responsive, and easily customizable personal website and blog built with Pelican. This project serves as a template for anyone looking to create their own static site with a professional look and a light/dark theme toggle.

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Running Locally](#running-locally)
- [Customization](#customization)
  - [Site-wide Configuration](#site-wide-configuration)
  - [Adding Content](#adding-content)
- [Deployment](#deployment)
- [License](#license)

---

## Features

- **Static Site Generation**: Blazing fast load times, enhanced security, and simple hosting.
- **Python-Powered**: Built with [Pelican](https://getpelican.com), a powerful static site generator in Python.
- **Responsive Design**: Looks great on desktops, tablets, and mobile devices.
- **Light/Dark Theme**: A theme toggle allows users to switch between a professional light mode and a sleek dark mode. The preference is saved locally.
- **Markdown Content**: Easily write and edit pages and blog posts using simple Markdown syntax.
- **Easy to Customize & Deploy**: Designed to be straightforward to clone, modify, and deploy on services like GitHub Pages.

---

## How It Works

This project uses Pelican to transform simple text files into a complete, ready-to-publish website.

1.  **You write content** as Markdown (`.md`) files inside the `content/` directory.
2.  **Pelican reads your content**, processes it through the templates located in the `theme/` directory, and applies the settings from `pelicanconf.py`.
3.  **It generates the final static website** (HTML, CSS, JS) in the `output/` directory.
4.  This `output/` folder is all you need to host your website.

---

## Getting Started

Follow these instructions to get a copy of this project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed:
- [Git](https://git-scm.com/)
- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/ArunKumar0047/ArunKumar0047.github.io.git
    cd ArunKumar0047.github.io
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

### Running Locally

To build the site and start a local development server that automatically reloads when you make changes:

```sh
make devserver
```

Your website will be available at `http://127.0.0.1:8000`.

---

## Customization

This template is designed for you to make it your own.

### Site-wide Configuration

Most of the important settings can be changed in `pelicanconf.py`:

- `AUTHOR`: Your name.
- `SITENAME`: The title of your website.
- `SITEURL`: Leave this blank for local development. It will be set automatically in `publishconf.py` for deployment.
- `MENUITEMS`: Edit this list to change the navigation links in the header.

### Adding Content

- **To edit pages** (like "About" or "Projects"), modify the `.md` files in the `content/pages/` directory.
- **To add a new blog post**, create a new `.md` file in `content/blog/`. Start the file with metadata like this:

  ```markdown
  Title: My New Post
  Date: YYYY-MM-DD HH:MM
  Category: MyCategory
  Tags: tag1, tag2

  Your content starts here...
  ```

---

## Deployment

To generate the final website for publishing, run:

```sh
make publish
```

This command uses the settings in `publishconf.py` to build the site with the correct production URL and feed settings. You can then deploy the contents of the `output/` directory to any static web host, such as GitHub Pages.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.