package main

import "testing"

// TestCatFact tests that `catFact` loads non-empty facts
// without errors and that those facts are different
func TestCatFact(t *testing.T) {
	const TRIES = 5

	options := map[string]int{}

	for i := 0; i < TRIES; i++ {
		s, e := catFact()
		if e != nil {
			t.Fatal("Error quering a cat fact", e)
		} else if s == "" {
			t.Fatal("No error occurred but `catFact` returned" +
				"an empty string")
		}

		options[s] += 1
	}

	// Tests are repeating
	t.Logf("Out of %d cat facts, %d are unique", TRIES, len(options))
    if len(options) <= (1+TRIES)/2 {
		t.FailNow()
	}
}
