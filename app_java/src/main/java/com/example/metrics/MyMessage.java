package com.example.metrics;

public final class MyMessage {
    private final String alias;
    private final String content;


    public MyMessage(String alias, String content) {
        this.alias = alias;
        this.content = content;
    }

    public String getAlias() {
        return alias;
    }

    public String getContent() {
        return content;
    }
}
