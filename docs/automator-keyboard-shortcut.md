## macOS: Run `fmscript2xml` via a global keyboard shortcut

On macOS, the most reliable way to bind `fmscript2xml` to a keyboard shortcut is to use an **Automator Quick Action**.  
This avoids environment issues with Shortcuts and provides predictable clipboard access.

The examples below convert a FileMaker script from the clipboard and replace it with the XML output:

```sh
fmscript2xml --from-clipboard --clipboard --no-file
```

---

### Option A: Automator Quick Action (pyenv, Python 3.12.x)

Use this if `fmscript2xml` is installed via `pip` in a `pyenv` Python.

1. Open **Automator** → *New Document* → **Quick Action**
2. Set:
   - *Workflow receives current*: **no input**
   - *in*: **any application**
3. Add **Run Shell Script**
   - Shell: `/bin/zsh`
   - Pass input: *as arguments*
4. Paste the following script:

```zsh
#!/bin/zsh

PYENV_VERSIONS="$HOME/.pyenv/versions"

# Select the newest installed Python 3.12.x
V=$(ls -1d "$PYENV_VERSIONS"/3.12.* 2>/dev/null | sort -V | tail -n 1)

if [[ -z "$V" ]]; then
  osascript -e 'display alert "fmscript2xml failed" message "No Python 3.12.x found under ~/.pyenv/versions"'
  exit 1
fi

"$V/bin/fmscript2xml" --from-clipboard --clipboard --no-file
```

5. Save the Quick Action (e.g. **Convert FM Script (Clipboard)**)
6. Assign a keyboard shortcut in **System Settings → Keyboard → Keyboard Shortcuts → Services**

   **Recommended shortcut:** **⌘⌥⌃F** (Command–Option–Control–F). It’s easy to remember (F for FileMaker) and rarely conflicts with other apps.

This approach is resilient to Python 3.12 patch upgrades and does not rely on shell initialisation files.

---

### Option B: Automator Quick Action (standard shell install)

Use this if `fmscript2xml` is available directly in your `PATH`
(e.g. installed system-wide or via `pipx`).

Steps 1–3 are the same as above.  
In **Run Shell Script**, use:

```zsh
#!/bin/zsh

fmscript2xml --from-clipboard --clipboard --no-file
```

Save the Quick Action and assign a keyboard shortcut (recommended: **⌘⌥⌃F**) in **System Settings → Keyboard → Keyboard Shortcuts → Services**.

---

### Notes

- **Recommended keyboard shortcut:** **⌘⌥⌃F** (Command–Option–Control–F) — memorable (F for FileMaker) and usually conflict-free.
- On first use, macOS may prompt for clipboard or automation permissions.
- If the action fails silently, check **System Settings → Privacy & Security** for Automator permissions.
