package models

import "gorm.io/gorm"

type Record struct {
	gorm.Model
	Text string `json:"text"`
}
