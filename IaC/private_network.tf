resource "random_id" "name" {
  byte_length = 2
}

locals {
  private_network_name = "private-network-${random_id.name.hex}"
  private_ip_name      = "private-ip-${random_id.name.hex}"
}

resource "google_compute_network" "private_network" {
  name    = local.private_network_name
  project = var.project
}

resource "google_compute_global_address" "private_ip_address" {
  name          = local.private_ip_name
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = google_compute_network.private_network.self_link
}

resource "google_service_networking_connection" "private_vpc_connection" {
  provider                = google-beta
  network                 = google_compute_network.private_network.self_link
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
}

resource "google_vpc_access_connector" "connector" {
  name          = var.private_network_connector_name
  project       = var.project
  region        = var.region
  ip_cidr_range = var.ip_cidr_range
  network       = google_compute_network.private_network.name
}
