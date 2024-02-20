package ru.dmfrpro.app;

import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

class ControllerTest {

    @Test
    void testAvailability() {
        var controller = new Controller();
        var modelAndView = controller.index();
        assertNotNull(modelAndView, "ModelAndView should not be null");
    }

    @Test
    public void testHtml() {
        var controller = new Controller();
        var modelAndView = controller.index();
        var htmlContent = modelAndView.getViewName();
        assertEquals("index", htmlContent);
    }

    @Test
    public void testTime() {
        var controller = new Controller();
        var modelAndView = controller.index();

        String actualCurrentTime = (String) modelAndView
                .getModel()
                .getOrDefault("currentTime", "");

        var moscowZone = ZoneId.of("Europe/Samara");
        var currentTime = LocalDateTime.now(moscowZone);
        var formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        var time = currentTime.format(formatter);

        assertEquals(time, actualCurrentTime);
    }
}
