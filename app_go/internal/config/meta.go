package config

type Meta map[string]Config

type ConfigUpdater func(Config) Config

var metaCfg *Meta = nil

func newMeta() *Meta {
	cfg := make(Meta)
	for _, env := range []Env{Local, Testing, Production} {
		islice := env
		cfg[islice.String()] = Config{}
	}
	return &cfg
}

func getMeta() *Meta {
	if metaCfg == nil {
		metaCfg = newMeta()
	}
	return metaCfg
}

func (mcfg *Meta) SetSlice(islice Env, cfg Config) *Meta {
	(*mcfg)[islice.String()] = cfg
	return mcfg
}

func (mcfg *Meta) InheritSlice(to Env, from Env, updater ConfigUpdater) *Meta {
	(*mcfg)[to.String()] = updater((*mcfg)[from.String()])
	return mcfg
}

func (mcfg *Meta) getConfig(islice Env) Config {
	return (*mcfg)[islice.String()]
}
