package main_test

import (
	main "app_golang"
	"testing"
)

func TestAbs(t *testing.T) {
	got := main.One()
	if got != 1 {
		t.Errorf("Abs(-1) = %d; want 1", got)
	}
}
