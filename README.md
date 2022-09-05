![stargazersx](https://user-images.githubusercontent.com/65187002/188505313-c85dd8f1-3946-4f5a-897b-3c22288c906a.png)
#
<h2 align="center">⭐ Display the latest STARGAZERS of your repository ⭐</h2>

<br><br>

<h1 align="center">See a <a href="https://github.com/drknzz/stargazers-test/">LIVE</a> usage</h1>

<br><br>

## ▶️ Usage ▶️

### Required file structure
```
repository_root/
├─ .github/
│  ├─ workflows/
│  │  ├─ action.yml
├─ README.md
```

### Action
Copy the content below and paste it into **action.yml** inside **.github/workflows/ directory**.

```
name: stargazers

on:
  watch:
    types: [started]

jobs:
  stargazers:
    runs-on: ubuntu-latest
    steps:
      - uses: drknzz/stargazers@main
```

### Embed
To showcase the stargazers file simply put these two comments in your **README.md** file:

```
<!-- stargazers -->
<!-- stargazers -->
```
