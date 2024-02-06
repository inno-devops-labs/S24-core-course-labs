## Framework Justification:

The project was developed with Node.js and Express.js. I chose this stack because it is very easy to work with and lightweight.

## Best Practices and Coding Standards:

### Modular Structure:

- The application is organized with a modular structure, promoting clarity and ease of maintenance.
- Key components are separated into distinct folders: `test` for testing, `views` for view templates, and `app.js` for main application logic.

### Separation of Concerns:

- Express.js is used to maintain a clear separation of concerns within the application.
- Route definitions are in `app.js`, and views are stored in the `views` folder, contributing to code readability and maintainability.

### Version Control:

- A well-crafted `.gitignore` file demonstrates adherence to version control best practices.
- Helps manage versioned files and directories efficiently.

### Dependencies:

- The `package.json` file specifies the essential Node.js packages required for the app, streamlining the installation process.

### Documentation:

- A comprehensive `README.md` that contains instructions on setting up, running the project, and running tests.
- The `README.md` also contains images. 

## Testing and Code Quality:

### Unit Testing:

- Unit tests, in the `test` folder, specifically for testing the routes and functionality of the app.

### Code Comments:

- Code contains descriptive comments, enhancing readability and providing clear documentation for each component.