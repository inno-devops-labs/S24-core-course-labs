import { expect, test } from "bun:test";
import { returnTime, returnTzTime } from "./utils.ts";

// Test returnTime has returnTzTime("Europe/Moscow") in it
test("returnTime has current Europe/Moscow time in it.", () => {
  expect(returnTime().toString()).toContain(
    returnTzTime("Europe/Moscow").toString(),
  );
});

// Test returnTzTime("Europe/Moscow") is same as returnTzTime("Europe/Istanbul")
test("Europe/Moscow and Europe/Istanbul time is same.", () => {
  expect(returnTzTime("Europe/Moscow")).toBe(returnTzTime("Europe/Istanbul"));
});

// Test returnTzTime("Europe/Moscow") is different from returnTzTime("Asia/Tokyo")
test("Europe/Moscow and Asia/Tokyo time is different.", () => {
  expect(returnTzTime("Europe/Moscow")).not.toBe(returnTzTime("Asia/Tokyo"));
});
