#COVIDTRACKER

## The spec

The following is a public API with information about COVID-19 in the US:
https://covidtracking.com/api

Using this API, create a web page that satisfies the following user story:

"As a US citizen, I would like to know how cases of COVID-19 have been changing
 over time in my State."

## Getting Started

To run this project, you need to clone it 

```
git@github.com:agata-anastazja/covidtracker.git
```
### Prerequisites

You need to have python3 installed.
Then run in your command line client 
```
pip3 install -r requirements.txt
```

### Running locally

To run locally, all you need to do is run a setup script
```$xslt
./local.sh
```

### Testing

To run locally run
```$xslt
nosetests
```

### Approach to the task
I have broken the task down and prioritised making a call to the API while hardcoding the state of California. I was 
test driving and working in small slices to satisfy expected user need.

### Given more time
The next steps would be as follows:
* error handling for when the api call goes wrong
* logging for api call
* provided the users with more stats about the state of California
* provided the users with the option to choose which state's stats they can see
* made it more user friendly with React frontend replacing jinja templates

