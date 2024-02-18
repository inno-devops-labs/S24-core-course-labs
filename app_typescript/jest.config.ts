export default {
  preset: "ts-jest",
  testEnvironment: "jest-environment-jsdom",
  transform: {
    "^.+\\.tsx?$": "ts-jest",
  },
  moduleNameMapper: {
    "\\.(gif|ttf|eot|svg|png|css)$":
      "<rootDir>/src/tests/__mocks__/fileMock.js",
    "^@app/(.*)$": "<rootDir>/$1",
  },
};
