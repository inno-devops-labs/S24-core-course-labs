# Moscow timezone time web application

The document provide brief explanation of best practices applied in GoLang application developing. It explains such topics as coding standards, "hand" testing, and ensuring code quality.

## HTTP handler usability

There is no need to use any Framework to get a ability to run a server. GoLang provide some functional for it such that HTTP handler. By using library time we can get a time in Moscow timezone.

### Best practices applied

- To ensure code quality was used as a formatter which is follows `Google` standarts;
- The application was tested by hands. It displays the correct time in correct format updates upon page refreshing;
- Only proper libraries was used to develop this app to avoid displaying incorrect format of time.
