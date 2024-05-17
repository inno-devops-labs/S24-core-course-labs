#include <iostream>
#include <ctime>
#include "./cpp-httplib/httplib.h"

int main() {
    // Get the current time
    std::time_t current_time = std::time(nullptr);
    struct tm summer_start_date = {0};

    // Set the date when summer starts (e.g., June 21st)
    summer_start_date.tm_year = 2024 - 1900; // Year - 1900
    summer_start_date.tm_mon = 5; // June (0-based index)
    summer_start_date.tm_mday = 1;

    // Calculate the time difference
    std::time_t summer_start_time = mktime(&summer_start_date);
    std::time_t time_left = summer_start_time - current_time;

    // Initialize the HTTP server
    httplib::Server server;

    // Define an HTTP GET handler
    server.Get("/", [time_left](const httplib::Request& req, httplib::Response& res) {
        // Calculate days, hours, minutes, and seconds
        int days = time_left / (60 * 60 * 24);
        int hours = (time_left % (60 * 60 * 24)) / (60 * 60);
        int minutes = (time_left % (60 * 60)) / 60;
        int seconds = time_left % 60;

        // Generate an HTML response
        std::string response = "<html><body>";
        response += "<h1>Time Left Until Summer 2024</h1>";
        response += "<p>" + std::to_string(days) + " days, "
                  + std::to_string(hours) + " hours, "
                  + std::to_string(minutes) + " minutes, "
                  + std::to_string(seconds) + " seconds</p>";
        response += "</body></html>";

        // Set the response content type to HTML
        res.set_content(response, "text/html");
    });

    // Start the HTTP server on port 80
    server.listen("127.0.0.1", 5050);

    return 0;
}
