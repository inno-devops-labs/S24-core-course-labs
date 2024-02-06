package ru.innopolis.demo

import org.junit.jupiter.api.Test
import org.springframework.boot.test.context.SpringBootTest
import org.junit.jupiter.api.Assertions.assertEquals;
import ru.innopolis.demo.controller.TimeController

@SpringBootTest
class AppKotlinApplicationTests {
	val controller = TimeController()
	@Test
	fun getCurrentTime() {
		assertEquals(controller.getCurrentTime().substring(0, 23), "Current time in Moscow ")
	}

}
