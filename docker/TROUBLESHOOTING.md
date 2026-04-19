# 🔧 Docker & Workshop Troubleshooting Guide

Practical troubleshooting for instructors running the Open WebUI + Ollama workshop environment on Windows with an NVIDIA RTX 5090.

---

## Quick Checks

Run these **before** the workshop starts to verify everything is working:

```powershell
# 1. Docker is running
docker info | Select-String "Server Version"

# 2. Ollama is running and listening
curl http://localhost:11434/api/tags

# 3. GPU is visible to Ollama
ollama ps

# 4. Open WebUI container is running
docker ps --filter "name=open-webui" --format "table {{.Status}}\t{{.Ports}}"

# 5. Open WebUI can reach Ollama (from inside the container)
docker exec open-webui curl -s http://host.docker.internal:11434/api/tags

# 6. Students can reach the UI (replace with your actual IP)
curl http://localhost:3000
```

If all six pass, you're good to go.

---

## Container Won't Start

### Symptoms
- `docker compose up -d` fails or the container exits immediately.
- Error messages mentioning port conflicts or daemon issues.

### Cause
- **Port 3000 is already in use** by another process (Node dev server, Grafana, etc.).
- **Docker Desktop is not running** or the Docker daemon hasn't started.

### Fix

```powershell
# Check if Docker is running
docker info

# If not, start Docker Desktop from the Start Menu or:
& "C:\Program Files\Docker\Docker\Docker Desktop.exe"

# Find what's using port 3000
netstat -ano | findstr ":3000"

# Kill the conflicting process (replace <PID> with the actual PID)
Stop-Process -Id <PID> -Force

# Retry
cd C:\Src\agenticworkshop\docker
docker compose up -d
```

---

## Open WebUI Can't Reach Ollama

### Symptoms
- The UI loads but shows a connection error or "Ollama not reachable" banner.
- Models list is empty despite Ollama running.

### Cause
- **Ollama is only listening on `127.0.0.1`**, which is not accessible from inside the Docker container. It needs to listen on `0.0.0.0`.
- **Windows Firewall** is blocking connections on port 11434.

### Fix

```powershell
# Set Ollama to listen on all interfaces
[System.Environment]::SetEnvironmentVariable("OLLAMA_HOST", "0.0.0.0:11434", "User")

# Restart Ollama after changing the environment variable
# (close the Ollama tray icon and relaunch, or restart the service)

# Verify Ollama is listening on 0.0.0.0
netstat -ano | findstr ":11434"
# You should see 0.0.0.0:11434 — not 127.0.0.1:11434

# Test from inside the container
docker exec open-webui curl -s http://host.docker.internal:11434/api/tags

# If firewall is the issue, add an inbound rule
New-NetFirewallRule -DisplayName "Ollama API" -Direction Inbound -LocalPort 11434 -Protocol TCP -Action Allow
```

---

## Models Not Appearing in the UI

### Symptoms
- Open WebUI loads fine but the model dropdown is empty.
- Students report "No models available."

### Cause
- Ollama is not running or hasn't finished starting.
- The `OLLAMA_BASE_URL` in `docker-compose.yml` doesn't match where Ollama is actually listening.
- Models haven't been pulled yet.

### Fix

```powershell
# Verify Ollama is running and responsive
curl http://localhost:11434/api/tags

# Pull the default workshop model if missing
ollama pull mistral:7b

# Confirm models are listed
ollama list

# Verify the API URL inside the container matches docker-compose.yml
docker exec open-webui printenv OLLAMA_BASE_URL
# Should output: http://host.docker.internal:11434

# If you changed docker-compose.yml, recreate the container
cd C:\Src\agenticworkshop\docker
docker compose down
docker compose up -d
```

---

## Slow or Hanging Responses

### Symptoms
- Model responses take 30+ seconds to start.
- Tokens trickle in extremely slowly.
- First prompt is slow, subsequent prompts are fast.

### Cause
- **Model not loaded into VRAM yet.** The first prompt after startup triggers a model load which takes 10–30 seconds depending on model size.
- **GPU not being used** — Ollama is falling back to CPU inference.
- **Model is too large** for available VRAM and is partially offloaded to system RAM.

### Fix

