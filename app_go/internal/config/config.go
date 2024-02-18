package config

import "fmt"

type Config struct {
	Env       Env
	Version   string
	DbCfg     DatabaseConfig
	ServerCfg ServerConfig
}

var config *Config = nil

type MetaProvider interface {
	SetSlice(islice Env, cfg Config) *Meta
	InheritSlice(to Env, from Env, updater ConfigUpdater) *Meta
}

type MetaSetter func(meta MetaProvider)

type ConfigError struct {
	Env Env
}

func (e *ConfigError) Error() string {
	return fmt.Sprintf("Cannot get env: %v", e.Env.String())
}

func New(env Env, ms MetaSetter) (*Config, error) {
	if config == nil {
		meta := getMeta()
		ms(meta)
		cfg := meta.getConfig(env)
		config = &cfg
	}

	if config.Env == 0 {
		return &Config{}, &ConfigError{env}
	}

	return config, nil
}
