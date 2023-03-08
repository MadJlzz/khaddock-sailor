variable "ssh_public_key" {
    type = string
    description = "Public SSH key that will be added to the authorized file of the e2e instance."
    default = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBzS1voPJdCLDvWZJyEEoHXxaCcFBmQK8kuZZ5yZOiUz madjlzz@madnux"
}