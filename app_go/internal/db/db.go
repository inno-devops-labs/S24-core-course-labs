package db

import (
	"fmt"
	"log/slog"

	"github.com/Legolass322/example_app_go/internal/config"
	"github.com/Legolass322/example_app_go/internal/models"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Database struct {
	log *slog.Logger
	cfg *config.Config
	db  *gorm.DB
}

var database *Database

func getConnectionString(cfg *config.DatabaseConfig) string {
	return fmt.Sprintf(
		"postgresql://%v:%v@%v:%d/%v",
		cfg.Username,
		cfg.Password,
		cfg.Host,
		cfg.Port,
		cfg.DbName,
	)
}

func Init(log *slog.Logger, cfg *config.Config) (*Database, error) {
	if database != nil {
		return nil, fmt.Errorf("Database already initted")
	}

	url := getConnectionString(&cfg.DbCfg)

	db, err := gorm.Open(postgres.Open(url), &gorm.Config{})
	if err != nil {
		return nil, err
	}

	database = &Database{
		log,
		cfg,
		db,
	}

	return database, nil
}

func MustInit(log *slog.Logger, cfg *config.Config) *Database {
	db, err := Init(log, cfg)
	if err != nil {
		panic(fmt.Errorf("Could not connect to db: %v", err))
	}

	return db
}

func Get() (*Database, error) {
	if database != nil {
		return database, nil
	}
	return nil, fmt.Errorf("No db struct")
}

func (db *Database) MustAutoMigrate() {
	if err := db.db.AutoMigrate(models.Record{}); err != nil {
		panic(fmt.Errorf("Cannot migrate: %w", err))
	}
}