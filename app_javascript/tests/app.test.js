const request = require("supertest");
const app = require("../app"); // Assuming your Express app is in a file named app.js

describe("GET /", () => {
  // Test case 1
  it("should return the current time in Moscow", async () => {
    const response = await request(app).get("/");
    expect(response.status).toBe(200);
    expect(response.text).toMatch(
      /The current time in Moscow is: \d{2}.\d{2}.\d{4}, \d{2}:\d{2}.\d{2}/gm,
    );
  });
});
