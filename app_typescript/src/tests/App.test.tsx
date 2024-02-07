import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import App from "../App";

it("test", () => {
  const { getByText } = render(<App />);
  const curDate = new Date().toLocaleTimeString("ru-RU", {
    timeZone: "Europe/Moscow",
  });

  const date = getByText(curDate);

  expect(date).toBeDefined();
});
