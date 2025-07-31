function generateQuestion(types) {
    const op = types[Math.floor(Math.random() * types.length)];
    let a = Math.floor(Math.random() * 99) + 1;
    let b = Math.floor(Math.random() * 99) + 1;
    if (op === '+') {
        return `${a} + ${b} =`;
    } else if (op === '-') {
        return `${a} - ${b} =`;
    } else if (op === '*') {
        return `${a} × ${b} =`;
    } else if (op === '÷') {
        b = Math.floor(Math.random() * 9) + 1;
        a = b * (Math.floor(Math.random() * 9) + 1);
        return `${a} ÷ ${b} =`;
    }
    return "";
}

document.getElementById('generate').onclick = function () {
    const num = parseInt(document.getElementById('num').value);
    const types = [];
    if (document.getElementById('add').checked) types.push('+');
    if (document.getElementById('sub').checked) types.push('-');
    if (document.getElementById('mul').checked) types.push('*');
    if (document.getElementById('div').checked) types.push('÷');
    const result = document.getElementById('result');
    result.textContent = "";
    if (!num || num <= 0 || num > 10000) {
        alert("请输入正确的题目数量");
        return;
    }
    if (types.length === 0) {
        alert("请至少选择一个操作类型");
        return;
    }
    let line = "";
    for (let i = 0; i < num; i++) {
        line += generateQuestion(types).padEnd(12, ' ');
        if ((i + 1) % 3 === 0) {
            result.textContent += line + "\n";
            line = "";
        }
    }
    if (line) result.textContent += line + "\n";
};

document.getElementById('download').onclick = function () {
    const content = document.getElementById('result').textContent.trim();
    if (!content) {
        alert("请先生成题目");
        return;
    }
    const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "题目.txt";
    link.click();
};