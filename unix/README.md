# UNIX

This is an interactive talk about UNIX and Python.

If you want to go through the talk, execute this command:

```bash
docker run -ti --rm davidgasquez/unix-talk:latest'
```

You can now run the commands specified in the following section.

## Outline

> Those who don't understand Unix are condemned to reinvent it, poorly.

- `1`
- Lots of people are scared of terminals but they can be really cool!
  - `matrix`, `party`, `weather`, ...
- What is a CLI?
  - Parts of a CLI (`cli`)
  - Terminal tricks: `|`, `&`, ...
    - Listing all the available commands: `compgen -c | wc -l`
  - Sample CLI: [sample.py](clis/sample.py).
    - We can now use also `$(whoami)` as the input of `--name`!
- UNIX Philosophy (`2`)
  - Lets build a CLI to get that form Wikipedia using Python
  - How to transform the [wiki script](clis/wiki.py) into the [CLI](clis/wiki.py)
  - `3`
- Why write command line programs?
  - Glue applications together
  - You don't need to write large applications
  - Easier to write and collaborate on
  - Useful to automate stuff
  - Scripts are like vampires and never die
- Cool things CLIs can do
  - Streams
    - Reddit stream: `pushshift`
    - Entity recognition on AskReddit comments: `askreddit-nlp`
  - Parallelization: `speedup`
- Practical problem solving
  - Iterative and composable. You build them interactively
  - A complicated 4 line pipeline started as a single command that was gradually refined into something that actually solves a complicated problem
- Benefits
  - Flexibility
  - Streaming
  - Parallelizing
  - Composability
- Interesting tools
  - `jq`
  - `curl`
  - `xargs`
  - many more!
- There are millions of ways to build UNIX pipelines! :)

## Resources

- [Hacker News discussion](https://news.ycombinator.com/item?id=19160659&utm_term=comment) on the [Problem solving with Unix commands article](http://vegardstikbakke.com/unix/)
