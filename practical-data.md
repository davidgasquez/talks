# Practical Data Science or Hithhiker Guide to Data

Learnings from working with data in the real world.

## Motivation

We focus too much on the 5% of the Data Science work. That is, the shiny algorithm or the new set of parameters that improved the accuracy of a Recurrent Neural Network by 0.05.
In an ideal world, that's most of the work of a Data Scientist. In the real world, that's a couple of hours.
Let's dig into the common pitfalls and what's needed to go from nothing to tuning model parameters.

## Outline

### Warning

- The talk is biased. Your milleage my vary.
- Theory != Practice. Tips shared here won't be easy to implement!
- The data landscape is evolving really fast.

### Why

- Data talks are mostly algorithm focused
- Working with data is tricky

### Kaggle Issue

- Get the CSV (web, database, peer, ...)
- Try to start using it
  - (try once per slide) errors you might get: OOM, mixed types, empty fields, ...

### The Power of Data

- With data, we can improve applying the scientific method. And... science works!
  - It gives us knowledge!
- Data makes choices clearer distinguishing the signal from the noise
- Has applications in every field, from web A/B Testing to ML in Biology
- In a SaaS company, the only way to tell how you're doing is looking at the data. In the phisical world you can see users buying or not coming to your store. Data is the main input for internet companies.

#### Data Applications

- Answering questions
- A/B Testing
- Predicting stuff; spam, churn, prices

### My Mistakes

- Getting the data was easy (Kaggle CSV)
  - Getting good data quality. The more you look into the data the more issues you spot.
- Working with data was simple
- Starting a project from the ground up could fix everything
- Data was enought
- Assuming the job was done. Pipelines need to be maintained
  - Automation works in a different way in Data Engineering

### Learnings

- KISS
- Learn many tools, approaches, technologies, frameworks
- Combine!
  - Unix

#### Science

- Reproducibility
  - Required for the scientific method
  - Required to keep you sane
  - Docker
  - Makefile
- Keep a log. Everything is an event and events don't change!
  - Version the data. VCS
- Figure out your hypothesis. Have a baseline metric for everything you want to affect
- Keep your data tidy
- Data starts and end with people
  - Focus is scarce. Lines of code are cheap. Optimize for people.

## Engineering

- Principles of data pipelines.
- Tests (Great Expectations)
- Explore and iterate quickly to learn unknowns unknowns
  - You should aim to build evolutionary Data Pipelines
  - Microservice style pipelines
- Automate. CI/CD
  - Dev environments. Docker.
  - Tests
- Keep consistent conventions
  - Linters
- Monitorize. Know the different types of failures. Errors in code, the data or in the process
- Let it crash. Some entropy is required. (forest controlled fires)

### The Future

- Streaming
- Containers (Docker)
- Serverless (AWS Lambda)
- NN Comodization (Keras)
- [Privacy Preserving AI](https://youtu.be/4zrU54VIK6k)
- Open Data (Qri)

## Quotes

- Most of the world will make decisions by either guessing or using their gut. They will be either lucky or wrong
- Theories come and go, but fundamental data always remain the same
- Data is the aggregated voice of our customers - Riley Newman, Airbnb
- To make great products, do machine learning like the great engineer you are, not like the great machine learning expert you aren’t
