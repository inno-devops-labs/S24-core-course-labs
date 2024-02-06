# Reasoning behind the CSharp app

## Note

I realized too late that I was supposed to use creativity for the bonus part. As you can see, I recreated the main Python app in C# instead. I will hopefully diverge in future assignments.

## Framework

For this application, I chose Asp.net framework, because I have a lot of experience with it.

## Practices used

1. I decided to use commonly-used ISO 8601 format with explicit timezone specification, which should make it easier to consume the API.
2. The solution is documented via auto-generated Swagger pages
3. Project code is split into different modules in a structured manner
4. Asp.net Dependency Injection mechanism is used for easier unit-testing in the future

## Testing

For now, the testing is manual - on page refresh the time changes to the current time in Moscow Standard Time.
