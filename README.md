<img width="1564" height="757" alt="image" src="https://github.com/user-attachments/assets/6b367588-84ca-4a58-aa63-fa6b477b82bf" />﻿# Joke-API-Webhook

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

`GET: https://joke-api-webhook-3mrl.vercel.app/`
`POST: https://joke-api-webhook-3mrl.vercel.app/moveo/joke`

## 5. JokeAPI Integration
  
* Endpoint Used: https://v2.jokeapi.dev/joke/Any
* Flags Applied: blacklistFlags=nsfw,religious,political,racist,sexist,explicit

## 6. Response Format

```
{
  "context": {},
  "responses": [
    {
      "type": "message",
      "text": "Joke text here"
    }
  ],
  "context": {}
}
```

## Testing Results

Postman was used for all endpoint testing

### Direct API Testing
`curl -X POST https://<project>.vercel.app/api/joke_api`

### Current Issue: Moveo Not Receiving Jokes
Observed Behavior:
* The webhook executes successfully
* The API returns valid responses
* The endpoint is reachable publicly
* However, jokes are not displayed on Moveo’s end

## Moveo Platform Configuration & Development

This section documents the configuration and development steps performed within the Moveo.ai platform, in order to integrate the external Joke API webhook with the AI Agent.
All steps described below are supported by screenshots, which are provided alongside this documentation as evidence of correct setup.

### Customized Intents for dialog trigger
<img width="805" height="601" alt="image" src="https://github.com/user-attachments/assets/17e2b41a-4726-4065-a605-43f337049d2b" />

### Webhook Action Setup
<img width="1564" height="757" alt="image" src="https://github.com/user-attachments/assets/c076c8b3-a6f3-4a7f-a2dc-08b571e62a96" />

### Dialog flow
<img width="339" height="430" alt="image" src="https://github.com/user-attachments/assets/175e0918-b2f7-48e8-bd84-0f884c9a008c" />

## Conclusion

✅ The webhook is correctly implemented
✅ The API is live and functional
✅ The Moveo agent is correctly configured
❌ Joke responses are not being parsed in the Moveo UI
