const assert = require('assert');
const request = require('supertest');
const app = require('./app');

describe('GET /', function () {
    it('responds with HTML containing the current time in Damascus', function (done) {
        request(app)
            .get('/')
            .expect('Content-Type', /html/)
            .expect(200) // Verify that the endpoint returns a status code of 200 (OK)
            .end(function (err, res) {
                if (err) return done(err);
                // Verify the correct text outputted
                assert.ok(res.text.includes('The current time in Damascus, Syria:'));
                done();
            });
    });
});
