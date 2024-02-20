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