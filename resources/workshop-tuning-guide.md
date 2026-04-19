# Workshop-Day Ollama Tuning Guide

> **Audience:** Instructor running Agentic AI 101 on the workshop host machine.
> **Hardware:** NVIDIA RTX 5090 (32 GB VRAM) · Gen5 NVMe storage · Windows · Ollama via scheduled task "Ollama Serve"
> **Workshop models:** `tinyllama:1.1b` · `llama3.2:3b` · `mistral:7b` · `llava:7b`

---

## Current Baseline Configuration

These environment variables are **already set** as persistent env vars on the host and should stay in place:

| Variable | Value | Scope | Purpose |
|---|---|---|---|
| `OLLAMA_HOST` | `0.0.0.0:11434` | User | Listen on all interfaces so students can connect |
| `OLLAMA_FLASH_ATTENTION` | `1` | Machine | Enable Flash Attention for faster inference |
| `OLLAMA_KV_CACHE_TYPE` | `q8_0` | Environment | Quantized KV cache — reduces per-model VRAM overhead |
| `OLLAMA_CONTEXT_LENGTH` | `131072` | Environment | 128k context window (personal use — **too large for workshop**) |

> ⚠️ **The 128k context length is the single biggest VRAM waste during the workshop.** Each loaded model allocates KV cache proportional to context length. Workshop prompts rarely exceed 500 tokens, so 128k is ~16× more than needed.

---

## 1. Workshop-Day Environment Variables

Set these **additional** variables before the workshop begins:

### `OLLAMA_KEEP_ALIVE=2m`

Models unload from VRAM **2 minutes** after the last request (default: 5m).

- Gen5 NVMe cold-loads take only 1.0–1.5 s, so aggressive unloading is fine.
- Prevents VRAM contention when students switch between models.

> ⚠️ **Why this matters:** If models stay loaded too long, VRAM fills up and later model requests spill to system RAM → CPU processing → **10–50× slower responses.**

### `OLLAMA_NUM_PARALLEL=4`

Allow **4 concurrent requests** per loaded model (default: 1, which queues everything).

- Benchmarked: RTX 5090 handles **10 concurrent requests** to `mistral:7b` with a max response time of only 1.1 s.
- Setting to 4 is conservative and leaves headroom.

> 💡 Higher values (up to 10) work, but 4 keeps per-request latency predictable and VRAM allocation modest.

### `OLLAMA_MAX_LOADED_MODELS=2`

Keep at most **2 models** in VRAM simultaneously (default: auto, which can fill VRAM).

- Worst-case combo: `tinyllama` (1.2 GB) + `mistral` (8.3 GB) = ~9.5 GB — leaves plenty of headroom on 32 GB.
- Prevents the scenario where four different students load four different models and exhaust VRAM.

> ✅ With `OLLAMA_KEEP_ALIVE=2m`, idle models unload quickly, so the 2-model cap rarely blocks requests in practice.

### `OLLAMA_CONTEXT_LENGTH=8192`

Reduce context window from **128k → 8k** for the workshop.

- Workshop prompts are short (rarely over 500 tokens).
- Massively reduces per-model VRAM overhead from KV cache allocation.
- The 128k default is for personal use with long documents — not needed here.

