resource "aws_cloudwatch_event_rule" "daily_etl" {
  name                = "ducks-etl-daily"
  schedule_expression = "cron(0 2 * * ? *)"
}
