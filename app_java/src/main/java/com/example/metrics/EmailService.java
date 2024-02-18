package com.example.metrics;

import io.prometheus.client.Gauge;
import io.prometheus.client.Summary;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.stereotype.Service;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

import java.net.SocketTimeoutException;
import java.util.Date;
import java.util.Properties;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import io.micrometer.core.instrument.Counter;
import io.micrometer.core.instrument.Timer;


@Service
@PropertySource("mailing.properties")
public class EmailService {
    private final String HOST;
    private final String SERVICE_PASSWORD;
    private final String SERVICE_EMAIL;
    private final Counter successfulSmtpRequests;
    private final Counter totalSmtpRequests;
    private final Timer smtpRequestSuccessfulTimer;

    @Autowired
    public EmailService(@Value("${mailing.host}") String HOST, @Value("${mailing.password}") String SERVICE_PASSWORD,
                        @Value("${mailing.email}") String SERVICE_EMAIL, MeterRegistry registry) {
        this.HOST = HOST;
        this.SERVICE_PASSWORD = SERVICE_PASSWORD;
        this.SERVICE_EMAIL = SERVICE_EMAIL;
        successfulSmtpRequests = registry.counter("SUCCESSFUL_SMTP_REQUESTS");
        totalSmtpRequests = registry.counter("TOTAL_SMTP_REQUESTS");
        smtpRequestSuccessfulTimer = registry.timer("SMTP_SUCCESSFUL_REQUEST_DURATION");
    }

    public void sendEmail(MyMessage messageInfo, Receiver receiver) {
        String to = receiver.getEmail();
        String password = SERVICE_PASSWORD;
        String username = SERVICE_EMAIL;
        Properties prop = new Properties();
        prop.put("mail.smtp.auth", true);
        prop.put("mail.smtp.starttls.enable", "true");
        prop.put("mail.smtp.host", HOST);
        prop.put("mail.smtp.port", "587");
        prop.put("mail.smtp.timeout", "3000");

        Session session = Session.getInstance(prop, new javax.mail.Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        });

        try {
            javax.mail.Message message = new MimeMessage(session);

            message.setFrom(new InternetAddress("anonymou_threats@mail.ru"));

            message.setRecipients(Message.RecipientType.TO,
                    InternetAddress.parse(to));

            message.setSubject("Anonymous Threat");

            String content = messageInfo.getContent();
            message.setText(content);

            long startTime = new Date().getTime();
            Transport.send(message);
            long finishTime = new Date().getTime();
            smtpRequestSuccessfulTimer.record(finishTime - startTime, TimeUnit.MILLISECONDS);

            successfulSmtpRequests.increment();

        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            totalSmtpRequests.increment();
        }
    }
}