variable "machine_type"{
    type = string
    default = "e2-micro"
}

variable "disk_type"{
    type = string
    default = "pd-standard"
}

variable "image_type"{
    type = string
    default = "COS_CONTAINERD"
}

variable "region"{
    type = string
    default = "us-central1"
}

variable "project_id"{
    type = string
    default = "k8s-assignment-453321"
}

variable "repo_name"{
    type = string
    default = "k8s-repo"
}




