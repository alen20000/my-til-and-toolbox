# comfyui-setup

記錄 comfyui 的基礎環境路徑與關鍵配置，確保知識系統的可維護性。

## web-access
- local-url: `http://127.0.0.1:8188`
- documentation: `https://docs.comfy.org/`
- official github `https://github.com/Comfy-Org/ComfyUI`

## important-directories
- root: `comfyui_windows_portable`
- custom-nodes: `...\comfyui\custom_nodes`
- models: `...\comfyui\models`
- output: `...\comfyui\output`
- workflows `...\ComfyUI\user\default\workflows`

## environment-notes
syn:python.default-interpreter-path - 指向 `.../python_embeded/python.exe`
syn:git.pull - 定期執行 `git pull` 以確保 custom_nodes 更新

params:
    - --listen 127.0.0.1 (預設監聽地址)
    - --port 8188 (預設埠號)