resource "google_compute_network" "e2e_vpc_network" {
    name = "khaddock-sailor-e2e-vpc"
    description = "Virtual Private Cloud hosting machines for e2e testing"
    auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "e2e_vpc_subnet" {
  name          = "khaddock-sailor-e2e-eu-we3-subnet"
  ip_cidr_range = "10.156.0.0/20"
  region        = "europe-west3"
  network       = google_compute_network.e2e_vpc_network.id
}

resource "google_compute_firewall" "e2e_fw_allow_ssh" {
  name        = "khaddock-sailor-e2e-tcp-22-allow-rule"
  network     = google_compute_network.e2e_vpc_network.name
  description = "Allow SSH to instances tagged as 'e2e'."

  allow {
    protocol  = "tcp"
    ports     = ["22"]
  }

  source_ranges = ["78.236.232.245/32"]
  target_tags = ["khaddock-sailor-e2e"]
}

resource "google_compute_instance" "e2e_compute" {
  name         = "khaddock-sailor-e2e"
  machine_type = "e2-medium"
  zone         = "europe-west3-a"

  tags = ["khaddock-sailor-e2e"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size = "10"
    }
  }

  metadata = {
    ssh-keys = "madjlzz:${var.ssh_public_key}"
  }

  network_interface {
    network = google_compute_network.e2e_vpc_network.name
    subnetwork = google_compute_subnetwork.e2e_vpc_subnet.name
    access_config {
      
    }
  }

}

resource "local_file" "ansible_inventory" {
  content = templatefile("${path.module}/templates/inventory.tftpl",
    {
      instance_external_ip = google_compute_instance.e2e_compute.network_interface.0.access_config.0.nat_ip
    }
  )
  filename = "../ansible/inventories/khaddock-sailor.ini"

  lifecycle {
    prevent_destroy = false
  }

}
