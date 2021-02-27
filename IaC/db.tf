module "db" {
  source           = "./modules/postgresql/modules/postgresql"
  db_name          = var.db_name
  database_version = var.database_version
  name             = "${var.project}-dashboard-sample1"
  region           = var.region
  zone             = var.zone
  project_id       = var.project

  ip_configuration = var.ip_configuration

  module_depends_on = [google_service_networking_connection.private_vpc_connection.network]
}
