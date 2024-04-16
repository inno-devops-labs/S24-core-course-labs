package com.example.metrics;

import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import java.util.ArrayList;
import java.util.Map;
import java.util.concurrent.TimeoutException;

@RestController
@RequestMapping(path = "/api")
public class Controller {
    private final Service service;

    @Autowired
    public Controller(Service service) {
        this.service = service;
    }

    @PostMapping("/receivers")
    public void createUser(@RequestBody Receiver receiver) {
        service.createReceiver(receiver);
    }

    @PostMapping("/messages")
    public void sendMessage(@RequestBody MyMessage message) throws TimeoutException {
        service.sendMessage(message);
    }

    @GetMapping("/messages")
    public ArrayList<String> getMessages(String alias) {
        return service.getMessages(alias);
    }

    @GetMapping("/persist")
    public String getLast(String newValue) {
        String filePath = "persist/file.txt";
        StringBuilder content = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(newValue);
        } catch (IOException e) {
            e.printStackTrace();
        }

        return content.toString();
    } 
}
