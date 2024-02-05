package com.example.app_java;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RouteController {

    private int accessCount = 0;

    @GetMapping("/route")
    public String getRoute() {
        accessCount++;
        return "Route accessed " + accessCount + " times.";
    }
}