provider "google" {
  project = "playground-s-11-0914590e"
  region  = "us-east1" # Região padrão (não afeta as instâncias específicas)
  credentials = file("chave.json")
}

resource "google_compute_instance" "vm1" {
  name         = "vm-us-east1"
  machine_type = "e2-medium"
  zone = "us-east1-d"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata = {
    ssh-keys = "rodrigo2186@gmail.com:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHRu764qeva8AAmab6g2NvTtqcsSqrWqcwbkLBMw3CUk rodrigo2186@gmail.com"
  }

  metadata_startup_script = <<EOT
#!/bin/bash
sudo apt update && sudo apt install -y python3 python3-pip chromium-driver
pip3 install selenium
git clone https://github.com/rodrigo210686/selenium-acess-we-page.git
cd selenium-acess-we-page/
nohup setsid /usr/bin/python3 -u access-web.py > output.log 2>&1 &

EOT
}

resource "google_compute_instance" "vm2" {
  name         = "vm-europe-west1"
  machine_type = "e2-medium"
#  zone         = "europe-west1-b"
  zone         = "us-east1-b"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata = {
    ssh-keys = google_compute_instance.vm1.metadata.ssh-keys
  }

  metadata_startup_script = google_compute_instance.vm1.metadata_startup_script
}

resource "google_compute_instance" "vm3" {
  name         = "vm-us-east4"
  machine_type = "e2-medium"
#  zone         = "australia-southeast1-a"
  zone         = "us-east1-c"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata = {
    ssh-keys = google_compute_instance.vm1.metadata.ssh-keys
  }

  metadata_startup_script = google_compute_instance.vm1.metadata_startup_script
}

output "public_ips" {
  value = {
    vm1 = google_compute_instance.vm1.network_interface[0].access_config[0].nat_ip
    vm2 = google_compute_instance.vm2.network_interface[0].access_config[0].nat_ip
    vm3 = google_compute_instance.vm3.network_interface[0].access_config[0].nat_ip
  }
}
                             
