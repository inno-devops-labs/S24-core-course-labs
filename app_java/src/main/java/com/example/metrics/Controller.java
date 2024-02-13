package com.example.metrics;

import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.*;

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
}
