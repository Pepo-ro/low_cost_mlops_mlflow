variable "project" {
  type = string
}

variable "credentials_file" {
  type = string
}

variable "region" {
  type = string
}

variable "zone" {
  type = string
}

variable "private_network_connector_name" {
  type    = string
  default = "private-network-connector"
}

variable "ip_cidr_range" {
  type    = string
  default = "10.8.0.0/28"
}

# GCS params
variable "bucket_name" {
  type = string
}

variable "bucket_location" {
  type    = string
  default = "US"
}

variable "storage_class" {
  type    = string
  default = "STANDARD"
}

variable "versioning_enabled" {
  type    = bool
  default = true
}

variable "content" {
  type = string
}

# db params
variable "db_name" {
  type    = string
  default = "default"
}

variable "database_version" {
  type    = string
  default = "POSTGRES_12"
}

variable "ip_configuration" {
  default = {
    ipv4_enabled        = false
    authorized_networks = []
    require_ssl         = true
    private_network     = ""
  }
}

variable "db_password" {
  type    = string
  default = ""
}

variable "db_user_name" {
  type    = string
  default = "default"
}
