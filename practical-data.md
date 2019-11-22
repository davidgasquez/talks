# Practical Data Science

Failures and learnings from my time in the data world.

## Motivation

People talk about their shiny new algorithm or how much a new set of parameters improved the accuracy of a complex Neural Network.
I'd say that's the easy part about working with data.
This talk focus on the rest of the work needed to tune the parameters.

## Outline

### Warning

- The talk is biased from my experience.
- Theory != Practice. Tips shared here won't be easy to implement!
- The data landscape is evolving really fast.

### Why

- Data talks are mostly algorithm focused
- Working with data is tricky
- I made some mistakes I want to share

#### Kaggle Issue

- Get the CSV (web, database, peer, ...)
- Try to start using it
  - (try once per slide) errors you might get: OOM, mixed types, empty fields, ...

### The Power of Data

- With data, we can improve applying the scientific method. And... science works!
  - It gives us knowledge!
- Data makes choices clearer distinguishing the signal from the noise
- Has applications in every field, from web A/B Testing to ML in Biology
- In a SaaS company, the only way to tell how you're doing is looking at the data. In the phisical world you can see users buying or not coming to your store. Data is the main input for internet companies.

### Data Applications

- Answering questions
- A/B Testing
- Predicting stuff; spam, churn, prices

### My Mistakes

- Getting the data was easy (Kaggle CSV)
- Working with data was simple
- Starting a project from the ground up could fix everything
- Data was enought
- Assuming the job was done. Pipelines need to be maintained
  - Automation works in a different way in Data Engineering

### Learnings

- Reproducibility
  - Required for the scientific method
  - Required to keep you sane
- Everything is an event and events dont change!
- Learn many tools
- Combine the tools!
  - Unix Slide
- KISS
- Have a baseline metric for everything you want to affect
- Keep your data tidy
- Explore and iterate quickly to learn unknowns unknowns
  - e.g normalizing the variables. If you don't you'll have a ranking!
  - You should aim to build evolutionary Data Pipelines
- Let it crash. Some entropy is required. (forest controlled fires)
- Monitorize. Know the different types of failures. Errors in code, the data or in the process
- Data starts and end with people
  - Focus is scarce. Lines of code are cheap. Optimize for people.
- Keep consistent conventions

### The Future

- Streaming
- Containers
- Serverless
- NN

## Quotes

- Most of the world will make decisions by either guessing or using their gut. They will be either lucky or wrong
- Theories come and go, but fundamental data always remain the same
- Data is the aggregated voice of our customers - Riley Newman, Airbnb
- To make great products, do machine learning like the great engineer you are, not like the great machine learning expert you aren’t