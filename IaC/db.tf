module "db" {
  source           = "./modules/postgresql/modules/postgresql"
  db_name          = var.db_name
  database_version = var.database_version
  name             = "${var.project}-dashboard-sample"
  region           = var.region
  zone             = var.zone
  project_id       = var.project
}
