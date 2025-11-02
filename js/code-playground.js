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
