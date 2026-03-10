variable "aws_region" {
  default = "eu-west-2"
}

variable "db_user" {
  default = "postgres"
}

variable "db_password" {
  sensitive = true
}

variable "database_url" {
  sensitive = true
}
