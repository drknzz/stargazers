# stargazers
⭐Display the latest STARGAZERS of your repository ⭐

<!-- stargazers -->
<!-- stargazers -->

# Usage

Use this action as you would any other action.

## Required file structure
```
repository_root/
├─ .github/
│  ├─ workflows/
│  │  ├─ action.yml
├─ README.md
```

## Example usage
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
