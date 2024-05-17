locals {
  instances = [
    for instance in var.instances : merge(
      instance,
      merge({
        metadata = merge(
          can(instance.metadata) ? instance.metadata : {},
          {
            user-data = coalesce(
              can(instance.metadata.user-data) ? instance.metadata.user-data : null,
              file("${path.root}/data/user-metadata.secret.yaml"),
              var.default_user-data,
            )
          }
        )
      }),
      { boot_disk = merge(instance.boot_disk, {
        initialize_params = merge(var.default_disk_initialize_params, instance.boot_disk.initialize_params)
      }) },
      { network_interface = merge(instance.network_interface, {
        subnet_id = coalesce(instance.network_interface.subnet_id, var.default_subnet_id)
      }) },
      { scheduling_policy = merge({ preemptible = null }, instance.scheduling_policy) },
    )
  ]
}
