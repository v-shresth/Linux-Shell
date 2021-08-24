# Linux Shell on Browser

For making this project we have used Bootstrap and some own HTML, CSS on frontend and Python at backend and we have used Django Framework

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary python libraries.

```bash
yum install python3
pip install django
pip install subprocess
```

## Usage

It takes the command from browser using POST request analyze the command via subprocess and return Output.

```python
import subprocess

command = request.POST.get("cmd", default)
command = subprocess.getoutput(command)
```
