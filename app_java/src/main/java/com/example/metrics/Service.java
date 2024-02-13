package com.example.metrics;

import org.springframework.beans.factory.annotation.Autowired;

import java.util.ArrayList;
import java.util.concurrent.TimeoutException;

@org.springframework.stereotype.Service
public class Service {
    private final Repository repo;
    private final EmailService emailService;

    @Autowired
    public Service(Repository repo, EmailService emailService) {
        this.repo = repo;
        this.emailService = emailService;
    }

    public void sendMessage(MyMessage message) throws TimeoutException {
        repo.saveMessage(message);
        emailService.sendEmail(message, repo.getReceiver(message.getAlias()));
    }

    public ArrayList<String> getMessages(String alias) {
        return repo.getMessages(alias);
    }

    public void createReceiver(Receiver receiver) {
        repo.createReceiver(receiver);
    }
}
