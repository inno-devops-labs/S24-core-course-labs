## Technical Stack
As an example of the main web-framework we've used **FastAPI** for its wide popularity, easiness, well-structured 
documentation, high-performance. For realizing our main functional requirements _(i.e. getting time)_ we have used 
**datetime** (for getting actual time) with **pytz** (for setting correct timezone).

## Best practices implemented
1. All project has appropriate naming convention.
2. Pipenv.lock instead of simple requirements.txt (however, I've left a file because of assignment requirements) will help to deploy the project on the current machine without
chance of corrupts during building stage
3. PEP-8 standards in the main backend code.
4. PEP-484 (i.e type hinting)


## Testing
Because we have no complex functionality in our application, there are not many test cases. We cannot test endpoint `/`
for the reason that this just returns file, but we can test `/api/time/` for confirming that our application correctly 
retrieve current moscow time. 

### Best practices applied
1. Tests have meaningful name.
2. Appropriate creation of mock by using **fixtures**.
3. Code coverage. Our tests coverage maintains 91%.