package main

import (
	"encoding/json"
	"io/ioutil"
	"net/http"
)

type fact struct {
	Fact string `json:"fact"`
	// `length` field is ignored
}

func catFact() (string, error) {
	resp, err := http.Get("https://catfact.ninja/fact")
	if err != nil {
		return "", err
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	var fact fact
	err = json.Unmarshal(body, &fact)

	return fact.Fact, err
}
