# Broken by Reddit ~~Greed~~ Changes to the API

## Daily Programmer

A program to download a challenge from reddit.com/r/dailyprogrammer and then output it to stdout to be used in various editors/ides

Inspired by [what-to-code](https://github.com/joereynolds/what-to-code) 

## Installation

```
pip install dailyprogrammer
```

## Usage
```
# Downloads challenge #200, the easy one
> dp 200 easy

# Downloads all variants of challenge #200 (easy, intermediate, hard)
> dp 200

# Downloads all easy challenges
> dp easy

```


## Todo

- better search query (the current one searches all numbers on the title)
- bypass reddit 100 posts limit on the api
