const request = require("supertest");
const app = require("../app"); // Assuming your Express app is in a file named app.js

describe("GET /", () => {
    // Test case 1
    it("should return the current time in Moscow", async () => {
        const response = await request(app).get("/");
        expect(response.status).toBe(200);
        console.log(response.text);

    });
});