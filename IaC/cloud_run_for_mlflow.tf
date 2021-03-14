resource "google_cloud_run_service" "mlflow_cloudrun" {
  name     = "mlflow-cloudrun"
  location = var.region

  template {
    spec {
      containers {
        image = "asia.gcr.io/${var.project}/mlflow-cloudrun"

        resources {
          limits = { "memory" : "512Mi" }
        }
        env {
          name  = "STORE_URI"
          value = "postgresql+psycopg2://${var.db_user_name}:${var.db_password}@${module.db.private_ip_address}:5432/${var.db_name}"
        }
        env {
          name  = "ARTIFACTE_URI"
          value = "gs://${google_storage_bucket_object.artifacts.bucket}/${google_storage_bucket_object.artifacts.name}"
        }
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale"        = "1000"
        "run.googleapis.com/vpc-access-connector" = google_vpc_access_connector.connector.name
        "run.googleapis.com/vpc-access-egress"    = "private-ranges-only"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
  autogenerate_revision_name = true
}

data "google_iam_policy" "cloud_run_asia_iam_policy" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "cloud_run_asia_policy" {
  location = google_cloud_run_service.mlflow_cloudrun.location
  project  = google_cloud_run_service.mlflow_cloudrun.project
  service  = google_cloud_run_service.mlflow_cloudrun.name

  policy_data = data.google_iam_policy.cloud_run_asia_iam_policy.policy_data
}
