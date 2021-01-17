
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

# GCS 設定
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

