package db

import "github.com/Legolass322/example_app_go/internal/models"

func (db *Database) AddRecord(text string) error {
	const op = "db.record.AddRecord"

	var record models.Record
	record.Text = text

	if result := db.db.Create(&record); result.Error != nil {
		return result.Error
	}

	return nil
}

func (db *Database) ListRecords() ([]models.Record, error) {
	const op = "db.record.ListRecords"

	var records []models.Record

	if result := db.db.Find(&records); result.Error != nil {
		return nil, result.Error // todo: custom error
	}

	return records, nil
}
