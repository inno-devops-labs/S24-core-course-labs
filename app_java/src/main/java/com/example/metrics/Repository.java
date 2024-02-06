package com.example.metrics;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@org.springframework.stereotype.Repository
public class Repository {
    private final Map<String, ArrayList<String>> messages;
    private final Map<String, Receiver> receivers;

    public Repository() {
        messages = new HashMap<>();
        receivers = new HashMap<>();
    }

    public void saveMessage(MyMessage message) {
        List<String> cur = messages.get(message.getAlias());
        cur.add(message.getContent());
    }

    public void createReceiver(Receiver receiver) {
        receivers.put(receiver.getAlias(), receiver);
        messages.put(receiver.getAlias(), new ArrayList<>());
    }

    public ArrayList<String> getMessages(String alias) {
        return messages.get(alias);
    }

    public Receiver getReceiver(String alias) {
        return receivers.get(alias);
    }
}