```powershell
# Check if GPU is being used
ollama ps
# The "PROCESSOR" column should show your GPU (e.g., "100% GPU")

# Pre-warm the model before students arrive
curl http://localhost:11434/api/generate -d '{"model": "mistral:7b", "prompt": "hello", "stream": false}'

# Check VRAM usage
nvidia-smi

# If GPU is not listed, see the "GPU Not Being Used" section below
```

---

## GPU Not Being Used

### Symptoms
- `ollama ps` shows CPU instead of GPU.
- `nvidia-smi` doesn't list Ollama or shows 0% GPU utilization.
- Inference is painfully slow.

### Cause
- **NVIDIA drivers are outdated or missing.**
- **Ollama was installed before the GPU drivers** and didn't detect the GPU.
- **CUDA toolkit issue** — Ollama bundles its own CUDA runtime, but driver compatibility still matters.

### Fix

```powershell
# Verify GPU is visible to the system
nvidia-smi
# Should show RTX 5090 with driver version

# Check minimum driver version — Ollama requires NVIDIA driver >= 452.39
# RTX 5090 requires much newer drivers; update to latest from:
# https://www.nvidia.com/Download/index.aspx

# After updating drivers, restart Ollama and test
ollama ps

# Verify with a generation — watch nvidia-smi in another terminal
nvidia-smi --loop=1
```

> **Note:** Ollama runs directly on the Windows host, not inside Docker, so Docker GPU passthrough configuration is not needed for this setup.

---

## Students Can't Connect

### Symptoms
- Students see "connection refused" or "site can't be reached" in their browser.
- The UI works on the instructor machine (localhost:3000) but not from student laptops.

### Cause
- **Windows Firewall** is blocking inbound connections on port 3000.
- Students are using the **wrong IP address**.
- **Browser cache** is showing a stale error page.

### Fix

```powershell
# Find the correct IP to share with students
Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.PrefixOrigin -eq "Dhcp" -or $_.PrefixOrigin -eq "Manual" } | Select-Object IPAddress, InterfaceAlias

# Open port 3000 in Windows Firewall
New-NetFirewallRule -DisplayName "Workshop Open WebUI" -Direction Inbound -LocalPort 3000 -Protocol TCP -Action Allow

# Verify the container is listening on 0.0.0.0:3000 (not 127.0.0.1)
netstat -ano | findstr ":3000"

# Test from a student machine (or use your phone on the same network)
# http://<instructor-ip>:3000

# If students see a stale page, have them hard-refresh
# Ctrl+Shift+R (or Ctrl+F5) in the browser
```

> **Tip:** Write the URL on the whiteboard: `http://<your-ip>:3000`

---

## Resetting Open WebUI to a Clean State

### Symptoms
- Old chat history or settings from a previous workshop are cluttering the UI.
- Configuration is in a bad state and you want a fresh start.

### Cause
- The `open-webui-data` Docker volume persists data across container restarts by design.

### Fix

```powershell
cd C:\Src\agenticworkshop\docker

# Stop and remove the container and its volume
docker compose down -v

# Verify the volume is gone
docker volume ls | findstr "open-webui"

# Start fresh
docker compose up -d
```

> **Warning:** This deletes all chat history, user settings, and uploaded documents. Do this **before** the workshop, not during.

---

## Checking Logs

When something isn't working and the cause isn't obvious, check the logs:

```powershell
# Open WebUI container logs (last 100 lines)
docker logs open-webui --tail 100

# Follow logs in real time (Ctrl+C to stop)
docker logs open-webui -f

# Ollama logs (if running as a Windows service)
# Check the Ollama log file at:
Get-Content "$env:LOCALAPPDATA\Ollama\logs\server.log" -Tail 50

# Look for specific errors in Open WebUI logs
docker logs open-webui 2>&1 | Select-String -Pattern "error|failed|refused"
```

---

## Quick Reference

| What | Command |
|---|---|
| Start everything | `cd C:\Src\agenticworkshop\docker && docker compose up -d` |
| Stop everything | `docker compose down` |
| Full reset | `docker compose down -v && docker compose up -d` |
| Container status | `docker ps --filter "name=open-webui"` |
| Open WebUI logs | `docker logs open-webui --tail 50` |
| Ollama status | `curl http://localhost:11434/api/tags` |
| GPU status | `nvidia-smi` |
| Loaded models | `ollama ps` |
| Your IP address | `Get-NetIPAddress -AddressFamily IPv4` |
