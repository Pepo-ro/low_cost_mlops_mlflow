module "db" {
  source           = "./modules/postgresql/modules/postgresql"
  db_name          = var.db_name
  database_version = var.database_version
  name             = "${var.project}-dashboard"
  region           = var.region
  zone             = var.zone
  project_id       = var.project
  user_name        = var.db_user_name
  user_password    = var.db_password
  ip_configuration = {
    ipv4_enabled        = false
    authorized_networks = []
    require_ssl         = false
    private_network     = google_compute_network.private_network.self_link
  }
  module_depends_on = [google_service_networking_connection.private_vpc_connection.network]
}
