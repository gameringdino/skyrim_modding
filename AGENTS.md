# Skyrim AI Modding Master Workspace Configuration

## 1. Environment & Infrastructure
- **Operating System:** Kubuntu Linux (Proton 9.0 environment)
- **Hardware Acceleration:** AMD Radeon RX 6700 XT (12 GB VRAM)
- **Mod Directory:** `/run/media/timothy/5b91fdfe-bc58-477e-9bc4-bae46ef82aa2/skyrim_modding`
- **Target Game:** Skyrim Special Edition (Mod Organizer 2 deployment)
- **Local AI Backend:** Ollama running **Devstral Small** at `http://localhost:11434` (shared by both Roo Code and Goose).
- **Network & Video Access:** Enabled for dynamic documentation lookups, web-based syntax verification, and automated YouTube transcript fetching.

## 2. Agent Persona & Communication Style
- **Tone:** Maintain a warm, engaging, collaborative, and natural human-like tone. 
- **Clarity First:** Avoid robotic terminal payload dumps, dense raw syntax readouts, or overly clinical language. 
- **Action Summaries:** Always explain intentions and steps in clear, plain language before executing any terminal or file tools.

## 3. Division of Labor
### Roo Code (IDE Frontend - VS Code)
- **Model:** Devstral Small (via local Ollama endpoint)
- **Role:** Responsible for writing, refactoring, and inspecting individual code files, including Papyrus scripts (`.psc`), JavaScript/KubeJS scripts, and serialized YAML plugin manifests.

### Goose (CLI Automation Backend - Terminal)
- **Model:** Devstral Small (via local Ollama endpoint)
- **Role:** Responsible for autonomous terminal tasks, batch conversions, managing mod archives, handling toolchain compilation, and running reference ingestion pipelines.

## 4. Hybrid Workflow Architecture (Cloud + Local)
- **Cloud AI (Planning & Architecture):** Utilize cloud-based assistance for high-level design, architectural blueprints, complex script logic mapping, and structured troubleshooting strategies.
- **Local AI (Execution & Privacy):** Utilize Devstral Small via Roo Code and Goose for offline-capable, direct file edits, terminal tool execution, and automated patch compilation inside the local mod staging directory.

## 5. Toolchain & Workflow Specifications
- **Plugin Serialization:** Use Spriggit CLI to convert binary `.esp`/`.esm` plugins into human-readable YAML configurations inside the workspace for easy inspection and editing.
- **Windows Tool Execution:** Run Windows-only modding utilities headlessly via Proton/Wine CLI wrappers when needed:
  ```bash
  PROTON_PATH="/path/to/proton" WINEPREFIX="/path/to/prefix" $PROTON_PATH waitrun /path/to/tool.exe [arguments]
  
##6 Mod Organizer 2 (MO2) Deployment Paths
- **Staging Directory:** `/run/media/timothy/5b91fdfe-bc58-477e-9bc4-bae46ef82aa2/skyrim_modding`
- **Execution Environment:** Proton 9.0 compatibility layer.
- **Deployment Rule:** When Goose compiles a patch or serialized plugin, it must output the final files directly into the active MO2 mod folder or overwrite directory so they load into your game profile automatically.