> ⚠️ **This is the highest-impact change.** Restoring the original 128k value after the workshop is critical (see [Section 3](#3-how-to-revert-after-workshop)).

---

## 2. How to Apply (Step by Step)

### Step 1 — Open PowerShell as Administrator

### Step 2 — Set each env var at User level

```powershell
[System.Environment]::SetEnvironmentVariable("OLLAMA_KEEP_ALIVE", "2m", "User")
[System.Environment]::SetEnvironmentVariable("OLLAMA_NUM_PARALLEL", "4", "User")
[System.Environment]::SetEnvironmentVariable("OLLAMA_MAX_LOADED_MODELS", "2", "User")
[System.Environment]::SetEnvironmentVariable("OLLAMA_CONTEXT_LENGTH", "8192", "User")
```

### Step 3 — Restart Ollama via the scheduled task

> ⚠️ **Do NOT kill the Ollama process directly.** Always use the scheduled task so it restarts cleanly.

```powershell
Stop-ScheduledTask -TaskName "Ollama Serve"
Start-Sleep 5
Start-ScheduledTask -TaskName "Ollama Serve"
```

### Step 4 — Verify

```powershell
curl http://localhost:11434/api/ps
```

You should see an empty `models` array (nothing loaded yet). If you get a connection error, wait a few seconds and retry — the task may still be starting.

> 💡 To confirm env vars took effect, run a quick inference and check `nvidia-smi` — VRAM usage per model should be noticeably lower than with 128k context.

---

## 3. How to Revert After Workshop

> ⚠️ **CRITICAL: No permanent changes should remain on the machine after the workshop.** Follow every step below.

### Step 1 — Remove workshop-specific vars and restore originals

```powershell
# Remove workshop-only variables
[System.Environment]::SetEnvironmentVariable("OLLAMA_KEEP_ALIVE", $null, "User")
[System.Environment]::SetEnvironmentVariable("OLLAMA_NUM_PARALLEL", $null, "User")
[System.Environment]::SetEnvironmentVariable("OLLAMA_MAX_LOADED_MODELS", $null, "User")

# Restore original 128k context length
[System.Environment]::SetEnvironmentVariable("OLLAMA_CONTEXT_LENGTH", "131072", "User")
```

### Step 2 — Restart the scheduled task

```powershell
Stop-ScheduledTask -TaskName "Ollama Serve"
Start-Sleep 5
Start-ScheduledTask -TaskName "Ollama Serve"
```

### Step 3 — Verify original behavior is restored

```powershell
curl http://localhost:11434/api/ps
```

> ✅ **Checklist before leaving the machine:**
> - [ ] `OLLAMA_KEEP_ALIVE` is removed (not present in User env vars)
> - [ ] `OLLAMA_NUM_PARALLEL` is removed
> - [ ] `OLLAMA_MAX_LOADED_MODELS` is removed
> - [ ] `OLLAMA_CONTEXT_LENGTH` is back to `131072`
> - [ ] Ollama scheduled task is running

---

## 4. Benchmark Data (Why These Values)

All benchmarks taken on the workshop host: **RTX 5090 (32 GB) · Gen5 NVMe · Ollama with Flash Attention + q8_0 KV cache.**

### Model Cold-Load Times (Gen5 NVMe)

| Model | Cold-Load Time |
|---|---|
| `tinyllama:1.1b` | ~1.0 s |
| `llama3.2:3b` | ~1.5 s |
| `mistral:7b` | ~1.5 s |

> 💡 These times are why `OLLAMA_KEEP_ALIVE=2m` is safe — a 1–1.5 s reload is imperceptible compared to generation time.

### Single-User Response Times (Model Warm)

| Model | Avg Response Time | Throughput |
|---|---|---|
| `tinyllama:1.1b` | 0.4 s | ~840 tok/s |
| `llama3.2:3b` | 1.2 s | ~420 tok/s |
| `mistral:7b` | 1.1 s | ~257 tok/s |

### 10-Concurrent-User Response Times

| Model | Max Response Time |
|---|---|
| `tinyllama:1.1b` | 0.7 s |
| `llama3.2:3b` | 0.6 s |
| `mistral:7b` | 1.1 s |

> ✅ Even under 10× concurrency, worst-case response stays at ~1 s. The RTX 5090 has headroom to spare for the workshop models.

### VRAM Footprints

| Model | VRAM Usage |
|---|---|
| `tinyllama:1.1b` | ~1.2 GB |
| `llama3.2:3b` | ~3.5 GB |
| `mistral:7b` | ~8.3 GB |
| `llava:7b` | ~8.4 GB |
| `phi4:14b` | ~10.8 GB |

### Models NOT Recommended for Student-Facing Use

| Model | Issue |
|---|---|
| `qwen3.5:9b` | **22+ seconds per response** — reasoning model with internal chain-of-thought that generates thousands of hidden tokens before the visible answer |
| `deepseek-r1:14b` | **16–51 seconds per response** — same reasoning overhead, plus larger footprint |
| `phi4:14b` | 2.7 s avg response (acceptable) but **10.8 GB VRAM** footprint — loading it alongside `mistral:7b` uses 19+ GB and leaves little room for a second model |

> ⚠️ If a student accidentally selects one of these in Open WebUI, it will work but may appear "stuck" for 20–50 seconds. Tell students to **only use the four recommended models**.

---

## 5. Troubleshooting

### "Model responses are very slow"

**Check VRAM usage:**

```powershell
nvidia-smi
```

If VRAM usage is **>28 GB**, models are spilling to system RAM (CPU processing = 10–50× slower).

**Force-unload a specific model:**

```powershell
curl -X POST http://localhost:11434/api/generate -d '{"model":"MODEL_NAME","keep_alive":0}'
```

Replace `MODEL_NAME` with the model to evict (e.g., `mistral:7b`).

**Force-unload all models:**

```powershell
curl http://localhost:11434/api/ps
```

Note every loaded model, then unload each one with the command above.

### "Students see long delays when switching models"

This is **expected behavior** — a 1–1.5 s cold load while the new model is read from NVMe into VRAM.

> 💡 **Tip:** Use `ollama-warmup.py` before labs that target a specific model to pre-load it into VRAM so the first student request is fast.

### "Open WebUI shows model but responses timeout"

Ollama may have crashed or the scheduled task may have stopped.

**Restart via the scheduled task:**

```powershell
Stop-ScheduledTask -TaskName "Ollama Serve"
Start-Sleep 5
Start-ScheduledTask -TaskName "Ollama Serve"
```

Then verify with `curl http://localhost:11434/api/ps`.

### "A student loaded a 14B model and now everything is slow"

Unload it immediately:

```powershell
curl -X POST http://localhost:11434/api/generate -d '{"model":"deepseek-r1:14b","keep_alive":0}'
```

With `OLLAMA_MAX_LOADED_MODELS=2`, this should self-correct once the model is evicted.

---

## 6. Open WebUI Tips

- **Tell students which model to select for each lab.** Write it on the board or include it in the lab instructions.
- The model dropdown **persists between chats** — students may forget to switch when moving to a new lab.
- Consider **pinning recommended models** in the Open WebUI admin settings so `tinyllama:1.1b`, `llama3.2:3b`, `mistral:7b`, and `llava:7b` appear at the top of the dropdown.

> 💡 If a student's chat seems broken, the first thing to check is whether they have the **correct model selected**. The second is whether the model is actually loaded (check `curl http://localhost:11434/api/ps`).

> ⚠️ Open WebUI caches the model list. If you pull or remove models in Ollama while Open WebUI is running, students may need to **refresh the browser** to see the updated list.

---

## Quick-Reference Card

Copy this to a sticky note on the workshop machine:

```
WORKSHOP START:
  Set env vars → Restart "Ollama Serve" → Verify /api/ps

WORKSHOP END:
  Remove env vars → Restore CONTEXT_LENGTH=131072 → Restart "Ollama Serve"

EMERGENCY:
  nvidia-smi                          # check VRAM
  curl localhost:11434/api/ps         # check loaded models
  curl -X POST .../api/generate       # unload with keep_alive:0
  Stop/Start-ScheduledTask            # restart Ollama
```
