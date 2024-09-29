# FinancialBedrock

Access to capital for minorities has historically been an unfair playing field in the states. I see the help that translation of basic concepts can provide from my upbringing translating documents for my family members. My application aims at removing some of the language barriers and lack of familarity with business concepts in hopes of increasing access to loan from traditional lending institutions for foreign speaking members of minority population.

The application uses AWS Bedrock to take the input from end user and create business plans, forecasting for future earning and provides best practices for security of PII (personal identifiable information). The generative ai service from AWS with the Titan Text Embeddings V2 language model is meant to phrase the information in clear language with the ability to ask for clarification. The front end will use a simple layout with language options for commonly under served communities by lending entities.

The front end was built JS Vanilla and the backend uses Python with the Flask framework and utilizes Boto3 to interact with the AWS services. For background information and ideas on connecting bedrock to a front end I forked the repo from mikehostetler/amplify. 

I used my work account and one of the challenges I faced was IAM permissions for AWS Bedrock to enable the site to be connected to AWS services. I have provide a view of the output from the AI service from a AWS but was not able to connect it to the front end without permission from my supervisor at work.

I am proud of my ability to configure the language model to produce a curated output and building up a knowledge base on AWS Bedrock.

I have extensive knowledge of the IAM policies required to connect the AWS Bedrock to Boto3 as a result of Shellhack.
I learned that the concept of an application that creates business plans is fairly common online with little to no consideration to non-English speaking minority populations. 

I plan to build out the bot to enable a budget and ledger to bu uploaded to the LLM and create a projection which aside from business plans is a common request of lending entities for their lendees.
I plan to present this to management at work and see if there is any interest in utilizing AWS Bedrock to up-skill workers on finance concepts. 
