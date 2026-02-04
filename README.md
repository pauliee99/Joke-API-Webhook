# Joke-API-Webhook

## 1. Overview 
This project implements a serverless webhook API that delivers jokes to a Moveo AI chatbot.
The webhook is deployed on Vercel, written in Python (Flask), and fetches jokes dynamically from the public JokeAPI.  
  
The intended flow is:  
```
Moveo Chatbot
   ↓ (POST request)
Vercel Serverless Function (Flask)
   ↓
JokeAPI (external)
   ↓
Formatted response
   ↓
Moveo Chatbot displays joke
```
   
## 2. Technology Stack  

| Component       | Technology                                       |
| --------------- | ------------------------------------------------ |
| Hosting         | Vercel (Serverless Functions)                    |
| Language        | Python 3.12                                      |
| Framework       | Flask                                            |
| External API    | [https://v2.jokeapi.dev](https://v2.jokeapi.dev) |
| Bot Platform    | Moveo AI                                         |
| Deployment Type | API (serverless)                                 |

## 3. Project Structure
```
Joke-API-Webhook/
│
├── api/
│   └── joke_api.py        # Main webhook logic
│
├── requirements.txt       # Python dependencies
├── vercel.json            # Vercel configuration
└── README.md
```

## 4. API Endpoint Details

