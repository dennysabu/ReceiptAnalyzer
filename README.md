# Receipt Analyzer


This was a quick experiment I threw together to test the output of Azure Cognitive Services specifically with restaurant receipts. 


## Prerequisites
- Python 3.6+  (using f strings, you can reformat and use with <3.6)
- Requests library
- Azure Subscription 
     - Azure Form recognizer instance 



## Running the project

### Environment set up
When you create your Azure Form Recognizer instance, you'll get an endpoint and a key, you'll need both to make requests. 

These values will need to be passed to the <code>receipt-analysis.py</code> file. 

It's configured to use environment variables:

```python
     REQUEST_URL = os.environ['REQUEST_URL']
     KEY = os.environ['REQUEST_KEY'] 
```

You'll need to set those variables up in your environment, or edit the <code> receipt-analysis.py</code> file and hardcode your values. A quick word on security: you really should avoid hardcoding, especially if your code might end up on a public code sharing platform.

## Making the request

<code> receipt-analysis.py</code> is what will make the request and takes the file path of your receipt picture as the first and only argument.

```bash   
     python3 receipt-analysis.py [file-path]
```

If successful you'll see something like..

```bash
     Running OCR
     Loading Result...
     Waiting...
     Waiting...
     Results Loaded
```

It can take a few seconds to run as there are actually two requests, one of which can run multiple times before the results are available. 

You should have a new file called 'azure-results.json' which will have the results from Azure. 

## Getting User Friendly Data from JSON

You can use <code>process-azure-results.py</code> to print out certain information from the output of <code> receipt-analysis.py</code>.  It'll print out the address and the items that were ordered. 


```bash   
     python3 process-azure-results.py [file-path-to-your-json]
```

I only did this as a POC so there is very little (i.e. no) error checking so depending on what you get back from Azure, you're likely to run into an error. 





