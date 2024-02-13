package com.example.metrics;

import java.util.Objects;

public final class Receiver {
    private final String alias;
    private final String email;

    public Receiver(String alias, String email) {
        this.alias = alias;
        this.email = email;
    }

    public String getAlias() {
        return alias;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Receiver user)) return false;
        return Objects.equals(getAlias(), user.getAlias()) && Objects.equals(getEmail(), user.getEmail());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getAlias(), getEmail());
    }
}
