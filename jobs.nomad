job "hitos" { // -*- mode: hcl -*- 
  datacenters = ["dc1"]

  group "cc" {
    task "data" {
      driver = "podman"

      config {
        image = "docker://jjmerelo/hitos/data:latest"
      }
    }
  }
}
