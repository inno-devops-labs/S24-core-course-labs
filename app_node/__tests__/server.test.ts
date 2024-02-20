import request from 'supertest';
import app from '../src/server';

describe('GET /currentTime', () => {
  it('responds with the current time in GMT+3 timezone', async () => {
    const response = await request(app).get('/currentTime');
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('currentTime');
    const currentTime = new Date(response.body.currentTime);
    expect(currentTime.getTime()).toBeGreaterThan(0);
  });
});

afterAll(async () => {
  // Stop the server after all tests are completed
  await app.close();
});
