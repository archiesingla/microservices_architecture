provider "google" {
    region = var.region
    project = var.project_id
}
resource "google_container_cluster" "gke_cluster"{
    name = "k8s-cluster"
    location = var.region
    initial_node_count = 1
    remove_default_node_pool = true
    deletion_protection = false
    node_config {
        disk_size_gb = 10
    }
}
resource "google_container_node_pool" "node_pool"{
    name = "k8s-cluster-node"
    location= var.region
    cluster = google_container_cluster.gke_cluster.name
    node_count = 1
    node_config{
        preemptible = true
        machine_type = var.machine_type
        image_type   = var.image_type
        disk_size_gb = 10
    }
}


resource "google_artifact_registry_repository" "k8s_repo" {
    location = var.region
    project = var.project_id
    repository_id = var.repo_name
    format = "DOCKER"
}