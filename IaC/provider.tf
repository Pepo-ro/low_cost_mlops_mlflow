terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials_file)
  project     = var.project
  region      = var.region
  zone        = var.zone
}

resource "google_storage_bucket" "ml_bucket" {
  name          = var.bucket_name
  location      = var.bucket_location
  storage_class = var.storage_class

  versioning {
    enabled = var.versioning_enabled
  }
}

resource "google_storage_bucket_object" "artifacts" {
  name    = "artifacts/"
  bucket  = google_storage_bucket.ml_bucket.name
  content = var.content
}

resource "google_storage_bucket_object" "mlruns" {
  name    = "mlruns/"
  bucket  = google_storage_bucket.ml_bucket.name
  content = var.content
}