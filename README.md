# simple-log-analysis
Basic log analysis to detect failed login attempts

## Purpose
This project demonstrates basic log analysis techniques to identify
failed authentication attempts and potential brute-force activity.

## What this project does
- Parses authentication logs
- Extracts failed login attempts
- Aggregates attempts by source IP
- Flags potential brute-force sources

## Security relevance
Log analysis is a core defensive technique used in SOC and Blue Team
operations to detect suspicious behavior early.

## Running with Docker
```bash
docker build -t simple-log-analysis .
docker run simple-log-analysis
```
