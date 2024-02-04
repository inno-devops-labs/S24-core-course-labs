package service

import "time"

// Clock have method to get current time (specified by nowFunc)
type Clock struct {
	nowFunc func() time.Time
}

// NewClock returns the Clock
func NewClock(nowFunc func() time.Time) *Clock {
	return &Clock{
		nowFunc: nowFunc,
	}
}

// GetCurrentTime return the current time
func (c *Clock) GetCurrentTime(location *time.Location) time.Time {
	return c.nowFunc().In(location)
}
