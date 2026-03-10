resource "aws_ecs_cluster" "main" {
  name = "ducks-etl-cluster"
}

resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ducks-etl-ecs-task-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      }
      Effect = "Allow"
    }]
  })
}

resource "aws_ecs_task_definition" "ducks_etl" {
  family                   = "ducks-etl"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
}
