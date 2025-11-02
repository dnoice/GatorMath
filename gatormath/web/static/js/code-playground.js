/**
 * Metadata:
 *     Project: GatorMath
 *     File Name: code-playground.js
 *     File Path: gatormath/web/static/js/code-playground.js
 *     Module: Code Playground
 *     Created: 2025-11-02
 *     Modified: 2025-11-02
 *     Version: 1.0.0
 *     Author: Dennis 'dnoice' Smaltz
 *     AI Acknowledgement: Claude Code
 *
 * Description:
 *     Interactive JavaScript code editor with live execution and output display.
 *     Captures console.log and console.error output and displays in a styled
 *     output panel. Uses eval() for code execution (client-side only).
 *
 * Exports (Global):
 *     - window.runCode(): Execute code from editor textarea
 *
 * Features:
 *     - Code editor (textarea with monospace font)
 *     - Run button to execute code
 *     - Output panel with log/error styling
 *     - Console.log capture and redirection
 *     - Console.error capture with styling
 *     - JSON stringify for object logging
 *     - Try-catch error handling
 *
 * Dependencies:
 *     - Native JavaScript eval()
 *     - Console API override
 *
 * Security Note:
 *     - Uses eval() for code execution
 *     - Client-side only (no server execution)
 *     - Runs in user's browser context
 *     - No persistent storage or external API calls
 */

// ===== CODE PLAYGROUND =====
// Interactive code editor with live execution

window.runCode = function() {
    const code = document.getElementById('codeEditor').value;
    const output = document.getElementById('codeOutput');
    output.innerHTML = '';

    const originalLog = console.log;
    const originalError = console.error;

    console.log = (...args) => {
        const div = document.createElement('div');
        div.className = 'log';
        div.textContent = args.map(arg =>
            typeof arg === 'object' ? JSON.stringify(arg, null, 2) : String(arg)
        ).join(' ');
        output.appendChild(div);
    };

    console.error = (...args) => {
        const div = document.createElement('div');
        div.className = 'error';
        div.textContent = args.join(' ');
        output.appendChild(div);
    };

    try {
        eval(code);
    } catch (error) {
        const div = document.createElement('div');
        div.className = 'error';
        div.textContent = 'Error: ' + error.message;
        output.appendChild(div);
    }

    console.log = originalLog;
    console.error = originalError;
};

// Add keyboard shortcut for code editor
const codeEditor = document.getElementById('codeEditor');
if (codeEditor) {
    codeEditor.addEventListener('keydown', (e) => {
        // Ctrl+Enter or Cmd+Enter to run code
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            e.preventDefault();
            runCode();
        }

        // Tab key for indentation
        if (e.key === 'Tab') {
            e.preventDefault();
            const start = codeEditor.selectionStart;
            const end = codeEditor.selectionEnd;
            codeEditor.value = codeEditor.value.substring(0, start) + '  ' + codeEditor.value.substring(end);
            codeEditor.selectionStart = codeEditor.selectionEnd = start + 2;
        }
    });
}
