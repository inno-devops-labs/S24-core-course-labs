package config

import (
	"time"

	"github.com/spf13/viper"
)

func MustNewConfig() *Config {
	viper.BindEnv("DB_HOST")
	viper.SetConfigFile(".env")
	viper.ReadInConfig()

	env := fromString(viper.GetString("ENV"))

	metaSetter := func(meta MetaProvider) {
		meta.SetSlice(Production, Config{
			Env: Production,
			DbCfg: DatabaseConfig{
				Host:     viper.GetString("DB_HOST"),
				Port:     5432,
				Username: viper.GetString("POSTGRES_USER"),
				Password: viper.GetString("POSTGRES_PASSWORD"),
				DbName:   viper.GetString("POSTGRES_DB"),
			},
			ServerCfg: ServerConfig{
				Host:                viper.GetString("SERVER_HOST"),
				Port:                viper.GetInt("SERVER_PORT"),
				Timeout:             5 * time.Second,
				GracefulStopTimeout: 10 * time.Second,
			},
		}).InheritSlice(
			Testing,
			Production,
			func(c Config) Config {
				c.Env = Testing
				return c
			},
		).InheritSlice(
			Local,
			Testing,
			func(c Config) Config {
				c.Env = Local
				c.ServerCfg.Timeout = time.Second
				c.ServerCfg.GracefulStopTimeout = 2 * time.Second
				return c
			},
		)
	}

	cfg, err := New(env, metaSetter)

	if err != nil {
		panic(err)
	}

	return cfg
}
