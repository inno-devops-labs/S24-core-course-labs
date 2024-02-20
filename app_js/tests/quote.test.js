// quote.test.js
const request = require('supertest');
const app = require('../app');

describe('GET /', () => {
  it('should return a 200 OK status', () => {
    return request(app)
      .get('/')
      .expect(200);
  });

  it('should return a quote in the response', () => {
    return request(app)
      .get('/')
      .then(response => {
        expect(response.text).toMatch(/Life is about making an impact, not making an income. –Kevin Kruse|Whatever the mind of man can conceive and believe, it can achieve. –Napoleon Hill|Strive not to be a success, but rather to be of value. –Albert Einstein|Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference. –Robert Frost|The most difficult thing is the decision to act, the rest is merely tenacity. –Amelia Earhart|Every strike brings me closer to the next home run. –Babe Ruth|Definiteness of purpose is the starting point of all achievement. –W. Clement Stone|Life isn't about getting and having, it's about giving and being. –Kevin Kruse|Life is what happens to you while you’re busy making other plans. –John Lennon/);
      });
  });
});
