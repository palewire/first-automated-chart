# Contributing

How to propose changes to this repository.

Fork the repository and clone it:

```bash
gh repo clone your-name/first-automated-chart
```

Change into the project directory:

```bash
cd first-automated-chart
```

Install the dependencies using pipenv:

```bash
pipenv install
```

To start a test server the previews the site, use the following commands

```bash
cd docs
pipenv run make livehtml
```

Once it starts, visit [localhost:8000](http://localhost:8000) in your browser. Edits made in the `docs/` folder will appear soon after being pushed to GitHub.

You should commit your changes to a branch and then submit a pull request to the source repository. You can learn how in the class ["First Pull Request"](https://palewi.re/docs/first-pull-request/index.html)
