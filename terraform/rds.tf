resource "aws_db_instance" "postgres" {
  identifier          = "ducks-etl-db"
  allocated_storage   = 20
  engine              = "postgres"
  engine_version      = "15"
  instance_class      = "db.t3.micro"
  username            = var.db_user
  password            = var.db_password
  skip_final_snapshot = true
  publicly_accessible = true
}
