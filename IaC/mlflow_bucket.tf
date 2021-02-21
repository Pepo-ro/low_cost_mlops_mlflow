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